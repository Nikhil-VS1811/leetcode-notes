class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        mySet=set(nums)
        m=len(mySet)
        return n!=m
            