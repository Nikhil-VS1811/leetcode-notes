class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Given a sorted unique integer array, return the smallest sorted list of ranges
        that cover all numbers in the array.
      
        Args:
            nums: A sorted array of unique integers
          
        Returns:
            A list of string ranges in format "a->b" or "a" for single elements
        """
      
        def format_range(start_idx: int, end_idx: int) -> str:
            """
            Format a range based on start and end indices.
          
            Args:
                start_idx: Starting index of the range
                end_idx: Ending index of the range
              
            Returns:
                String representation of the range
            """
            
            if start_idx == end_idx:
                return str(nums[start_idx])
            
            return f'{nums[start_idx]}->{nums[end_idx]}'
      
        
        current_idx = 0
        array_length = len(nums)
        result = []
      
        
        while current_idx < array_length:
            
            range_end_idx = current_idx
          
            
            while range_end_idx + 1 < array_length and nums[range_end_idx + 1] == nums[range_end_idx] + 1:
                range_end_idx += 1
          
            
            result.append(format_range(current_idx, range_end_idx))
          
            # Move to the next unprocessed element
            current_idx = range_end_idx + 1
      
        return result