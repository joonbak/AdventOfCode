with open("Day 11/Input.txt", "r") as file:
    lines = file.read().split("\n")

def empty_rows(lines):
    empty = []
    for r, row in enumerate(lines):
        if all(ch == "." for ch in row):
            empty.append(r)
    return empty

def empty_cols(lines):
    empty = []
    for c, col in enumerate(zip(*lines)):
        if all(ch == "." for ch in col):
            empty.append(c)
    return empty

def vectors(lines):
    galaxies = []
    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if ch == "#":
                galaxies.append((r, c))
    return galaxies

empty_r = empty_rows(lines)
empty_c = empty_cols(lines)
points = vectors(lines)

distance = 0
scale = 1000000

for i, (r1, c1) in enumerate(points):
    for (r2, c2) in points[:i]:
        for r in range(min(r1, r2), max(r1, r2)):
            distance += scale if r in empty_r else 1
        for c in range(min(c1, c2), max(c1, c2)):
            distance += scale if c in empty_c else 1

print(distance)