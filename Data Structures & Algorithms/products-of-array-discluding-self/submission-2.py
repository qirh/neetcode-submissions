class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        [
            1 -> 2 x 4 x 6
            2 -> 1 x 4 x 6
            4 -> 1 x 2 x 6
            6 -> 1 x 2 x 4
        ]
        before = [(1), 1, 1 x 2 = 2, 1 x 2 x 4 = 8]
        after = [2 x 4 x 6 = 48, 4 x 6 = 24, 6, (1)]
        res = 
        """

        res = [1] * len(nums)
        for i in range(1, len(nums)):
            prev_num = nums[i-1]
            prev_res = res[i-1]
            res[i] = prev_num*prev_res
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        