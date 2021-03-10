from ctypes import *
from ctypes.wintypes import *

import win32process
import win32api
import win32ui
import win32event

from subprocess import check_output

def get_window_name(name):
    task = name + ".exe"
    process = check_output(["tasklist","/nh","/v","/fo","csv","/fi", "ImageName eq " + task], shell=True).decode("utf-8")
    name = process.split(",")[9].split("\"")[1]
    return name

# access memory access level
PROCESS_VM_READ =       0x0010     #dwDesiredAccess read level
PROCESS_VM_WRITE =      0x0020     #dwDesiredAccess write level
PROCESS_ALL_ACCESS =    0x1F0FFF   #dwDesiredAccess all level

window_name = get_window_name("notepad")
HWND = win32ui.FindWindow(None, window_name).GetSafeHwnd()
PROCESS_ID = win32process.GetWindowThreadProcessId(HWND)
print(PROCESS_ID)
PROCESS_HANDLE = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, 15424)
win32api.WaitForInputIdle(PROCESS_HANDLE, 10000)
FILE_PATH = win32event.GetProcessImageFileNameW(PROCESS_HANDLE)
print(FILE_PATH)
modules = win32process.EnumProcessModules(PROCESS_HANDLE)


#OpenProcess
#GetProcessImagefileNameW
#EnumProcessModules
#GetModuleFileNameEx
#GetModuleInformation


print(PROCESS_HANDLE)
print(modules)