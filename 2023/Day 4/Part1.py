with open("Day 4/Input.txt", "r") as file:
    lines = file.read().split("\n")

score = 0

for line in lines:
    lst = []
    for num in line.split(":"):
        for game in num.split("|"):
            card = list(game.split())
            lst.append(card)
            
    points = 0
    tracker = 0
    for i in range(len(lst[2])):
        if lst[2][i] in lst[1]:
            if tracker > 0:
                points *= 2
            else:
                points = 1
            tracker += 1

    score += points
print(score)
