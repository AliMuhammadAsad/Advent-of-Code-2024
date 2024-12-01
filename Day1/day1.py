import os, sys

if os.path.exists('input1.txt'):
    sys.stdin = open('input1.txt', 'r')
inp = sys.stdin.read().strip()
inp = inp.split('\n')
lst1 = [int(x.split()[0]) for x in inp]; lst2 = [int(x.split()[1]) for x in inp]
lst1.sort(); lst2.sort()


def part1(lst1, lst2):
    return sum(abs(lst1[i] - lst2[i]) for i in range(len(lst1)))

def part2(lst1, lst2):
    freq = {}   
    for i in lst2:
        if i in freq: freq[i] += 1
        else: freq[i] = 1

    return sum(i*freq[i] for i in lst1 if i in freq and freq[i] > 0)
    

print(part1(lst1, lst2))    # 2285373
print(part2(lst1, lst2))    # 21142653