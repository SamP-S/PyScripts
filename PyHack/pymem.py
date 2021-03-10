from typing import Any,  List, NewType
from ctypes import *
from ctypes.wintypes import *
import os.path

# Process Access Permisions
PROCESS_QUERY_INFORMATION   =   0x0400
PROCESS_VM_OPERATION        =   0x0008
PROCESS_VM_READ             =   0x0010
PROCESS_VM_WRITE            =   0x0020
PROCESS_ALL_ACCESS          =   0x1f0fff

# Module Processing
LIST_MODULES_32BIT      = 0x01   # List the 32-bit modules.
LIST_MODULES_64BIT      = 0x02   # List the 64-bit modules.
LIST_MODULES_ALL        = 0x03   # List all modules.
LIST_MODULES_DEFAULT    = 0x0    # Use the default behavior

# OS Max Path
MAX_PATH = 260

psapi = WinDLL('Psapi.dll')
#psapi.EnumProcesses.argtypes = LPDWORD,DWORD,LPDWORD
psapi.EnumProcesses.restype = BOOL
#psapi.EnumProcessModules.argtypes = HANDLE, HMODULE, DWORD, LPDWORD
psapi.EnumProcessModules.restype = BOOL
psapi.GetProcessImageFileNameW.argtypes = HANDLE,LPWSTR,DWORD
psapi.GetProcessImageFileNameW.restype = DWORD
psapi.GetProcessImageFileNameA.argtypes = HANDLE,LPSTR,DWORD
psapi.GetProcessImageFileNameA.restype = DWORD

k32 = WinDLL('kernel32', use_last_error=True)
k32.GetModuleHandleW.argtypes = [LPCWSTR]
k32.GetModuleHandleW.restype = HMODULE
k32.LoadLibraryW.argtype = [LPCWSTR]
k32.LoadLibraryW.restype = HMODULE
k32.OpenProcess.argtypes = DWORD,BOOL,DWORD
k32.OpenProcess.restype = HANDLE
k32.ReadProcessMemory.argtypes = HANDLE,LPVOID,LPVOID,c_size_t,POINTER(c_size_t)
k32.ReadProcessMemory.restype = BOOL
k32.CloseHandle.argtypes = [HANDLE]
k32.CloseHandle.restype = BOOL


class Process:
    # Process class to contain information about the process

    def __init__(self, name: str="", id: int=-1, handle: int=-1, error: str=None):
        self.name = name
        self.pid = id            # process id = PID
        self.handle = handle
        self.error_code = error      # error = error code

    # open process for read/write access
    def open(self):
        dw_desired_access = (PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_READ | PROCESS_VM_WRITE)
        b_inherit_handle = False
        self.handle = k32.OpenProcess(dw_desired_access, b_inherit_handle, self.pid)
        if not self.handle:
            raise Exception("Unable to open process: {}".format(self.name))

    def close(self) -> int:
        k32.CloseHandle(self.handle)
        return GetLastError()

    def get_all_access_handle(self) -> int:
    # Gets full access handle of the process.
    # return: handle of the process
        self.handle = k32.OpenProcess(PROCESS_ALL_ACCESS, True, self.pid)

    def get_base_address(self):
        count = 64
        try:
            if self.handle:
                hModules = (HMODULE * count)()
                #cb = ctypes.sizeof(hModules)
                cb = sizeof(hModules)
                bytes_returned = DWORD()
                psapi.EnumProcessModulesEx(self.handle, ctypes.byref(hModules), cb, ctypes.byref(bytes_returned), LIST_MODULES_ALL)
                #print("epm: handle=", self.handle, " hModule=", hModules, " cb=", cb, " bytes_returned=", bytes_returned)
                hModule_list = hModules[:]
                for i in range(len(hModule_list)-1, 0, -1):
                    if hModule_list[i] == None:
                        hModule_list.pop(i)
                print(hModule_list)
                return hModule_list
            else:
                print("handle no worky")
        except:
            print("EXCEPTION: EnumProcessModules failed: ", GetLastError())

    def get_pointer(self, lp_base_address: hex, offsets: List[hex]=()) -> int:
        # Get the pointer of a given address
        # lp_base_address: The address from where you want to get the pointer.
        # offsets: a list of offets.
        if not offsets:
            return lp_base_address
        else:
            pointer = lp_base_address
            for offset in offsets:
                pointer += offset
            return pointer

    def read(self, lp_base_address: int) -> Any:
        try:
            read_buffer = c_uint(0)
            lp_buffer = byref(read_buffer)
            n_size = ctypes.sizeof(read_buffer)
            number_of_bytes_read = ctypes.c_ulonglong(0)
            lp_number_of_bytes_read = ctypes.byref(number_of_bytes_read)
            mem_read = k32.ReadProcessMemory(self.handle, lp_base_address, lp_buffer, n_size, lp_number_of_bytes_read)
            #print("read: handle=", self.handle, " lp_base_address=", lp_base_address, " buffer=", read_buffer, " n_size=", n_size, " number_of_bytes_read=", number_of_bytes_read)
            #print("memory_read=", mem_read)
            return read_buffer.value
        except (BufferError, ValueError, TypeError) as error:
            if self.handle:
                self.close()
            self.error_code = GetLastError()
            print(error)
            error = {'msg': str("ERROR: exception"), 'Handle': self.handle, 'PID': self.pid,
                     'Name': self.name, 'ErrorCode': self.error_code}
            print(error['msg'])

    def write(self, lp_base_address: int, value: int) -> bool:
    # Write data to the process's memory.
    # param lp_base_address: The process' pointer.
    # param value: The data to be written to the process's memory
    # return: It returns True if succeed if not it raises an exception.
        try:
            write_buffer = ctypes.c_uint(value)
            lp_buffer = ctypes.byref(write_buffer)
            n_size = ctypes.sizeof(write_buffer)
            number_of_bytes_written = ctypes.c_ulonglong(0)
            lp_number_of_bytes_written = ctypes.byref(number_of_bytes_written)
            mem_written = k32.WriteProcessMemory(self.handle, lp_base_address, lp_buffer, n_size, lp_number_of_bytes_written)
            #print("write: handle=", self.handle, " lp_base_address=", lp_base_address, " buffer=", write_buffer, " n_size=", n_size, " number_of_bytes_written=", number_of_bytes_written)
            #print("memory_written=", mem_written)
            return True
        except:
            if self.handle:
                self.close()
            self.error_code = GetLastError()
            error = {'msg': str("ERROR: exception"), 'Handle': self.handle, 'PID': self.pid, 'Name': self.name, 'ErrorCode': self.error_code}
            print(error['msg'])
            return False


class ReadWriteMemory:

    # Class is used to read and write to the memory of a running processs

    def __init__(self):
        self.process = Process()

    def get_process_by_name(self, process_name: str) -> "Process":
    # description: Get the process by the process executabe\'s name and return a Process object.
    # param process_name: The name of the executable file for the specified process for example, my_program.exe.
    # return: A Process object containing the information from the requested Process.
        if not process_name.endswith(".exe"):
            process_name = process_name + '.exe'
        process_ids = self.enumerate_processes()
        for process_id in process_ids:
            self.process.handle = k32.OpenProcess(PROCESS_QUERY_INFORMATION, False, process_id)
            if self.process.handle:
                image_file_name = (c_char * MAX_PATH)()
                if psapi.GetProcessImageFileNameA(self.process.handle, image_file_name, MAX_PATH) > 0:
                    filename = os.path.basename(image_file_name.value)
                    if filename.decode('utf-8') == process_name:
                        self.process.pid = process_id
                        self.process.name = process_name
                        return self.process
                self.process.close()

    def get_process_by_id(self, process_id: int) -> "Process":
    # description: Get the process by the process ID and return a Process object.
    # param process_id: The process ID.
    # return: A Process object containing the information from the requested Process.
        self.process.handle = k32.OpenProcess(PROCESS_QUERY_INFORMATION, False, process_id)
        if self.process.handle:
            image_file_name = (c_char * MAX_PATH)()
            if psapi.GetProcessImageFileNameA(self.process.handle, image_file_name, MAX_PATH) > 0:
                filename = os.path.basename(image_file_name.value)
                self.process.pid = process_id
                self.process.name = filename.decode('utf-8')
                self.process.close()
                return self.process
            else:
                raise print("Unable to get the executable name for PID=", self.process.pid)

    @staticmethod
    def enumerate_processes() -> list:
    # Get the list of running processes ID's from the current system.
    # return: A list of processes ID's
        count = 64
        while True:
            process_ids = (DWORD * count)()
            cb = ctypes.sizeof(process_ids)
            bytes_returned = DWORD()
            if psapi.EnumProcesses(byref(process_ids), cb, byref(bytes_returned)):
                if bytes_returned.value < cb:
                    return list(set(process_ids))
                else:
                    count *= 2


###################################################################################


def main():
    print("read3.py")
    DEBUG_BASE_ADDRESS = False
    DEBUG_READ = True
    
    # memory mananger setup
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name("ac_client.exe")
    process.open()
    print("PID: ", process.pid, ", name: ", process.name)

    if DEBUG_BASE_ADDRESS:
        base_addr_list = process.get_base_address()
        for base_addr in base_addr_list:
            if base_addr != None:
                print(hex(base_addr))
            else:
                print("base_addr = NULL")

    if DEBUG_READ:
        # get local play address
        local_addr = process.read(0x400000 + 0x10F4F4)
        print("local_address = ", hex(local_addr))

        # READ
        # get health from local player
        isPosMoving = process.read(local_addr + 0x0070)
        print("isPosMoving = ", isPosMoving)
        speed = process.read(local_addr + 0x0080)
        print("speed = ", speed)
        health = process.read(local_addr + 0x00F8)
        print("health = ", health)

        # WRITE
        written = process.write(local_addr + 0x00F8, 10000)
        print("memory written = ", written)

if __name__ == "__main__":
    main()