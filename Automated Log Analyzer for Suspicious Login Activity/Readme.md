# 🔐 Security Log Analyzer (Python)

## 📖 Overview

This project simulates a real-world **Security Operations Center (SOC)** task: analyzing login logs to detect suspicious activity and potential security threats.

The script processes raw log data, applies detection rules, assigns **risk scores**, and classifies events by **severity level**—similar to how modern SIEM tools operate.

---

## Key Features

* Detects failed login attempts
* Identifies logins outside normal working hours
* Flags activity from blacklisted IP addresses
* Detects potential brute-force attacks
* Assigns **risk scores** to each event
* Classifies alerts as **LOW / MEDIUM / HIGH / CRITICAL**
* Outputs structured alerts to a file for investigation

---

## Detection Logic

Each log entry is evaluated using multiple security rules:

| Detection Rule                         | Risk Score |
| -------------------------------------- | ---------- |
| Failed login attempt                   | +2         |
| Login outside working hours            | +2         |
| Blacklisted IP address                 | +5         |
| Multiple failed attempts (brute-force) | +5         |

👉 Total score determines severity:

* **LOW** (1–2)
* **MEDIUM** (3–4)
* **HIGH** (5–7)
* **CRITICAL** (8+)

---

## Project Structure

```
.
├── log_analyzer_adv.py     # Main analysis script
├── login_logs.txt      # Sample log file
├── alerts.txt          # Output alerts
└── README.md           # Project documentation
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/security-log-analyzer.git
cd security-log-analyzer
```

2. Run the script:

```bash
python log_analyzer_adv.py
```

3. View results:

* Console output (real-time alerts)
* `alerts.txt` file (saved alerts)

---

## Example Output

```
[HIGH] User: alex | IP: 192.168.1.10 | Time: 23:50:33
Risk Score: 7
Reasons: Failed login, Login outside working hours
--------------------------------------------------
```

---

## Technologies Used

* Python
* File handling (`open`, `read`, `write`)
* String parsing
* Loops & conditionals
* Basic threat detection logic

---

## Skills Demonstrated

* Log parsing and data processing
* Security event detection
* Risk scoring and prioritization
* Automation of repetitive analysis tasks
* Writing clean, structured Python code

---

## Real-World Relevance

This project mirrors how security analysts:

* Investigate login activity
* Detect suspicious behavior
* Prioritize threats based on severity
* Generate actionable alerts

---

## Future Improvements

* Integrate threat intelligence APIs (IP reputation)
* Export alerts in JSON format (SIEM-style)
* Add visualization/dashboard
* Implement real-time log monitoring

---

## Author

Adrian Tanase

Built as part of my cybersecurity learning journey focused on **security automation and detection engineering**.

---
