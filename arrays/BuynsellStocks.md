# Best Time to Buy and Sell Stock (LeetCode 121)

## Approach
We use a hash map to store numbers we have seen so far.  
For each number, we check if its complement (target - current number) already exists in the map.

## Complexity
- Time: O(n)
- Space: O(n)
