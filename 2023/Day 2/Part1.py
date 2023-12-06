with open("Day 2/Input.txt", "r") as file:
    lines = file.read().split("\n")

hash_map = {"red" : 12, "green" : 13, "blue" : 14}

ans = 0

for line in lines:
    valid = True
    id, line = line.split(":")
    for game in line.split(";"):
        for balls in game.split(","):
            num, colour = balls.split()
            if int(num) > hash_map[colour]:
                valid = False
    if valid:
        ans += int(id.split()[-1]) 
        
print(ans)

