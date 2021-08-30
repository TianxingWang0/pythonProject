
def subarraysDivByK(A, K):
    from collections import defaultdict

    memo = defaultdict(int)  # Memoization as: cumulativeSum mod K -> Frequency
    memo[0] = 1

    currSum = 0  # Current cumulative sum
    count = 0  # Number of continuous subarrays whose sum is divisible by K

    for i in A:
        currSum += i
        mod = currSum % K
        if mod in memo:
            count += memo[mod]

        memo[mod] += 1

    return count

subarraysDivByK([2, -2, 2, -4], 6)