import pymem
import ctypes
from ctypes import wintypes


class overlay:

    def __init__(self, handle):
        self.handle = handle
        #self.window_rect = RECT(0,0,0,0)
        #self.client_rect = RECT(0,0,0,0)

        self.u32 = ctypes.WinDLL('User32.dll')
        self.u32.GetWindowRect.argtypes = wintypes.HWND, wintypes.LPRECT
        self.u32.GetWindowRect.restype = wintypes.BOOL
        #self.u32.EnumWindows.argtypes = wintypes.WNDENUMPROC, wintypes.LPARAM
        self.u32.EnumWindows.restype = wintypes.BOOL
        self.u32.IsWindowVisible.argtypes = [wintypes.HWND]
        self.u32.IsWindowVisible.restype = wintypes.BOOL
        self.u32.IsWindowEnabled.argtypes = [wintypes.HWND]
        self.u32.IsWindowEnabled.restype = wintypes.BOOL
        self.u32.GetWindowThreadProcessId.argtypes = wintypes.HWND, wintypes.LPDWORD
        self.u32.GetWindowThreadProcessId.restype = wintypes.DWORD

    def get_window_rect(self, handle, rect):
        return self.u32.GetWindowRect(handle, ctypes.byref(rect))

    def get_hwnds_for_pid(self, pid):
        def callback(hwnd, hwnds):
            if self.u32.IsWindowVisible(hwnd) and self.u32.IsWindowEnabled(hwnd):
                found_pid = self.u32.GetWindowThreadProcessId(hwnd, None)
                print(found_pid)
                if found_pid == pid:
                    hwnds.append (hwnd)
                return True
        hwnds = []
        print(callback)
        self.u32.EnumWindows(callback, hwnds)
        return hwnds


def main():
    process_exec = "ac_client.exe"
    # process handle setup
    rwm = pymem.ReadWriteMemory()
    process = rwm.get_process_by_name(process_exec)
    if process == None:
        print("Could not find: ", process_exec)
        return
    process.open()
    print("PID: ", process.pid, ", name: ", process.name)

    esp = overlay(process.handle)

    hwnds = esp.get_hwnds_for_pid(process.pid)
    print(hwnds)

    window_rect = wintypes.RECT()
    window_found = esp.get_window_rect(process.handle, window_rect)
    if window_found == 0:
        error_code = ctypes.GetLastError()
        print("Could not find window: ", error_code)
        # error_code 1400 = ERROR_INVALID_WINDOW_HANDLE
    print(window_rect)
    
if __name__ == "__main__":
    main()    
