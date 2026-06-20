class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
      
        # Iterate through the array with index and value
        for current_index, value in enumerate(nums):
            # Check if we've seen this value before and if the distance is within k
            if value in index_map and current_index - index_map[value] <= k:
                # Found a duplicate within distance k
                return True
          
            # Update the dictionary with the current index for this value
            # This overwrites any previous index, keeping only the most recent
            index_map[value] = current_index
      
        # No duplicates found within distance k
        return False