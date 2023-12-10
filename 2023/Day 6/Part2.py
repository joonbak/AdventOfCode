with open("Day 6/Input.txt", "r") as file:
    time, distance = file.read().split("\n")


time =  list(map(int, ["".join(time.split(":")[1].split())]))
distance =  list(map(int, ["".join(distance.split(":")[1].split())]))

total = []
for i in range(len(time)):
    t = time[i]
    d = distance[i]

    wins = 0
    for j in range(t):
        my_dist = j * (t - j)
        if my_dist > d:
            wins += 1
    total.append(wins)

nums = 1
for x in total:
    nums *= x
print(nums)
