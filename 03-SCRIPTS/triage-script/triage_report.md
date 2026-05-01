# SOC Triage Exercise

**Author:** Adrian Tanase
**Date:** 2025-10-25  

**Environment:** Local lab (MacOSx target VM (Vagrant) at `10.0.0.5` — NAT/host-only).  
**Tools used:** tcpdump, Wireshark, tshark, Splunk Free, triage-script.sh

**Goal:** capture network traffic, produce /var/log evidence for failed logins, inspect Windows event logs, ingest Linux logs into a local Splunk, and produce a 1-page triage note.

**Pen-test Required Tasks:**
1. Create an Ubuntu VM (Vagrant) for a target host.
2. (Optional) Bring up a Windows evaluation VM (for event logs).
3. Use Wireshark and tshark to capture traffic on the host-only network.
4. Generate SSH failed logins from an attacker VM (or Mac host).
5. Run triage script on target Ubuntu to collect logs & artifacts.
6. Install Splunk (local) and ingest `/var/log/auth.log` to make a basic detection rule for repeated SSH failures.


---

## Summary
At 2025-10-25 20:33:12 UTC, the test target observed a burst of failed SSH authentication attempts from a remote host. Network captures show repeated TCP connections to port 22. Host logs contain repeated `Failed password` events. No successful authentication observed.

## Attacker
    Mac:sec-porto adriantanase$ TARGET=10.0.0.5; for i in {1..25}; do ssh -o ConnectTimeout=2 -o BatchMode=yes invaliduser@"$TARGET" 'echo hello' 2>/dev/null || true; done


<img width="796" height="471" alt="Group 3" src="https://github.com/user-attachments/assets/9a972a23-596d-408a-9069-bc372351810c" />

(If **pentest-user** will cause SSH to hang waiting for a password, add -o BatchMode=yes so ssh fails fast instead of prompting)

# Auth.log Check

    # show all auth events for that IP (newest last)
    sudo tail -n 50 /var/log/auth.log
    sudo grep "Failed password" /var/log/auth.log | tail -n 50
    sudo grep "10.0.0.1" /var/log/auth.log -n | tail -n 50
    
    # specifically show accepted logins from that IP
    sudo grep "Accepted" /var/log/auth.log | grep "10.0.0.1" -n

    # count failed password attempts from that IP
    sudo grep "Failed password" /var/log/auth.log | grep "10.0.0.1" | wc -l

    # who is/was logged in around that time
    who; sudo ss -tnp | grep ':22'

<img width="766" height="467" alt="Group 5" src="https://github.com/user-attachments/assets/eb632051-b49c-4d29-8cb8-969ecbb07f04" />



## Evidence (sanitized excerpts)
    **/var/log/auth.log** (excerpt, IPs anonymized):
    Oct 25 20:33:26 vultr sshd[2060]: Failed password for root from `10.0.0.5` port 42010 ssh2
    Oct 25 20:39:30 vultr sshd[2060]: Failed password for root from `10.0.0.5` port 42010 ssh2
    Oct 25 20:39:32 vultr sshd[2060]: Failed password for root from `10.0.0.5` port 42010 ssh2
    Oct 25 20:39:36 vultr sshd[2084]: Failed password for root from `10.0.0.5` port 14931 ssh2
    Oct 25 20:39:40 vultr sshd[2084]: Failed password for root from `10.0.0.5` port 14931 ssh2
    Oct 25 20:39:44 vultr sshd[2084]: Failed password for root from `10.0.0.5` port 14931 ssh2
    Oct 25 20:39:48 vultr sshd[2150]: Failed password for root from `10.0.0.5` port 20518 ssh2
    Oct 25 20:39:52 vultr sshd[2150]: Failed password for root from `10.0.0.5` port 20518 ssh2
    Oct 25 20:39:56 vultr sshd[2150]: Failed password for root from `10.0.0.5` port 20518 ssh2
    Oct 25 20:41:45 vultr sudo:     root : TTY=pts/0 ; PWD=/root/seclabs ; USER=root ; COMMAND=/usr/bin/grep Failed password /var/log/auth.log
    ...


## Run triage-script (triage.sh) (see the files in artifacts)

<img width="705" height="438" alt="Screenshot 2025-10-26 at 12 31 19 AM" src="https://github.com/user-attachments/assets/1d462fc9-c56a-4450-8f10-390008fcdffe" />

## IOCs (synthetic)
- Attacker IP: `10.0.0.5` (RFC1918 used for lab)  
- Attempted usernames: `pentest-user`

## Actions taken / recommended containment
1. Block source IP (`10.0.0.5`) at perimeter or host firewall.  
2. Confirm no successful logins; rotate credentials for any affected accounts.  
3. Preserve evidence: collected triage archive `triage-20251025-1430.tar.gz` (hash: `SHA256: <redacted>`) — archived offline.  
4. Tune detection: create SIEM rule to alert on >5 failed SSH attempts per 5 minutes (example Splunk query in `tshark-filters.txt`).  
5. If public keys were used anywhere, rotate keys and review authorized_keys.



## Notes on data
All logs and screenshots are sanitized to remove real IPs and any sensitive identifiers. This repository contains no customer data or private keys.
