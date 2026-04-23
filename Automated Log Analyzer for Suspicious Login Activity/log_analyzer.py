# Open the log file in read mode and load all contents into a string
with open("login_logs.txt", "r") as file:
    logs = file.read()

# Parse the logs – Split the log file into individual lines for processing
lines = logs.split("\n")

# Initialize a counter for failed login attempts
failed_count = 0

# List to store any suspicious activity we detect
alerts = []

# Loop through each log entry, skipping the header row
for line in lines[1:]:
    if line: # Make sure the line is not empty
        # Split the log entry into its components
        parts = line.split(",")
        username = parts[0]
        ip = parts[1]
        time = parts[2]
        status = parts[3]

        # Extract the hour from the timestamp for time-based analysis
        hour = int(time.split(":")[0])

        # Detect suspicious activity
        # Check for failed login attempts
        if status == "failed":
            failed_count += 1
            alerts.append(line) # Store flagged results
            
        # Check for logins outside normal working hours (before 9 AM or after 10 PM)
        if hour < 9 or hour > 22:
            # Store flagged results
            alerts.append("Unusual time: " + line)

# If there are too many failed attempts, flag a potential brute-force attack
if failed_count > 3:
    print("Possible brute-force attack detected")

# Write all detected alerts to a separate file for further investigation
with open("alerts.txt", "w") as file:
    for alert in alerts:
        file.write(alert + "\n")
