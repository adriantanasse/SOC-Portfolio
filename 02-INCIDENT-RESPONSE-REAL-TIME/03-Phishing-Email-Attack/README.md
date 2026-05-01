# Phishing Detection Lab with Wazuh (Behavior-Based Detection)

## 📌 Overview

This project simulates a **real-world Security Operations Center (SOC) investigation**, demonstrating **detection** engineering, **threat analysis**, and **incident response** in the context of a **phishing attack**. The attack was conducted using the Social-Engineer Toolkit (SET), where a malicious actor successfully harvested user credentials through a spoofed login portal.

The lab environment integrates **multiple security tools and techniques**, including:

- A phishing page generated with the **Social-Engineer Toolkit (SET)**
- A **Python-based credential harvesting server** used by the attacker
- **Custom Wazuh detection rules** focused on behavior-based threat identification
- Network monitoring and alerting **powered by Suricata**

Rather than relying solely on signature-based detection, this project emphasizes the identification of attacker behavior patterns, such as suspicious HTTP activity, credential submission events, and abnormal server responses, to improve detection accuracy and incident visibility.

## Attack Scenario
1. A victim accesses a **fake Nassau County login page**
2. The attacker runs a **Python HTTP server** to **collect** credentials
3. Victim **submits** login details
4. Credentials are stored in an **XML file**
5. Wazuh detects:
    - Suspicious Python HTTP server
    - Credential submission via POST requests
    - Correlates events → flags phishing attack
---

| Component      | Role                                           |
| -------------- | ---------------------------------------------- |
| Kali Linux     | Attacker machine (SET + credential harvesting) |
| Ubuntu + Wazuh | SIEM + detection                               |
| Suricata       | Network IDS                                    |
| Victim Browser | Sends credentials                              |


### Step 1: Phishing Page (SET)

The phishing page was created using:

👉 Social-Engineer Toolkit (SET) → Credential Harvester Attack

- Cloned login page (Nassau County portal)
- Hosted locally on attacker machine
- Delivered over HTTP

Code: `sudo setoolkit`

Typical flow:
```
Social-Engineering Attacks
→ Website Attack Vectors
→ Credential Harvester Attack Method
→ Site Cloner
```

Hosted page: `http://192.168.69.2`

![Phishing Login Page](images/phishing-website.png)

### Step 2: Credential Harvesting Server

SET automatically spins up a Python-based web server that captures credentials.

**Captured fields:**

- Email
- Password
- Form parameters

![Collecting Credentials](images/collecting-credentials.png)

### Step 3: Stored Credentials
Captured credentials are saved in XML format:
```
<param>MainLoginForm[email]=example@email.com</param>
<param>MainLoginForm[password]=password123</param>
```
![Collected Credentials XML](images/collected-credentials-xml.png)

### Step 4: Wazuh Detection Rules

Custom rules were created to detect attack behavior.

**1. Detect Python HTTP Server (SET)**

```
<rule id="100001" level="6">
  <match>BaseHTTP</match>
  <description>Suspicious Python-based web server detected (SET)</description>
</rule>
```

**2. Detect Credential Submission**

```   
<rule id="100002" level="10">
  <match>POST</match>
  <description>HTTP POST request detected (possible credential submission)</description>
</rule>
```

**3. Correlate Attack (Phishing Confirmation)**

```
<rule id="100003" level="12">
  <if_sid>100001</if_sid>
  <if_sid>100002</if_sid>
  <description>Confirmed phishing attack (SET credential harvester)</description>
</rule>
```

### Step 5: Wazuh Alerts

Wazuh generates alerts based on behavior:

- Python BaseHTTP server detected (SET)
- HTTP traffic spikes
- POST credential submissions
- Correlated phishing alert

![Wazuh Alerts](images/wazuh-alerts.png)

![Wazuh Alerts Detailed](images/wazuh-alerts-2.png)


## Indicators of Compromise (IOCs)

Wazuh + Suricata logs reveal:

- Attacker IP: `192.168.69.2`
- Port: `80`
- Protocol: `HTTP`
- Signature/Server type: `Python BaseHTTP (SET)`
- Behavior:
    - Multiple POST requests
    - Credential submission patterns

***This confirms the phishing infrastructure.***

**Detection Logic Summary**

| Behavior              | Detection Method   |
| --------------------- | ------------------ |
| SET phishing server   | BaseHTTP signature |
| Credential submission | HTTP POST          |
| Attack confirmation   | Rule correlation   |

## Response Actions
- Identified malicious server IP
- Confirmed credential compromise
- Correlated alerts to validate attack
- Simulated containment within lab

## Recommendations
**Detection Improvements**
Expand rules for:
- Suspicious web servers
- Credential harvesting patterns
- Add geo/IP anomaly detection

**Prevention**
- Enforce HTTPS-only policies
- Implement phishing awareness training
- Deploy email filtering & sandboxing

**Monitoring**
Alert on:
- High POST request frequency
- Unknown web servers in internal network
