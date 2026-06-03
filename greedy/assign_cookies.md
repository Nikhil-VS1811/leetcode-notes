# Assign Cookies (LeetCode 455)

## Approach
1) sort it
2) while(studInd<g.size() && cookieInd<s.size())
        {
            if(s[cookieInd]>=g[studInd])
            {
                studInd++;   
            }
            cookieIndex++;
        }

## Complexity
- Time: O(n*logn + m*logm),
- Space: O(n)
