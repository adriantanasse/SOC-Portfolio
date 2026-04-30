Suspicious Outbound Traffic (Possible C2 / Data Exfiltration)
🎯 Scenario

A compromised machine (Ubuntu victim) starts making suspicious outbound connections to an external server (Kali attacker), simulating command-and-control (C2) or data exfiltration.

You will:

Simulate outbound traffic (attacker-controlled)
Detect it with Suricata + Wazuh
Investigate the alert
Block the attacker
Write an incident report

1. simulate malware
2. while true; do curl http://<kali-ip>:8080; sleep 5; done
