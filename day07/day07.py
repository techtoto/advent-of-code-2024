#!/usr/bin/env python3
import re

with open("./day07/day07-input.txt") as f:
    lines = re.findall(r"(\d+):\s(.+)", f.read())

current_sum = 0

for line in lines:
    expected = int(line[0])
    numbers = [int(x) for x in line[1].split(" ")]
    
    # n acts as a bitmask; 0b0 -> add, 0b1 -> multiply
    for n in range(1 << (len(numbers) - 1)): # every permutation of additions and multiplications: 2^(len(numbers) - 1)
        result = numbers[0]
        for i in range(1, len(numbers)):
            if ((n >> (i - 1)) & 1) == 1:
                result *= numbers[i]
            else:
                result += numbers[i]
        if result == expected:
            current_sum += result
            break

print(current_sum)