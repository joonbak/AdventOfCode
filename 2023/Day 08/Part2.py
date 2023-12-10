from math import gcd

with open("Day 8/Input.txt", "r") as file:
    lines = file.read().split("\n\n")

steps, *blocks = lines

for block in blocks:
    element = block.split("\n")

line = [x.replace(" ", "").split("=") for x in element]

hash_map = {}
for row in line:
    hash_map[row[0]] = list(row[1][1:-1].split(","))

positions = [key for key in hash_map if key.endswith("A")]
cycles = []

for curr in positions:
    cycle = []
    curr_steps = steps
    step_count= 0
    first_z = None

    while True:
        while step_count == 0 or not curr.endswith("Z"):
            step_count += 1
            if curr_steps[0] == "R":
                curr = hash_map[curr][1]
            else:
                curr = hash_map[curr][0]

            curr_steps = curr_steps[1:] + curr_steps[0]

        cycle.append(step_count)

        if first_z == None:
            first_z = curr
            step_count = 0
        elif curr == first_z:
            break

    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)
