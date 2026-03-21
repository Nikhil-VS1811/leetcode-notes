# Pow(x, n) (LeetCode 50)

## Approach
    1. assign the n to temp
    2. solve the negative n
    3. go to power recursive func
    4. IN recursive FUNC
        1. get the base condition like n==0 and n==1
        2. if n is even then return power(x*x,n/2)
        3. if n is odd then return x* power(x,n-1)   

## Complexity
- Time: O(log n)
- Space: O(log n)
