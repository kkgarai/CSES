"""
The edit distance between two strings is the minimum number of operations required to transform one string into the other.

The allowed operations are:
Add one character to the string.
Remove one character from the string.
Replace one character in the string.
For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.

Your task is to calculate the edit distance between two strings.

Input

The first input line has a string that contains n characters between A–Z.

The second input line has a string that contains m characters between A–Z.

Output

Print one integer: the edit distance between the strings.

Constraints
1≤n, m≤5000
Example

Input:
LOVE
MOVIE

Output:
2
"""

a = input()
b = input()

dp = [[float('inf') for _ in range(len(a)+1)] for _ in range(2)]

for j in range(len(a)):
    dp[0][j] = j  # when len_s2 = 0, we need to remove all of s2


for i in range(1, len(b)+1):
    for j in range(len(a)+1):
        if j == 0:
            dp[i % 2][j] = i  # when all of s1 is empty, fill s1
        elif a[j-1] == b[i-1]:
            # last element is same,so no changed needed
            dp[i % 2][j] = dp[(i-1) % 2][j-1]
        else:
            dp[i % 2][j] = 1 + min(dp[(i - 1) % 2][j],
                                   min(dp[i % 2][j - 1], dp[(i - 1) % 2][j - 1]))

            # case 1 = insert
            # case 2 = remove
            # case 3 = replace

# modulo taken to store values in odd and even places
print(dp[len(b) % 2][-1])
