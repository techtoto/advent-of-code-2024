#!/usr/bin/env python3

with open("./day09/day09-input.txt") as f:
    input = f.read().replace("\n", "")

disk = []
id = 0
free = False
checksum = 0

def put_n_times_to_disk(n, o):
    global disk
    for i in range(n):
        disk.append(o)

for n in input:
    n = int(n)
    if free:
        put_n_times_to_disk(n, None)
        free = False
    else:
        put_n_times_to_disk(n, id)
        id += 1
        free = True

print(len(disk))

for i in range(len(disk) - 1, 0, -1):
    first_free_disk_index = disk.index(None)
    if first_free_disk_index >= i:
        break
    if disk[i] != None:
        disk[first_free_disk_index] = disk[i]
        disk[i] = None

for i in range(len(disk)):
    if disk[i] != None:
        checksum += i * disk[i]

print(checksum)