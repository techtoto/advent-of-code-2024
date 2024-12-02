#!/usr/bin/env python3

reports = []
safe_reports = 0

with open("./day02/day02-input.txt") as f:
    reports = [[int(x) for x in line.split(" ")] for line in f.read().splitlines()]

for report in reports:
    sorted_ascending = report.copy()
    sorted_descending = report.copy()
    sorted_ascending.sort()
    sorted_descending.sort(reverse = True)

    if report != sorted_ascending and report != sorted_descending:
        continue

    safe = True
    for i in range(len(report) - 1):
        if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
            safe = False
            break
    
    if safe:
        safe_reports += 1

print(safe_reports)
