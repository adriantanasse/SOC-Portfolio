with open("login_logs.txt", "r") as file:
    logs = file.read()

lines = logs.split("\n")

failed_count = 0
alerts = []

for line in lines[1:]:
    if line:
        parts = line.split(",")
        username = parts[0]
        ip = parts[1]
        time = parts[2]
        status = parts[3]

        hour = int(time.split(":")[0])

        if status == "failed":
            failed_count += 1
            alerts.append(line)

        if hour < 6 or hour > 22:
            alerts.append("Unusual time: " + line)

if failed_count > 3:
    print("Possible brute-force attack detected")

with open("alerts.txt", "w") as file:
    for alert in alerts:
        file.write(alert + "\n")
