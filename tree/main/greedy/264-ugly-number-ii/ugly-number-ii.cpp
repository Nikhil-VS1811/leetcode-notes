class Solution {
public:
    int nthUglyNumber(int n) {
        priority_queue<long long,vector<long long>,greater<long long>>minHeap;
        unordered_set<long long>visited;

        minHeap.push(1);
        visited.insert(1);
        long long ugly=1;

        for(int i=0;i<n;i++)
        {
            ugly=minHeap.top();
            minHeap.pop();

            long long a=ugly*2;
            long long b=ugly*3;
            long long c=ugly*5;

            if(!visited.count(a))
            {
                minHeap.push(a);
                visited.insert(a);
            }
            if(!visited.count(b))
            {
                minHeap.push(b);
                visited.insert(b);
            }
            if(!visited.count(c))
            {
                minHeap.push(c);
                visited.insert(c);
            }
        }
        return (int)ugly;
    }
};