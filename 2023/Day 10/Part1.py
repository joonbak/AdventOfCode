from collections import deque

with open("Day 10/Input.txt", "r") as file:
    lines = file.read().split("\n")

for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

seen = {(sr, sc)}
q = deque([{sr, sc}])

while q:
    r, c = q.popleft()
    ch = lines[r][c]

    if r > 0 and ch in "S|JL" and lines[r - 1][c] in "|7F" and (r - 1, c) not in seen:
        seen.add((r - 1, c))
        q.append((r - 1, c))
        
    if r < len(lines) - 1 and ch in "S|7F" and lines[r + 1][c] in "|JL" and (r + 1, c) not in seen:
        seen.add((r + 1, c))
        q.append((r + 1, c))

    if c > 0 and ch in "S-J7" and lines[r][c - 1] in "-LF" and (r, c - 1) not in seen:
        seen.add((r, c - 1))
        q.append((r, c - 1))

    if c < len(lines[r]) - 1 and ch in "S-LF" and lines[r][c + 1] in "-J7" and (r, c + 1) not in seen:
        seen.add((r, c + 1))
        q.append((r, c + 1))

print(len(seen) // 2)

