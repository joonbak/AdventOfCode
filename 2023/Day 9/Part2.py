with open("Day 9/Input.txt", "r") as file:
    lines = file.read().split("\n")

def f(digits):
    d = []
    for i in range(len(digits) - 1):
        d.append(digits[i+1] - digits[i])
    if all(x==0 for x in d):
        return digits[0]
    else:
        return digits[0] - f(d)



ans = 0
for line in lines:
    digits = [int(x) for x in line.split()]
    ans += f(digits)

print(ans)