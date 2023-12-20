with open("Day 12/Input.txt", "r") as file:
    lines = file.read().split("\n")

cache = {}

def count(cfg, nums):
    if cfg == "":
        if nums == ():
            return 1
        else:
            return 0
    if nums == ():
        if "#" in cfg:
            return 0
        else:
            return 1
    
    key = (cfg, nums)

    if key in cache:
        return cache[key]
    
    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])
        else:
            result += 0

    cache[key] = result        
    return result


total = 0

for line in lines:
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    cfg = "?".join([cfg] * 5)
    nums *= 5
    total += count(cfg, nums)

print(total)