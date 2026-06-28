class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        freq_by_num: {
            1: 1,
            2: 2,
            3: 3
        }
        ---
        nums_by_freq: [
            {1}, # i = 0
            {2}, # i = 1
            {3}, # i = 2
            {}, # i = 3
            {}, # i = 4
            {}, # i = 5
        ]
        ---
        res = []
        """
        freq_by_num = {}

        for num in nums:
            if num not in freq_by_num:
                freq_by_num[num] = 0
            freq_by_num[num] += 1
        

        nums_by_freq = [set() for i in range(len(nums))]
        
        for num, freq in freq_by_num.items():
        
            nums_by_freq[freq-1].add(num)
        
        
        res = []

        for i in range(len(nums_by_freq)-1, -1, -1):
            res.extend(nums_by_freq[i])
            if len(res) == k:
                return res
            elif len(res) > k:
                return res[:k]
        
        return res
        