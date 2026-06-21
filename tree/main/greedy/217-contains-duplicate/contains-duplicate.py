class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        mySet=set()
        for i in range(n):
            mySet.add(nums[i])
        m=len(mySet)
        if n==m:
            return False
        return True