import re
from collections import Counter

log_file_path = "access.log"

log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).+?"\S+ \S+ \S+" (?P<status>\d{3})')

ip_counter = Counter()
status_counter = Counter()

with open(log_file_path, "r") as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            ip = match.group("ip")
            status = match.group("status")
            ip_counter[ip] += 1
            status_counter[status] += 1

print("Top 10 IP Addresses:")
for ip, count in ip_counter.most_common(10):
    print(f"{ip}: {count} requests")

print("\nHTTP Status Code Counts:")
for status, count in status_counter.items():
    print(f"{status}: {count} responses")
