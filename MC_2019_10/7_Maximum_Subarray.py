class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumulated_sum = nums[0]
        best = cumulated_sum
        for k in nums[1:]:
            cumulated_sum = max(k, cumulated_sum + k)
            best = max(cumulated_sum, best)
        return best
