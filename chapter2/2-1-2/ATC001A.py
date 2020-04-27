import sys
import string
import time


def input():
    return sys.stdin.readline().rstrip()


def I():
    return int(input())


def S():
    return input()


def MI():
    return map(int, input().split())


def MS():
    return map(str, input().split())


def LI():
    return list(map(int, input().split()))


def LI_():
    return [int(i) - 1 for i in input().split()]


def StoI():
    return [ord(i) - 97 for i in input()]


def ItoS(nn):
    return chr(nn + 97)


N = {False: 'No', True: 'Yes'}
MOD = 10 ** 9 + 7
inf = float('inf')
IINF = 10 ** 10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10 ** 9)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    H, W = MI()
    c = [list(S()) for _ in range(H)]

    for h in range(H):
        if 's' in c[h]:
            s = (h, c[h].index('s'))
        if 'g' in c[h]:
            g = (h, c[h].index('g'))

    def dfs(y, x):
        c[y][x] = '#'
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if (0 <= nx) and (nx < W) and (0 <= ny) and (ny < H) and (c[ny][nx] != '#'):
                dfs(ny, nx)

    dfs(s[0], s[1])
    if c[g[0]][g[1]] == 'g':
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
