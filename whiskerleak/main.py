"""
WhiskerLeak 🐾 - Mimikatz-Inspired Credential Dumper (Educational Use Only)

🎯 What It Does:
- Modular framework for dumping credentials from memory
- Handles token abuse and simple hash extraction

🧪 Requirements:
- Windows OS
- Run as Administrator
- Python 3.x
- Modules: pywin32, ctypes, psutil (to be added)

⚠️ WARNING:
This tool is for educational and authorized use only!
Do not run on machines you don't own or have permission to test.
"""

from modules import sekurlsa, lsadump, tokens

def banner():
    print("""
╦ ╦╦╔╗╔╔═╗╔═╗╔═╗╦═╗  🐾 WhiskerLeak 🐾
║║║║║║║╠═╣║ ╦║╣ ╠╦╝  Credential Dumper & PrivEsc Toolkit
╚╩╝╩╝╚╝╩ ╩╚═╝╚═╝╩╚═  by @chouaib-k | Edu Use Only
""")

def menu():
    print("""
[1] Dump Credentials (sekurlsa::logonpasswords)
[2] Dump SAM Hashes (lsadump::sam)
[3] Token Abuse (token::whoami / elevate)
[0] Exit
""")

def main():
    banner()
    while True:
        menu()
        choice = input("Whisker > ").strip()

        if choice == "1":
            sekurlsa.run()
        elif choice == "2":
            lsadump.run()
        elif choice == "3":
            tokens.run()
        elif choice == "0":
            print("🐾 See you later, sneaky cat.")
            break
        else:
            print("[!] Invalid option. Try again.")

if __name__ == "__main__":
    main()
