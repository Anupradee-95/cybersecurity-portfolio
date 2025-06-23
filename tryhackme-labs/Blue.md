# TryHackMe - Blue Room

## Objective
Exploit SMB vulnerability (EternalBlue) on a vulnerable Windows machine.

## Tools Used
- Nmap
- Metasploit
- smbclient

## Exploitation Steps
1. Scanned ports: `nmap -sC -sV [IP]`
2. Found open port 445 (SMB)
3. Used `exploit/windows/smb/ms17_010_eternalblue` in Metasploit
4. Gained remote shell access

## Lessons Learned
- Importance of patching legacy services
- Basics of Windows post-exploitation
