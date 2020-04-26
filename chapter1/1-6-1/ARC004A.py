import sys
import string
import time
import math


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
# sys.setrecursionlimit(10 ** 6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


def main():
    N = I()
    x = [0] * N
    y = [0] * N

    for i in range(N):
        x[i], y[i] = MI()

    ans = 0.0
    for n in range(N - 1):
        for i in range(n, N):
            length = math.sqrt((x[n] - x[i]) ** 2 + (y[n] - y[i]) ** 2)
            if length > ans:
                ans = length

    print(ans)


if __name__ == '__main__':
    main()
