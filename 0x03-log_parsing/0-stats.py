#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys
import signal
from collections import defaultdict

# Initialize variables for tracking metrics
total_file_size = 0
status_codes_count = defaultdict(int)
lines_processed = 0


def print_and_reset_stats():
    """
    Prints current statistics and resets line counter.
    Outputs the total file size and counts of each status code,
    then resets the lines_processed counter for the next batch.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        print(f"{status_code}: {status_codes_count[status_code]}")
    # Reset line counter for next batch of lines
    global lines_processed
    lines_processed = 0


def handle_interrupt(signum, frame):
    """
    Handles keyboard interruption by printing current stats.
    Captures SIGINT to output current statistics before exiting.
    """
    print_and_reset_stats()
    sys.exit(0)


# Register signal handler for graceful exit on CTRL+C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        lines_processed += 1

        # Parse log entry based on expected format
        try:
            _, _, _, method, status_code, file_size = line.rsplit(' ', 4)
            status_code = int(status_code)
            file_size = int(file_size.strip())

            # Update metrics
            total_file_size += file_size
            status_codes_count[str(status_code)] += 1

        except ValueError:
            # Skip lines that don't match expected format
            continue

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print_and_reset_stats()

except Exception as e:
    # Handle unexpected errors gracefully
    print(f"An error occurred: {e}")

finally:
    # Ensure final statistics are printed before script exits
    print_and_reset_stats()
