# Python Security Log Analyzer

## Overview
This project simulates a real-world security task: analyzing login logs to detect suspicious activity.

## Features
- Detects failed login attempts
- Identifies unusual login times (outside working hours)
- Flags potential brute-force attacks
- Writes alerts to a separate file

## Technologies Used
- Python
- File handling
- String parsing
- Loops and conditionals

## Files used
- `log_analyzer.py` → main script
- `login_logs.txt` → input logs
- `alerts.txt` → detected alerts

## How to Run
```bash
python log_analyzer.py
