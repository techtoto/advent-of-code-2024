#!/usr/bin/env python3
import re

with open("./day03/day03-input.txt") as f:
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", f.read()) # https://regex101.com/r/UoZaQW/1

sum1 = 0
sum2 = 0
mul_enabled = True

for mul in muls:
    if mul[0] != "" and mul[1] != "":
        sum1 += int(mul[0]) * int(mul[1])

    if mul[2] == "do()":
        mul_enabled = True
    elif mul[3] == "don't()":
        mul_enabled = False
    elif mul_enabled:
        sum2 += int(mul[0]) * int(mul[1])


print(sum1)
print(sum2)
