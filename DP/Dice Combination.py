"""
Your task is to count the number of ways to construct sum n by throwing a dice one or more times.
Each throw produces an outcome between 1 and 6.

For example, if n=3, there are 4 ways:
1+1+1
1+2
2+1
3
Input

The only input line has an integer n.

Output

Print the number of ways modulo 109+7.

Constraints
1≤n≤106
Example

Input:
3

Output:
4
"""

mod=int(1e9)+7

n=int(input())
dp=[0 for _ in range(n+1)]
dp[0]=1
dp[1]=1

for i in range(2,n+1):
    for j in range(1,7):
        if i-j<0:
            break
        dp[i]=(dp[i]+dp[i-j])%mod
# print(dp)
print(dp[-1])
