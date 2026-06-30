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

        before = [1] * len(nums)
        for i in range(1, len(nums)):
            prev_num = nums[i-1]
            prev_res = before[i-1]
            before[i] = prev_num*prev_res
            
        after = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            next_num = nums[i+1]
            next_res = after[i+1]
            after[i] = next_num*next_res
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = before[i] * after[i]


        return res
        