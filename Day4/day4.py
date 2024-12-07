import re, os, sys

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
inp = sys.stdin.read().strip()
inp = inp.split('\n')
# print(inp)
rows = len(inp); cols = len(inp[0]); tar = 'XMAS'
dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]
revdirs = [(0, -1), (-1, 0), (-1, -1), (-1, 1)]

def is_valid(x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols


def part1(inp):
    xmas_count = 0
    
    def check_word(x, y, dx, dy):
        if is_valid(x + dx*3, y + dy*3, rows, cols):
            if(inp[x][y] == 'X' and inp[x + dx][y + dy] == 'M' and inp[x + dx*2][y + dy*2] == 'A' and inp[x + dx*3][y + dy*3] == 'S'):
                return True
        return False
    
    for i in range(rows):
        for j in range(cols):
            for  (dx, dy) in dirs + revdirs:
                if check_word(i, j, dx, dy):
                    xmas_count += 1
    
    return xmas_count

def part2(inp):
    xmas_count = 0
    for row in range(len(inp)):
        for col in range(len(inp[0])):
            if inp[row][col] == "A":
                if (row - 1 >= 0 and col - 1 >= 0 and col + 1 < len(inp[0]) and row + 1 < len(inp)):
                    tl, tr = inp[row - 1][col - 1], inp[row - 1][col + 1]
                    bl, br = inp[row + 1][col - 1], inp[row + 1][col + 1]

                    vtr = (tl == "M" and br == "S") or (tl == "S" and br == "M")
                    vtl = (tr == "M" and bl == "S") or (tr == "S" and bl == "M")
                    
                    if vtr and vtl:
                        xmas_count += 1
                    
                    
    return xmas_count


print(part1(inp))
print(part2(inp))