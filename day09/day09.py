#!/usr/bin/env python3

with open("./day09/day09-input.txt") as f:
    input = f.read().replace("\n", "")

disk1 = []
disk2 = []
id = 0
free = False

def put_n_times_to_disks(n, o):
    global disk
    for i in range(n):
        disk1.append(o)
        disk2.append(o)

def get_suiting_free_block(n, disk: list):
    i = disk.index(None)
    current_block_length = get_block_length(i, disk)
    while n > current_block_length:
        try:
            i = disk.index(None, i + current_block_length)
        except ValueError:
            return None
        current_block_length = get_block_length(i, disk)
    return i

def get_block_length(i, disk: list):
    for j in range(i, len(disk)):
        if disk[i] != disk[j]:
            return j - i
    return j - i + 1

def move_file(id, disk: list):
    file_i = disk.index(id)
    file_length = disk.count(id)
    to_i = get_suiting_free_block(file_length, disk)
    if to_i != None:
        if to_i < file_i:
            for i in range(file_length):
                disk[to_i + i] = id
                disk[file_i + i] = None

for n in input:
    n = int(n)
    if free:
        put_n_times_to_disks(n, None)
        free = False
    else:
        put_n_times_to_disks(n, id)
        id += 1
        free = True

for i in range(len(disk1) - 1, 0, -1):
    first_free_disk_index = disk1.index(None)
    if first_free_disk_index >= i:
        break
    if disk1[i] != None:
        disk1[first_free_disk_index] = disk1[i]
        disk1[i] = None

def checksum(disk):
    sum = 0
    for i in range(len(disk)):
        if disk[i] != None:
            sum += i * disk[i]
    return sum

print(checksum(disk1))

for id in range(disk2[-1], -1, -1):
    move_file(id, disk2)

print(checksum(disk2))
