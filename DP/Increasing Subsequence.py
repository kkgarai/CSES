"""
You are given an array containing n integers. Your task is to determine the longest increasing subsequence in the array, i.e., the longest subsequence where every element is larger than the previous one.

A subsequence is a sequence that can be derived from the array by deleting some elements without changing the order of the remaining elements.

Input

The first line contains an integer n: the size of the array.

After this there are n integers x1,x2,…,xn: the contents of the array.

Output

Print the length of the longest increasing subsequence.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
8
7 3 5 3 6 2 9 8

Output:
4
"""


n = int(input())
arr = list(map(int, input().split()))


"""
# O(n^2) Solution

dp = [1 for i in range(n)]


longestSubsequenceLength = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], 1+dp[j])

    longestSubsequenceLength = max(dp[i], longestSubsequenceLength)

print(longestSubsequenceLength)
"""

# O(n*log(n)) Solution

# Python program to find
# length of longest
# increasing subsequence
# in O(n Log n) time

# Binary search (note
# boundaries in the caller)
# A[] is ceilIndex
# in the caller


def CeilIndex(A, l, r, key):

    while (r - l > 1):

        m = l + (r - l)//2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r


def LongestIncreasingSubsequenceLength(A, size):

    # Add boundary case,
    # when array size is one

    tailTable = [0 for i in range(size + 1)]
    len = 0  # always points empty slot

    tailTable[0] = A[0]
    len = 1
    for i in range(1, size):

        if (A[i] < tailTable[0]):

            # new smallest value
            tailTable[0] = A[i]

        elif (A[i] > tailTable[len-1]):

            # A[i] wants to extend
            # largest subsequence
            tailTable[len] = A[i]
            len += 1

        else:
            # A[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # ceil value in tailTable
            tailTable[CeilIndex(tailTable, -1, len-1, A[i])] = A[i]

    return len


print(LongestIncreasingSubsequenceLength(arr, n))
