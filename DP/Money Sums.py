"""
You have n coins with certain values. Your task is to find all money sums you can create using these coins.

Input

The first input line has an integer n: the number of coins.

The next line has n integers x1,x2,…,xn: the values of the coins.

Output

First print an integer k: the number of distinct money sums. After this, print all possible sums in increasing order.

Constraints
1≤n≤100
1≤xi≤1000
Example

Input:
4
4 2 5 2

Output:
9
2 4 5 6 7 8 9 11 13

"""


n = int(input())
coins = list(map(int, input().split()))

res = set()
for c in coins:
    if not res:
        res.add(c)
        continue
    temp = []
    for x in res:
        temp.append(x+c)

    res.add(c)
    for x in temp:
        res.add(x)


print(len(res))
print(*sorted(res))
