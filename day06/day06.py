#!/usr/bin/env python3

with open("./day06/day06-input.txt") as f:
    input_map = [list(x) for x in f.read().split("\n")]

x = 0
y = 0
step_count = 1
dir_cycle = [[0, -1], [1, 0], [0, 1], [-1, 0]]
dir_cycle_i = 0

# search guard
done = False
for current_y in range(len(input_map)):
    if not done:
        for current_x in range(len(input_map[y])):
            if input_map[current_y][current_x] == "^": # assumption: guard starts facing up
                x = current_x
                y = current_y
                done = True
                break

def in_boundaries(x, y):
    return x in range(len(input_map[0])) and y in range(len(input_map))

while True:
    x_dir = dir_cycle[dir_cycle_i % 4][0]
    y_dir = dir_cycle[dir_cycle_i % 4][1]

    if in_boundaries(x + x_dir, y + y_dir):
        if input_map[y + y_dir][x + x_dir] == "#":
            dir_cycle_i += 1
        else:
            if input_map[y][x] != "X":
                input_map[y][x] = "X"
                step_count += 1
            x += x_dir
            y += y_dir
    else:
        break

print(step_count)