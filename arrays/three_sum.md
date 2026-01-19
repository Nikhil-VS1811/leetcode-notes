# Three Sum (LeetCode 15)

## Approach
We use a hash map to store numbers we have seen so far.  
For each number, we check if its complement (target - current number) already exists in the map.

## Complexity
- Time: O(nlog n)+o(n2)
- Space: O(no of unique triplets)
