with open("Day 6/Input.txt", "r") as file:
    lines = file.read().split("\n")

lst = []
for line in lines:
    lst.append(line.split(":")[1].split())

total = []
for i in range(len(lst[0])):
    wins = 0
    for j in range(int(lst[0][i])):
        race = int(lst[0][i]) - j
        if race * j > int(lst[1][i]):
            wins += 1
    total.append(wins)

nums = 1
for x in total:
    nums *= x
print(nums)
