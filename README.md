## SOC Analyst Portfolio – Detection, Investigation & Threat Analysis

### 📌 Overview

This repository showcases **hands-on Security Operations Center (SOC) projects** focused on threat detection, incident investigation, and behavioral analysis.

The goal of this portfolio is to demonstrate **practical, job-ready skills** in:

- Threat detection & alert triage
- Network traffic analysis (PCAP)
- Detection engineering (Wazuh rules)
- Incident response & investigation workflows
- Adversary simulation & attack analysis

All projects are designed to **simulate real-world attack scenarios**, moving beyond theory into **practical SOC operations**.

⚙️ **Tools & Technologies**

- SIEM: **Wazuh**
- Network IDS: **Suricata**
- Traffic Analysis: **Wireshark**, **tcpdump**
- Attack Simulation: **Social-Engineer Toolkit (SET)**, **Kali Linux**
- Log Analysis: **Linux CLI**, **JSON logs**
- Scripting: **Python** (basic automation & analysis)

📂 **Repository Structure**
```
01-INCIDENT-SOC-ANALYSIS/
│
├── 01-SSH-Brute-Force-Detection
├── 02-DDoS-Traffic-Flood-Detection
└── 03-Phishing-Email-Attack

02-MALWARE-PCAP-ANALYSIS/
│
├── 01-IcedID-PCAP-Analysis
├── 02-Netsupport-RAT-PCAP-Analysis
└── 03-STRRAT-PCAP-Analysis

03-SCRIPTS/

README.md

```

🔍 **Project Highlights**
- Incident-Based SOC Investigations

**Realistic attack simulations** with full investigation workflows:

🔐 **SSH Brute Force Detection**
- Identified repeated failed login attempts
- Correlated authentication logs
- Detected attacker IP patterns
- Created alerting logic for brute-force behavior

🌐 **DDoS Traffic Flood Detection**
- Analyzed abnormal traffic spikes
- Detected high request frequency patterns
- Tuned detection thresholds in Wazuh
- Investigated network-level indicators
  
🎣 **Phishing Attack Investigation**
- Simulated phishing attack using SET (Social-Engineer Toolkit)
- Captured credentials via a fake login portal
- Detected malicious HTTP traffic using Suricata
- Built custom behavior-based Wazuh rules:
- Suspicious Python HTTP server detection
- Credential submission (POST request) detection
- Correlation rule confirming phishing activity
  
🦠 **Malware PCAP Analysis**

Deep packet-level investigations of real malware traffic:

**IcedID Analysis**
- Identified C2 communication patterns
- Extracted indicators of compromise (IOCs)
- Analyzed HTTP/HTTPS beaconing behavior

**Netsupport RAT Analysis**
- Detected remote access activity
- Identified suspicious connections and ports
- Tracked attacker communication flow

**STRRAT Analysis**
- Investigated malicious traffic signatures
- Identified payload delivery mechanisms
- Mapped infection behavior

**Each project follows a structured SOC workflow:**
1. Alert Triggered
2. Initial Triage
3. Log & Traffic Analysis
4. Threat Identification
5. Correlation of Events
6. Conclusion & Impact Assessment

**Contact**

If you're hiring for a SOC Analyst or Junior Cybersecurity role, feel free to reach out.
