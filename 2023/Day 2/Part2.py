with open("Day 2/Input.txt", "r") as file:
    lines = file.read().split("\n")

ans = 0


for line in lines:
    id, line = line.split(":")
    hash_map = {"red" : 0, "green" : 0, "blue" : 0}
    for game in line.split(";"):
        for balls in game.split(","):
            num, colour = balls.split()
            hash_map[colour] = max(hash_map[colour], int(num))
    power = 1
    for i in hash_map.values():
        power *= i
    ans += power
print(ans)
