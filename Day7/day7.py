import os, sys
from itertools import product

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
inp = sys.stdin.read().strip()
inp = inp.split('\n')

def concat(a, b):
    return int(str(a) + str(b))

def eval(num, ops):
    res = num[0]
    for i, op in enumerate(ops):
        if op == "+": res += num[i+1]
        elif op == "*": res *= num[i+1]
        elif op == "||": res = int(str(res) + str(num[i+1]))
    return res

def part1():
    calbs = 0
    for e in inp:
        tv, nums = e.split(":")
        tv = int(tv); nums = list(map(int, nums.split()))
        val_eq = False
        num_slots = len(nums) - 1
        for ops in product(["+", "*"], repeat=num_slots):
            try:
                res = eval(nums, ops)
                if res == tv:
                    val_eq = True
                    break
            except Exception:
                continue
    
        if val_eq:
            calbs += tv
    return calbs

def part2():
    calbs = 0
    for e in inp:
        tv, nums = e.split(":")
        tv = int(tv); nums = list(map(int, nums.split()))
        val_eq = False
        num_slots = len(nums) - 1
        for ops in product(["+", "*", "||"], repeat=num_slots):
            try:
                res = eval(nums, ops)
                if res == tv:
                    val_eq = True
                    break
            except Exception:
                continue
    
        if val_eq:
            calbs += tv
    return calbs

print(part1())
print(part2())