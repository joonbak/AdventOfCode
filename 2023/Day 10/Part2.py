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

maybe_s = {"|", "-", "J", "L", "7", "F"}

while q:
    r, c = q.popleft()
    ch = lines[r][c]

    if r > 0 and ch in "S|JL" and lines[r - 1][c] in "|7F" and (r - 1, c) not in seen:
        seen.add((r - 1, c))
        q.append((r - 1, c))
        if ch == "S":
            maybe_s &= {"|", "J", "L"}
        
    if r < len(lines) - 1 and ch in "S|7F" and lines[r + 1][c] in "|JL" and (r + 1, c) not in seen:
        seen.add((r + 1, c))
        q.append((r + 1, c))
        if ch == "S":
            maybe_s &= {"|", "7", "F"}

    if c > 0 and ch in "S-J7" and lines[r][c - 1] in "-LF" and (r, c - 1) not in seen:
        seen.add((r, c - 1))
        q.append((r, c - 1))
        if ch == "S":
            maybe_s &= {"-", "J", "7"}

    if c < len(lines[r]) - 1 and ch in "S-LF" and lines[r][c + 1] in "-J7" and (r, c + 1) not in seen:
        seen.add((r, c + 1))
        q.append((r, c + 1))
        if ch == "S":
            maybe_s &= {"-", "L", "F"}

assert len(maybe_s) == 1
(S,) = maybe_s

lines = [row.replace("S", S) for row in lines]
lines = ["".join(ch if (r, c) in seen else "." for c, ch in enumerate(row)) for r, row in enumerate(lines)]

outside = set()

for r, row in enumerate(lines):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError(f"unexpected character (horizontal): {ch}")
        if not within:
            outside.add((r, c))
            
print(len(lines) * len(lines[0]) - len(outside | seen))
