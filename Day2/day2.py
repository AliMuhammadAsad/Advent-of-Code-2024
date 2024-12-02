import os, sys

if os.path.exists('input2.txt'):
    sys.stdin = open('input2.txt', 'r')
inp = sys.stdin.read().strip()
inp = inp.split('\n')
lst = [x.split() for x in inp]

def isSafe(lst):
    is_inc = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    is_dec = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

    if not(is_inc or is_dec): return False

    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if diff < 1 or diff > 3: return False
    
    return True

def part1(lst):
    return sum(isSafe([int(x) for x in sublst]) for sublst in lst)

def part2(lst):
    safe = 0
    for sublst in lst:
        if isSafe([int(x) for x in sublst]): safe += 1
        else:
            for i in range(len(sublst)):
                modified_sublst = sublst[:i] + sublst[i + 1:]
                if isSafe([int(x) for x in modified_sublst]):
                    safe += 1; break
    
    return safe


print(part1(lst)) # 572
print(part2(lst)) # 612
