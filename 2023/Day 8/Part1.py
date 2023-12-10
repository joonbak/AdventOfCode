with open("Day 8/Input.txt", "r") as file:
    lines = file.read().split("\n\n")

steps, *blocks = lines

for block in blocks:
    element = block.split("\n")

line = [x.replace(" ", "").split("=") for x in element]

hash_map = {}
for row in line:
    hash_map[row[0]] = list(row[1][1:-1].split(","))


curr = "AAA"
step_count = 0


while curr != "ZZZ":
    step_count += 1

    if steps[0] == "R":
        curr = hash_map[curr][1]
    else:
        curr = hash_map[curr][0]
    
    steps = steps[1:] + steps[0]

print(step_count)