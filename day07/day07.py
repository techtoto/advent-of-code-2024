#!/usr/bin/env python3
import re, numpy

with open("./day07/day07-input.txt") as f:
    lines = re.findall(r"(\d+):\s(.+)", f.read())

sum_1 = 0
sum_2 = 0

for line in lines:
    expected = int(line[0])
    numbers = [int(x) for x in line[1].split(" ")]
    
    # PART 1
    # every permutation of additions and multiplications: 2^(len(numbers) - 1)
    # n acts as a bitmask; 0b0 -> add, 0b1 -> multiply
    for n in range(1 << (len(numbers) - 1)):
        result = numbers[0]
        for i in range(1, len(numbers)):
            if ((n >> (i - 1)) & 1) == 1:
                result *= numbers[i]
            else:
                result += numbers[i]
        if result == expected:
            sum_1 += result
            break

    # PART 2
    # every permutation of additions, multiplications and concatenations: 3^(len(numbers) - 1)
    for n in range(3 ** (len(numbers) - 1)):
        result = numbers[0]
        n_base_3 = numpy.base_repr(n, 3).zfill(len(numbers) - 1)
        for i in range(1, len(numbers)):
            if n_base_3[i - 1] == '1':
                result *= numbers[i]
            elif n_base_3[i - 1] == '0':
                result += numbers[i]
            else:
                result = int(f"{result}{numbers[i]}")
        if result == expected:
            sum_2 += result
            break

print(sum_1)
print(sum_2)