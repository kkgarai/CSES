"""
There is a list of n numbers and two players who move alternately. On each move, a player removes either the first or last number from the list, and their score increases by that number. Both players try to maximize their scores.

What is the maximum possible score for the first player when both players play optimally?

Input

The first input line contains an integer n: the size of the list.

The next line has n integers x1, x2, …, xn: the contents of the list.

Output

Print the maximum possible score for the first player.

Constraints
1≤n≤5000
−109≤xi≤109
Example

Input:
4
4 5 1 3

Output:
8
"""


n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for len in range(1, n+1):
    for i in range(n-len+1):
        j = i+len-1
        x = dp[i+2][j] if i+2 <= j else 0
        y = dp[i+1][j-1] if i+1 <= j-1 else 0
        z = dp[i][j-2] if i <= j-2 else 0

        dp[i][j] = max(arr[i]+min(x, y), arr[j]+min(y, z))

print(dp[0][-1])
