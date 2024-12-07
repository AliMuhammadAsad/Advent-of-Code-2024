import re, os, sys

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
inp = sys.stdin.read().strip()
# inp = inp.split('\n')
pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
do_p = r'do\(\)'
dont_p = r"don't\(\)"

def part1(inp):
    tok = re.findall(pattern, inp)
    sumi = sum(int(x) * int(y) for x, y in tok)
    return sumi

def part2(inp):
    mule = True; sumi = 0
    mulm = re.finditer(pattern, inp)
    dom = re.finditer(do_p, inp)
    dontm = re.finditer(dont_p, inp)

    allm = sorted(list(mulm) + list(dom) + list(dontm), key=lambda x: x.start())

    for am in allm:
        if am.group() == 'do()': mule = True
        elif am.group() == "don't()": mule = False
        else:
            x, y = re.match(pattern, am.group()).groups()
            if mule: sumi += int(x) * int(y)
    return sumi

print(part1(inp))
print(part2(inp))