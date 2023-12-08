with open("Day 6/Input.txt", "r") as file:
    lines = file.read().split("\n")

line = lines
lst = []
for line in lines:
    id, rest = line.split(":")
    num = rest.replace(" ", "")
    lst.append(num)

wins = 0
for j in range(int(lst[0])):
    race = int(lst[0]) - j
    if race * j > int(lst[1]):
        wins += 1

print(wins)

