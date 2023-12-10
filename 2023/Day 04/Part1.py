with open("Day 4/Input.txt", "r") as file:
    lines = file.read().split("\n")

score = 0

for line in lines:
    rest, second = line.split('|')
    card, first = rest.split(':')
    first_nums = [int(x) for x in first.split()]
    second_nums = [int(x) for x in second.split()]
    val = len(set(first_nums) & set(second_nums))
    if val > 0:
        score += 2**(val-1)

print(score)

