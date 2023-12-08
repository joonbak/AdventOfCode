from collections import defaultdict 

with open("Day 4/Input.txt", "r") as file:
    lines = file.read().split("\n")

hash_map = defaultdict(int)

for i, line in enumerate(lines):
    hash_map[i] += 1
    rest, second = line.split('|')
    card, first = rest.split(':')
    first_nums = [int(x) for x in first.split()]
    second_nums = [int(x) for x in second.split()]
    val = len(set(first_nums) & set(second_nums))

    for j in range(val):
        hash_map[i+j+1] += hash_map[i]

print(sum(hash_map.values()))


