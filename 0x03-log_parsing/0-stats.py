#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

# Initialize variables
line_count = 0
total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

def print_metrics():
    """Prints the computed metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


try:
    for line in sys.stdin:
        # Split the line to extract components
        parts = line.split()
        if len(parts) > 6:
            # Extract status code and file size from the line
            status_code = parts[-2]
            file_size = parts[-1]
            # Update metrics if the status code is valid
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            total_file_size += int(file_size)
            line_count += 1
            # Print metrics every 10 lines
            if line_count == 10:
                print_metrics()
                line_count = 0

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_metrics()
    raise

except Exception as e:
    # Handle other exceptions
    print(f"Error: {e}")

finally:
    # Ensure metrics are printed at the end
    print_metrics()
