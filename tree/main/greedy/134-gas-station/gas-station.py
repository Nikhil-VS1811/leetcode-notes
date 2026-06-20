class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Find the starting gas station index from which we can complete a circular tour.
        Uses a two-pointer approach to efficiently find the valid starting point.
      
        Args:
            gas: List of gas available at each station
            cost: List of gas cost to travel from station i to station i+1
          
        Returns:
            Starting station index if circuit is possible, -1 otherwise
        """
        n = len(gas)
      
        # Initialize pointers: start_index and end_index both at the last station
        start_index = n - 1
        end_index = n - 1
      
        # Track number of stations visited and current gas balance
        stations_visited = 0
        gas_balance = 0
      
        # Continue until we've checked all stations
        while stations_visited < n:
            # Add gas and subtract cost at current end position
            gas_balance += gas[end_index] - cost[end_index]
            stations_visited += 1
          
            # Move end pointer forward (circular)
            end_index = (end_index + 1) % n
          
            # If gas balance becomes negative, extend from the start
            while gas_balance < 0 and stations_visited < n:
                # Move start pointer backward
                start_index -= 1
              
                # Add gas and subtract cost at new start position
                gas_balance += gas[start_index] - cost[start_index]
                stations_visited += 1
      
        # If final balance is negative, circuit is impossible
        return -1 if gas_balance < 0 else start_index