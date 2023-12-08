with open("Day 5/Input.txt", "r") as file:
    lines = file.read().split("\n\n")

inputs, *blocks = lines

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for a, b, c in ranges:
            overlap_start = max(start, b)
            overlap_end = min(end, b + c)
            if overlap_start < overlap_end:
                new.append((overlap_start - b + a, overlap_end - b + a))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                break
        else:
            new.append((start, end))
    seeds = new

print(min(seeds)[0])