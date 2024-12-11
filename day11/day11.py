#!/usr/bin/env python3

with open("./day11/day11-input.txt") as f:
    stones = f.read().replace("\n", "").split(" ")

for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            new_stones.append(stone[:len(stone)//2])
            new_stones.append(str(int(stone[len(stone)//2:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    print(f"Iteration {i + 1}: length {len(new_stones)}")
    stones = new_stones
