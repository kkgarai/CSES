"""
Your task is to count the number of ways numbers 1,2,…,n can be divided into two sets of equal sum.

For example, if n=7, there are four solutions:
{1,3,4,6} and {2,5,7}
{1,2,5,6} and {3,4,7}
{1,2,4,7} and {3,5,6}
{1,6,7} and {2,3,4,5}
Input

The only input line contains an integer n.

Output

Print the answer modulo 109+7.

Constraints
1≤n≤500
Example

Input:
7

Output:
4
"""
mod = int(1e9)+7
n = int(input())

s = sum([i for i in range(n+1)])

if s % 2 or s <= 2:
    print(0)
else:
    target = s//2
    dp = [[0 for j in range(target+1)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, target+1):
            dp[i][j] = (dp[i-1][j]+dp[i-1][j-i]) % mod

    print(dp[-1][-1])
