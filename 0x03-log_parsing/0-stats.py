#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

def print_stats():
    """Prints the accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    line_count += 1
    parts = line.split()

    # Validate and parse the input line
    if len(parts) >= 7 and parts[-2].isdigit() and parts[-1].isdigit():
        file_size = int(parts[-1])
        status_code = parts[-2]

        # Update total file size
        total_size += file_size

        # Update status code count
        if status_code in status_codes:
            status_codes[status_code] += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final statistics
print_stats()
