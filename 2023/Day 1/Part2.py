with open("Input.txt", "r") as file:
    lines = file.read().split("\n")

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ans = 0

for string in lines:
    digits = []
    for i, char in enumerate(string):
        if char.isdigit():
            digits.append(char)
        for d, val in enumerate(nums):
            if string[i:].startswith(val):
                digits.append(str(d+1))

    sum = digits[0]+digits[-1]
    ans += int(sum)

print(ans)
