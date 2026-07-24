class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        pair_xor_set = set()
        for i in range(n):
            for j in range(i, n):
                pair_xor_set.add(nums[i] ^ nums[j])
        unique_triplet_xors = set()
        for p_val in pair_xor_set:
            for k in range(n):
                unique_triplet_xors.add(p_val ^ nums[k])
                
        return len(unique_triplet_xors)