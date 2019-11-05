class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_copy = nums.copy()
        sorted_copy.sort()
        ind_min = 0
        ind_max = len(sorted_copy) - 1
        while(ind_min != ind_max):
            sum_ind = sorted_copy[ind_min] + sorted_copy[ind_max]
            if sum_ind > target:
                ind_max -= 1
            elif sum_ind < target:
                ind_min += 1
            else:
                break
        ind_first = nums.index(sorted_copy[ind_min])
        ind_second = nums.index(sorted_copy[ind_max])
        if ind_first == ind_second:
            ind_second = nums[ind_second +
                              1:].index(nums[ind_second]) + ind_second + 1
        return [ind_first, ind_second]
