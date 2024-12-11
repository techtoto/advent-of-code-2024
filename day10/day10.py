#!/usr/bin/env python3

with open("./day10/day10-example.txt") as f:
    map = [[int(x) for x in line] for line in f.read().splitlines()]

score = 0

# assume a recangular map
def in_boundaries(x, y):
    return x in range(len(map[0])) and y in range(len(map))

# base is from day 4
# is only called on points where there is a 0
def search(x, y, trail_index=0):
    global score
    if in_boundaries(x, y):
        if map[y][x] == trail_index:
            if trail_index == 9:
                score += 1
                return
            else:
                if in_boundaries(x, y - 1):
                    search(x, y - 1, trail_index + 1) # top
                if in_boundaries(x + 1, y):
                    search(x + 1, y, trail_index + 1) # right
                if in_boundaries(x, y + 1):
                    search(x, y + 1, trail_index + 1) # bottom
                if in_boundaries(x - 1, y):
                    search(x - 1, y, trail_index + 1) # left

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 0:
            search(x, y)

print(score)