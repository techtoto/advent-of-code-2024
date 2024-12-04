#!/usr/bin/env python3

reports = []
safe_reports_1 = 0
safe_reports_2 = 0

with open("./day02/day02-input.txt") as f:
    reports = [[int(x) for x in line.split(" ")] for line in f.read().splitlines()]

def is_safe(report):
    sorted_ascending = report.copy()
    sorted_descending = report.copy()
    sorted_ascending.sort()
    sorted_descending.sort(reverse = True)

    if report != sorted_ascending and report != sorted_descending:
        return False

    safe = True
    for i in range(len(report) - 1):
        if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
            safe = False
            break
    return safe

for report in reports:
    if is_safe(report):
        safe_reports_1 += 1
    else:
        for i in range(len(report)):
            i_removed = report.copy()
            i_removed.pop(i)
            if is_safe(i_removed):
                safe_reports_2 += 1
                break

print(safe_reports_1)
print(safe_reports_1 + safe_reports_2)