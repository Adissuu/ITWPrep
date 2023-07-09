class Solution(object):
    def maximumJumps(self, nums, target):
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if -target <= nums[i] - nums[j] <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        if dp[n - 1] == -float('inf'):
            return -1
        else:
            return dp[n - 1]
