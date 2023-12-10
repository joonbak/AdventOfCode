with open("Day 3/Input.txt", "r") as file:
    lines = file.read().split("\n")

matrix = [list(line) for line in lines]

n_rows = len(matrix)
n_cols = len(matrix[0])

ans = 0

for i in range(n_rows):
    num = 0
    valid = False
    for j in range(len(matrix[i])+1):
        if j < n_cols and matrix[i][j].isdigit():
            num = num*10+int(matrix[i][j])
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i+x < n_rows and 0 <= j+y < n_cols:
                        curr = matrix[i+x][j+y]
                        if curr != "." and not curr.isdigit():
                            valid = True

        elif num > 0:
            if valid:
                ans += num
            num = 0
            valid = False
print(ans)


    
