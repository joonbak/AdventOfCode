with open("Day 1/Input.txt", "r") as file:
    lines = file.read().split("\n")

ans = 0

for c in lines:
    digits = []
    for i in c:
        if i.isdigit():
            digits.append(i)
    sum = digits[0]+digits[-1]
    ans += int(sum)

print(ans)

