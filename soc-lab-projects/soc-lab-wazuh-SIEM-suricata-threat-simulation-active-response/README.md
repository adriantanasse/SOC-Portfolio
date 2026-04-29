# SOC Lab Project – Wazuh SIEM + Suricata + Threat Simulation + Active Response

## Overview

Designed and implemented a **multi-host SOC lab environment** to simulate real-world cyber attacks and defensive monitoring using **SIEM, IDS, and automated responses**.

## Lab Architecture
#### Wazuh Manager installed on macOS host + 3 Virtual Machines (VMs):

```
macOS → Wazuh Manager
Ubuntu → Victim system
Windows → Victim system
Kali Linux → Attacker machine
```

**All VMs onboarded as agents into Wazuh.**
**Integrated Suricata for network-based intrusion detection.**


## Environment Setup
Configured Wazuh Manager ↔ Agent secure communication

**Enabled centralized log collection from:**
- SSH logs (Linux)
- System and authentication logs
- Custom log sources
- Configured Suricata to feed alerts into Wazuh for correlation


## Detection Engineering
**Developed custom detection rules:**

```
5760 → SSH authentication failures
5763 → SSH brute-force detection using:
```

```
<frequency> (attack threshold)
<timeframe> (time window)
<same_source_ip> (attacker correlation)
```

**Tuned alert levels and rule logic to reduce noise and improve detection accuracy**


## Active Response (Automated Defense)
Implemented automated response using:
`firewall-drop script`

**Configured:**
- IP blocking via iptables
- Timeout-based automatic unblocking

**Resolved issues with:**
✓ Command compatibility (firewall-drop vs built-in scripts)

✓ Agent vs manager execution context

✓ Configuration errors causing Wazuh service failures


## Threat Simulation (Red Teaming)

Simulated attacks from Kali Linux against victim machines:

- SSH Brute Force Attack
- Used Hydra, nmap
- Generated high-frequency failed login attempts

**Successfully triggered:**
- Wazuh alerts
- Correlation rule (5763)
- Active response (attacker IP blocked)


## Malware Detection Testing
Downloaded and tested **EICAR Test File**

**Verified:**
✓ Detection by security controls

✓ Alert generation within Wazuh

✓ Automatic removal behavior


## Troubleshooting & Debugging
**Diagnosed and fixed:**
✓ Wazuh API failures (ERROR3099 – not ready)

✓ Agent-to-manager SSL connection issues

✓ Active response not triggering on agents

✓ XML rule syntax errors causing service crashes

**Used tools like:**
- xmllint for validation
- Wazuh logs (ossec.log, active-responses.log)
- Manual testing of firewall rules (iptables)


## Key Outcomes
✓ Built a fully functional **SOC detection + response pipeline**

✓ Successfully **detected and mitigated** simulated attacks in real time

✓ Automated blocking of malicious IPs based on **SIEM correlation rules**

✓ Integrated **host-based** (HIDS) and **network-based** (NIDS) detection (Wazuh + Suricata)


## Skills Demonstrated
✓ SIEM configuration & management (**Wazuh**)

✓ IDS integration (**Suricata**)

✓ Linux & Windows log analysis

✓ Threat detection & rule creation

✓ Incident response automation

✓ Network security fundamentals

✓ Red team simulation (Hydra, nmap)

✓ Troubleshooting distributed systems

## Preview

Built a SOC lab using Wazuh SIEM on macOS with Ubuntu, Windows, and Kali Linux VMs. 
Configured agents and integrated Suricata IDS for network monitoring. 
Simulated SSH brute-force attacks using Hydra and developed custom detection rules with automated IP blocking via active response. 
Troubleshot SIEM, API, and agent communication issues to ensure a fully operational detection and response pipeline.
