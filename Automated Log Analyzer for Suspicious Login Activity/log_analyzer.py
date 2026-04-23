# Read the log file (IPs in our case)
with open("login_logs.txt", "r") as file:
    logs = file.read()

# Parse the logs
lines = logs.split("\n")

failed_count = 0
alerts = []

# Extract useful data
for line in lines[1:]:
    if line:
        parts = line.split(",")
        username = parts[0]
        ip = parts[1]
        time = parts[2]
        status = parts[3]

        hour = int(time.split(":")[0])

        # Detect suspicious activity
        ## Failed login tracking
        
        if status == "failed":
            failed_count += 1
            # Store flagged results
            alerts.append(line)
            
        ##  Detect unusual hours
        if hour < 6 or hour > 22:
            # Store flagged results
            alerts.append("Unusual time: " + line)

# Detect brute-force attacks
if failed_count > 3:
    print("Possible brute-force attack detected")

# Write all alerts to a file – alerts.txt
with open("alerts.txt", "w") as file:
    for alert in alerts:
        file.write(alert + "\n")
