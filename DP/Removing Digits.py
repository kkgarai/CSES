"""
You are given an integer n. 
On each step, you may substract from it any one-digit number that appears in it.

How many steps are required to make the number equal to 0?

Input

The only input line has an integer n.

Output

Print one integer: the minimum number of steps.

Constraints
1≤n≤106
Example

Input:
27

Output:
5

Explanation: An optimal solution is 27→20→18→10→9→0.
"""
n = int(input())

dp = [float('inf') for _ in range(n+1)]
dp[0] = 0

for i in range(n+1):
    for c in str(i):
        dp[i] = min(dp[i], 1+dp[i-(ord(c)-ord('0'))])

print(dp[-1])
