#!/usr/bin/env python3

xmas_count = 0
x_mas_count = 0

with open("./day04/day04-input.txt") as f:
    lines = f.read().split("\n") # lines[y][x]

def in_boundaries(x, y):
    return x in range(len(lines[y])) and y in range(len(lines))

def search(x, y, x_dir, y_dir, xmas_index=1):
    global xmas_count
    if in_boundaries(x + x_dir, y + y_dir):
        if lines[y + y_dir][x + x_dir] == "XMAS"[xmas_index]:
            if xmas_index == 3:
                xmas_count += 1
            else:
                search(x + x_dir, y + y_dir, x_dir, y_dir, xmas_index + 1)

def check_x_mas(x, y): # if statements straight outta hell
    global x_mas_count
    if (in_boundaries(x - 1, y - 1) and in_boundaries(x + 1, y - 1) and
        in_boundaries(x + 1, y + 1) and in_boundaries(x - 1, y + 1)):
        if (((lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S") or (lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M")) and 
            ((lines[y + 1][x - 1] == "M" and lines[y - 1][x + 1] == "S") or (lines[y + 1][x - 1] == "S" and lines[y - 1][x + 1] == "M"))):
            x_mas_count += 1

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "X":
            search(x, y, -1, -1) # upper left
            search(x, y, 0, -1) # upper
            search(x, y, 1, -1) # upper right
            search(x, y, 1, 0) # right
            search(x, y, 1, 1) # lower right
            search(x, y, 0, 1) # lower
            search(x, y, -1, 1) # lower left
            search(x, y, -1, 0) # left
            
        elif lines[y][x] == "A":
            check_x_mas(x, y)
            
print(xmas_count)
print(x_mas_count)
