# 1) Create the script on the server

cat > /tmp/triage.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
OUTDIR="/tmp/triage-$(hostname)-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$OUTDIR"
echo "Collecting triage data to $OUTDIR"

# Basic system info
uname -a > "$OUTDIR/uname.txt"
cat /etc/os-release > "$OUTDIR/os-release.txt"
uptime > "$OUTDIR/uptime.txt"
whoami > "$OUTDIR/whoami.txt"
id > "$OUTDIR/id.txt"

# Network & sockets
ip -br addr > "$OUTDIR/ip-addr.txt" 2>&1 || ip addr > "$OUTDIR/ip-addr-full.txt" 2>&1
ss -tnap > "$OUTDIR/ss-tcp.txt" 2>&1 || netstat -tnap > "$OUTDIR/netstat.txt" 2>&1
ip route show > "$OUTDIR/ip-route.txt"
ip -s link > "$OUTDIR/ip-link.txt"

# SSHD & fail2ban status
sudo systemctl status ssh -l > "$OUTDIR/sshd-systemctl.txt" 2>&1 || true
sudo systemctl status sshd -l > "$OUTDIR/sshd-systemctl-alt.txt" 2>&1 || true
sudo systemctl status fail2ban -l > "$OUTDIR/fail2ban-systemctl.txt" 2>&1 || true
sudo fail2ban-client status > "$OUTDIR/fail2ban-client-status.txt" 2>&1 || true
# Dump each jail list if fail2ban available
if command -v fail2ban-client >/dev/null 2>&1; then
  for j in $(fail2ban-client status | sed -n 's/.*Jail list: *//p' | tr ',' ' '); do
    [ -z "$j" ] && continue
    fail2ban-client status "$j" > "$OUTDIR/fail2ban-jail-${j}.txt" 2>&1 || true
  done
fi

# Logs: auth + recent journalctl for sshd/fail2ban
if [ -f /var/log/auth.log ]; then
  tail -n 10000 /var/log/auth.log > "$OUTDIR/auth.log.tail" 2>&1 || true
fi
if [ -f /var/log/secure ]; then
  tail -n 10000 /var/log/secure > "$OUTDIR/secure.log.tail" 2>&1 || true
fi
journalctl -u ssh -n 200 --no-pager > "$OUTDIR/journal-ssh.txt" 2>&1 || journalctl -u sshd -n 200 --no-pager > "$OUTDIR/journal-sshd.txt" 2>&1 || true
journalctl -u fail2ban -n 200 --no-pager > "$OUTDIR/journal-fail2ban.txt" 2>&1 || true

# last/who/ps
last -n 50 > "$OUTDIR/last.txt" 2>&1 || true
who -a > "$OUTDIR/who.txt" 2>&1 || true
ps aux --sort=-%mem | head -n 200 > "$OUTDIR/ps-aux-top.txt" 2>&1 || true

# iptables / nft
if command -v iptables-save >/dev/null 2>&1; then
  sudo iptables-save > "$OUTDIR/iptables-save.txt" 2>&1 || true
fi
if command -v nft >/dev/null 2>&1; then
  sudo nft list ruleset > "$OUTDIR/nft-ruleset.txt" 2>&1 || true
fi

# Show current conntrack counts (if available)
if command -v conntrack >/dev/null 2>&1; then
  sudo conntrack -L | head -n 2000 > "$OUTDIR/conntrack.txt" 2>&1 || true
fi

# Recent kernel messages
dmesg | tail -n 200 > "$OUTDIR/dmesg-tail.txt" 2>&1 || true

# Optional: a short live tcpdump to capture port 22 traffic for 5 seconds (uncomment if you want)
# Requires tcpdump installed and running as root; will capture up to 5s
if command -v tcpdump >/dev/null 2>&1; then
  echo "Running quick tcpdump (5s) to capture port 22 traffic..."
  sudo timeout 5 tcpdump -i any -s 0 -w "$OUTDIR/tcpdump-ssh.pcap" port 22 2> "$OUTDIR/tcpdump-ssh.log" || true
fi

# summarize sizes and package
tar -czf "${OUTDIR}.tar.gz" -C "$(dirname "$OUTDIR")" "$(basename "$OUTDIR")"
echo "Triage bundle created: ${OUTDIR}.tar.gz"
ls -lh "${OUTDIR}.tar.gz"
EOF

chmod +x /tmp/triage.sh


2) Copy the file to your host

scp root@<VULTR_IP>:/tmp/triage-myhost-20251025-235010.tar.gz .
