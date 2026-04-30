# -------------------------------
# Security Log Analyzer (Advanced)
# -------------------------------

# Open and read the log file
with open("login_logs.txt", "r") as file:
    logs = file.read()

# Split logs into individual lines
lines = logs.split("\n")

# Track failed login attempts per user (for brute-force detection)
failed_attempts = {}

# Store structured alerts
alerts = []

# Define a simple IP blacklist (can be expanded or externalized)
blacklist = ["8.8.8.8"]

# Function to assign severity based on risk score
def get_severity(score):
    if score >= 8:
        return "CRITICAL"
    elif score >= 5:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"

# Process each log entry (skip header)
for line in lines[1:]:
    if not line:
        continue

    parts = line.split(",")
    username = parts[0]
    ip = parts[1]
    time = parts[2]
    status = parts[3]

    hour = int(time.split(":")[0])

    # Initialize risk score for this event
    risk_score = 0
    reasons = []

    # -------------------------------
    # Detection Rules
    # -------------------------------

    # 1. Failed login attempt
    if status == "failed":
        risk_score += 2
        reasons.append("Failed login")

        # Track failed attempts per user
        failed_attempts[username] = failed_attempts.get(username, 0) + 1

    # 2. Unusual login time
    if hour < 6 or hour > 22:
        risk_score += 2
        reasons.append("Login outside working hours")

    # 3. Blacklisted IP
    if ip in blacklist:
        risk_score += 5
        reasons.append("Blacklisted IP address")

    # 4. Brute-force detection (multiple failures)
    if failed_attempts.get(username, 0) > 3:
        risk_score += 5
        reasons.append("Multiple failed attempts (possible brute-force)")

    # -------------------------------
    # Create Alert if Risk Detected
    # -------------------------------

    if risk_score > 0:
        severity = get_severity(risk_score)

        alert = {
            "username": username,
            "ip": ip,
            "time": time,
            "risk_score": risk_score,
            "severity": severity,
            "reasons": reasons
        }

        alerts.append(alert)

# -------------------------------
# Output Results
# -------------------------------

# Print alerts in a readable format
for alert in alerts:
    print(f"[{alert['severity']}] User: {alert['username']} | IP: {alert['ip']} | Time: {alert['time']}")
    print(f"  Risk Score: {alert['risk_score']}")
    print(f"  Reasons: {', '.join(alert['reasons'])}")
    print("-" * 50)

# Save alerts to a file
with open("alerts.txt", "w") as file:
    for alert in alerts:
        file.write(f"{alert}\n")
