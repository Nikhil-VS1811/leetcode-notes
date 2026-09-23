from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        freq=Counter(nums)

        for key,val in freq.items():
            if val>len(nums)//2:
                return key