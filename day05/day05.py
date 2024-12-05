#!/usr/bin/env python3

rules = []
pages = []
sum = 0

with open("./day05/day05-input.txt") as f:
    lines = f.read().split("\n")

for i in range(len(lines)):
    if lines[i] != "":
        rules.append(tuple([int(x) for x in lines[i].split("|")]))
    else:
        pages = lines[i+1:]
        break

pages = [tuple([int(x) for x in line.split(",")]) for line in pages]

def get_rules_for_page(page):
    current_rules = []
    for rule in rules:
        if rule[0] == page:
            current_rules.append(rule)
    return current_rules

for page_set in pages:
    rule_break = False

    for i in range(len(page_set)):
        if not rule_break:
            for rule in get_rules_for_page(page_set[i]):
                try:
                    first_index = page_set.index(rule[1])
                except ValueError:
                    continue
                else:
                    if first_index < i:
                        rule_break = True
                        break
        else:
            break

    if not rule_break:
        sum += page_set[int((len(page_set)) / 2)]
    
print(sum)
                
