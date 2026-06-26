class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()

        for i in range(len(nums)):
            num = nums[i]
            if (target-num) in s:
                return [s[target-num], i]
            s[num] = i
        return False