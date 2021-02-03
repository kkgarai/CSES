"""
Consider an n×n grid whose squares may have traps. It is not allowed to move to a square with a trap.

Your task is to calculate the number of paths from the upper-left square to the lower-right square where you only can move right or down.

Input

The first input line has an integer n: the size of the grid.

After this, there are n lines that describe the grid. Each line has n characters: . denotes an empty cell, and * denotes a trap.

Output

Print the number of paths modulo 109+7.

Constraints
1≤n≤1000
Example

Input:
4
....
.*..
...*
*...

Output:
3


"""


mod = int(1e9)+7
grid = []

n = int(input())

for _ in range(n):
    grid.append(input().strip())


if grid[-1][-1] == '*':
    print(0)
else:
    dp = [[0 for i in range(n)] for j in range(n)]
    dp[-1][-1] = 1

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j] == '*':
                continue
            if j != n-1:
                dp[i][j] = (dp[i][j] + dp[i][j+1]) % mod

            if i != n-1:
                dp[i][j] = (dp[i][j] + dp[i+1][j]) % mod

    print(dp[0][0])
