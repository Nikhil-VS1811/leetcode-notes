# String to Integer (atoi) (LeetCode 8)

## Approach
    1. delete white spaces
    2. get the sign
    3. get the helper func() ie.recurion func
    4. IN HELPER FUNC
        1. get the base condition 
        2. get the formula ie. num=num*10(s[i]-'0)
        3. crlt overflows
        4. return helper recursion

## Complexity
- Time: O(n)
- Space: O(n)
