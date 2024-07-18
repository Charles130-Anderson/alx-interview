#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Initialize metrics variables
total_size = 0
status_codes = defaultdict(int)
line_count = 0


def print_stats_and_exit(signum, frame):
    """
    Prints current stats and exits gracefully.
    Handles SIGINT by printing statistics collected so far,
    then terminates the script execution.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")
    sys.exit(0)


# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, print_stats_and_exit)

for line in sys.stdin:
    # Increment line count for each input line
    line_count += 1

    # Split line into parts based on spaces
    parts = line.split()

    # Check if line format matches expected structure
    if len(parts) != 7:
        continue

    try:
        # Extract file size and status code from line parts
        file_size = int(parts[6])
        status_code = int(parts[5])
    except ValueError:
        continue  # Skip lines with invalid numbers

    # Update total file size and status codes count
    total_size += file_size
    status_codes[status_code] += 1

    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_stats_and_exit(None, None)

# Print final statistics if script completes normally
print_stats_and_exit(None, None)
