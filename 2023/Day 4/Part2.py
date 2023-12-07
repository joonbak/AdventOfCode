from collections import defaultdict 

with open("Day 4/Input.txt", "r") as file:
    lines = file.read().split("\n")

score = 0
hash_map = defaultdict(int)

for id, line in enumerate(lines):
    hash_map[id] += 1
    id += 1
    lst = []
    for num in line.split(":"):
        for game in num.split("|"):
            card = list(game.split())
            lst.append(card)
            
    tracker = 0
    for i in range(len(lst[2])):
        if lst[2][i] in lst[1]:
            tracker += 1
    if i == len(lst[2])-1:
        copies = 1
        if id in hash_map:
            copies = hash_map[id] + 1
            
        for rounds in range(copies):
            for j in range(1, tracker+1):
                hash_map[id + j] += 1

print(sum(hash_map.values()))


