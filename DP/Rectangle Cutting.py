"""
Given an a×b rectangle, your task is to cut it into squares. On each move you can select a rectangle and cut it into two rectangles in such a way that all side lengths remain integers. What is the minimum possible number of moves?

Input

The only input line has two integers a and b.

Output

Print one integer: the minimum number of moves.

Constraints
1≤a,b≤500
Example

Input:
3 5

Output:
3
"""


a, b = list(map(int, input().split()))

dp = [[float('inf') for _ in range(b+1)] for _ in range(a+1)]
for i in range(a+1):
    for j in range(b+1):
        if i == j:
            dp[i][j] = 0
        else:
            for k in range(1, i):
                dp[i][j] = min(dp[i][j], 1+dp[k][j]+dp[i-k][j])

            for k in range(1, j):
                dp[i][j] = min(dp[i][j], 1+dp[i][k]+dp[i][j-k])

print(dp[-1][-1])
