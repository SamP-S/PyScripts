from ctypes import *
from ctypes.wintypes import *

# imports subroutine to get process id (PID)
from subprocess import check_output

# cmd command to be executed 
# tasklist /nh /v /fo csv /fi "ImageName eq notepad.exe"
def get_pid(name):
    task = name + ".exe"
    process = check_output(["tasklist","/nh","/v","/fo","csv","/fi", "ImageName eq " + task], shell=True).decode("utf-8")
    pid = int(process.split(",")[1].replace('\"',''))
    return pid

PROCESS_ID = get_pid("notepad")


# read from addresses
STRLEN = 255

# access memory access level
PROCESS_VM_READ =       0x0010     #dwDesiredAccess read level
PROCESS_VM_WRITE =      0x0020     #dwDesiredAccess write level
PROCESS_ALL_ACCESS =    0x1F0FFF   #dwDesiredAccess all level

k32 = WinDLL('kernel32', use_last_error=True)
print("The kernel32 is %s" % k32)

k32.GetModuleHandleW.argtypes = [LPCWSTR]
k32.GetModuleHandleW.restype = HMODULE
k32.LoadLibraryW.argtype = [LPCWSTR]
k32.LoadLibraryW.restype = HMODULE
k32.OpenProcess.argtypes = DWORD,BOOL,DWORD     # dwDesiredAccess, bInheritHandle, dwProcessID
k32.OpenProcess.restype = HANDLE
k32.ReadProcessMemory.argtypes = HANDLE,LPVOID,LPVOID,c_size_t,POINTER(c_size_t)
k32.ReadProcessMemory.restype = BOOL

LOAD_MODULE_HANDLE = k32.LoadLibraryW("notepad.exe")
if LOAD_MODULE_HANDLE == None:
    print("LoadLibraryW: ", GetLastError())

PROCESS_MODULE_HANDLE = k32.GetModuleHandleW("notepad.exe")
if PROCESS_MODULE_HANDLE == None:
    print("GetModuleHandleW: ", GetLastError())

PROCESS_HANDLE = k32.OpenProcess(PROCESS_ALL_ACCESS, 0, PROCESS_ID)
if PROCESS_HANDLE == None:
    print("OpenProcess: ", GetLastError())

print("Load_Handle: ", LOAD_MODULE_HANDLE)
print("Header_Address: ", PROCESS_MODULE_HANDLE)
print("Process: ", PROCESS_HANDLE)

buf = create_string_buffer(STRLEN)
bytes_read = c_size_t()
if k32.ReadProcessMemory(PROCESS_HANDLE, PROCESS_MODULE_HANDLE, buf, STRLEN, byref(bytes_read)):
    print(bytes_read.value,buf.raw)
else:
    print("ReadProcessMemory: ", GetLastError())