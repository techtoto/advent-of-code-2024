#!/usr/bin/env python3

xmas = "XMAS"
xmas_index = 1

xmas_count = 0
x_mas_count = 0

with open("./day04/day04-input.txt") as f:
    lines = f.read().split("\n") # lines[y][x]

def in_boundaries(x, y):
    return x in range(len(lines[y])) and y in range(len(lines))

def search_upper_left(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x - 1, y - 1):
        if lines[y - 1][x - 1] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_upper_left(x - 1, y - 1)

def search_upper(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x, y - 1):
        if lines[y - 1][x] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_upper(x, y - 1)

def search_upper_right(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x + 1, y - 1):
        if lines[y - 1][x + 1] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_upper_right(x + 1, y - 1)

def search_right(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x + 1, y):
        if lines[y][x + 1] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_right(x + 1, y)

def search_lower_right(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x + 1, y + 1):
        if lines[y + 1][x + 1] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_lower_right(x + 1, y + 1)

def search_lower(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x, y + 1):
        if lines[y + 1][x] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_lower(x, y + 1)

def search_lower_left(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x - 1, y + 1):
        if lines[y + 1][x - 1] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_lower_left(x - 1, y + 1)

def search_left(x, y):
    global xmas_index, xmas_count
    if in_boundaries(x - 1, y):
        if lines[y][x - 1] == xmas[xmas_index]:
            if xmas_index == 3:
                xmas_index = 1
                xmas_count += 1
            else:
                xmas_index += 1
                search_left(x - 1, y)

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
            xmas_index = 1
            search_upper_left(x, y)

            xmas_index = 1
            search_upper(x, y)
            
            xmas_index = 1
            search_upper_right(x, y)
            
            xmas_index = 1
            search_right(x, y)
            
            xmas_index = 1
            search_lower_right(x, y)
            
            xmas_index = 1
            search_lower(x, y)
            
            xmas_index = 1
            search_lower_left(x, y)
            
            xmas_index = 1
            search_left(x, y)
        elif lines[y][x] == "A":
            check_x_mas(x, y)
            
print(xmas_count)
print(x_mas_count)
