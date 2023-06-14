#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys

file_size = 0
i = 0
sm_tally = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = i
            if tokens[-2] in sm_tally:
                sm_tally[tokens[-2]] += 1
                i += 1
            try:
                file_size += int(tokens[-1])
                if a == i:
                    i += 1
            except ValueError:
                if a == i:
                    continue

        if i % 10 == 0:
            print(f"File size: {file_size}")
            for key, value in sorted(sm_tally.items()):
                if value:
                    print(f"{key}: {value}")

    print(f"File size: {file_size}")

    for key, value in sorted(sm_tally.items()):
        if value:
            print(f"{key}: {value}")

except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for key, value in sorted(sm_tally.items()):
        if value:
            print(f"{key}: {value}")
