# Python UAC Bypasses & LSASS Dump Toolkit

## ⚠️ Legal & Ethical Notice
For educational and authorized use only. Do not run on systems you don't own or have permission to test.

## 💻 Requirements
- Windows 10/11 VM
- Python 3.8+
- `pip install pywin32 psutil comtypes pypykatz`

## 🔧 Usage
1. Run UAC bypass scripts from non-admin shell:
   ```bash
   python fodhelper_bypass.py
   python sdclt_bypass.py
   python icmlua_bypass.py
   ```
2. Once elevated, dump LSASS with:
   ```bash
   python lsass_comsvcs.py
   python lsass_dbghelp.py
   ```
3. Parse credentials:
   ```bash
   python parse_lsass.py
   ```

## 📁 Structure
- `uac_bypass/`: Registry + COM UAC bypass techniques
- `cred_dump/`: LSASS dumping & parsing

## 🧪 Works well with Part 1 (Foothold Payloads)
Use this repo after gaining initial access via macro, HTA, or ISO as described in Part 1 of the lab series.

## 🔗 Coming Next
- Part 3: Lateral Movement with SMB + WMI
- Part 4: Covert Persistence Techniques