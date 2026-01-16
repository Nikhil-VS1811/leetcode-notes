# Missing Number (LeetCode 268)

## Approach
XOR cancels identical numbers.  
XOR all elements of the array with all numbers from 0 to n.  
The remaining value is the missing number.

## Complexity
- Time: O(n)
- Space: O(1)
