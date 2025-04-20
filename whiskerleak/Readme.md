# 🐾 WhiskerLeak – Credential Dumper & Privilege Escalation Framework

A Mimikatz-inspired credential dumping and privilege escalation toolkit written in Python.  
Built for educational labs, red team simulation, and CTF training purposes only.

## 🚨 What It Does

- Extracts credentials from memory (LSASS)
- Dumps local hashes (SAM)
- Basic Windows token impersonation

## 🔧 Requirements

- Windows OS
- Admin or SYSTEM privileges
- Python 3.x
- `pywin32`, `ctypes`, `psutil`

## 📁 Folder Structure

| File/Folder         | Description                                 |
|---------------------|---------------------------------------------|
| `main.py`           | Entry point with CLI menu                   |
| `modules/sekurlsa`  | Mimics `sekurlsa::logonpasswords`           |
| `modules/lsadump`   | Mimics `lsadump::sam`                       |
| `modules/tokens`    | Handles token listing and impersonation     |

## 🛑 Disclaimer

This project is for authorized security research, training, and education **only**.  
Do not use WhiskerLeak on any system you don't have explicit permission to test.

---

🐾 Stay stealthy. Stay curious.
