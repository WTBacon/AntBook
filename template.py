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
# sys.setrecursionlimit(10 ** 6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


def main():
    pass


if __name__ == '__main__':
    main()


# ===================　テンプレここまで =====================#
# リスト出力
def print_list(list):
    print(*list)
    return


# 2次元配列出力
def print_map(maplist):
    for i in maplist: print(*i, sep='')
    return


def memo():
    a = [0] * 5
    b = a  # 良くない配列のコピー
    b2 = a[:]  # 1次元のときはコピーはこれで良い
    a[1] = 3
    print('b:{}, b2:{}'.format(b, b2))  # b:[0, 3, 0, 0, 0], b2:[0, 0, 0, 0, 0]

    import copy
    a = [[0] * 3 for i in range(5)]  # 2次元配列はこう準備、[[0]*3]*5だとだめ
    b = copy.deepcopy(a)

    # 内包表記奇数のみ
    odd = [i for i in range(100) if i % 2 == 1]  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # 二部探索
    import bisect
    a = [1, 2, 3, 5, 6, 7, 8, 9]
    b = bisect.bisect_left(a, 8)

    # combinations、組み合わせ、順列
    from itertools import permutations, combinations, combinations_with_replacement, product
    a = ['a', 'b', 'C']
    print(list(permutations(a)))
    print(list(combinations(a, 2)))
    print(list(combinations_with_replacement(a, 3)))


# 素数生成
def generate_primenums():
    n = 100
    primes = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5 + 1)):
        primes.difference_update(range(i * 2, n + 1, i))
    primes = list(primes)
    return primes


# 階乗
def kaijo(n):
    import math
    return math.factorial(n)


# 選び方（コンビネーション nCr）
def num_combination(n, r):
    import math
    return math.factorial(n) // math.factorial(n - r)


# 最大公約数、最小公倍数
def calc_gcd(a, b):
    import fractions
    gcd = fractions.gcd(a, b)
    lcm = a * b // gcd
    return gcd, lcm


# 複数の最大公約数
def calc_gcd_list(l):
    import fractions
    gcd = l[0]
    for i in range(1, N):
        gcd = fractions.gcd(gcd, l[i])
    return gcd


# 各桁の和
def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def ceil(n):
    return n // 2 if n % 2 == 0 else n // 2 + 1
