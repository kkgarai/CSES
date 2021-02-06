"""
There are n projects you can attend. For each project, you know its starting and ending days and the amount of money you would get as reward. You can only attend one project during a day.

What is the maximum amount of money you can earn?

Input

The first input line contains an integer n: the number of projects.

After this, there are n lines. Each such line has three integers ai, bi, and pi: the starting day, the ending day, and the reward.

Output

Print one integer: the maximum amount of money you can earn.

Constraints
1≤n≤2⋅105
1≤ai≤bi≤109
1≤pi≤109
Example

Input:
4
2 4 4
3 6 6
6 8 2
5 7 3

Output:
7
"""

from bisect import bisect

n = int(input())
job = []
for i in range(n):
    job.append(list(map(int, input().split())))

dp = [0 for _ in range(n)]


job.sort(key=lambda x: x[1])

start, end, reward = [], [], []
for j in job:
    start.append(j[0])
    end.append(j[1])
    reward.append(j[2])

dp[0] = reward[0]

for i in range(1, n):
    included = reward[i]
    idx = bisect(end, start[i]-1)-1
    if idx != -1:
        included += dp[idx]

    excluded = dp[i-1]

    dp[i] = max(included, excluded)

print(dp[-1])
