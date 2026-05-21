class Solution {
public:
    priority_queue<int> small;
    priority_queue<int, vector<int>, greater<int>> large;

    unordered_map<int,int> delayed;

    int smallSize = 0;
    int largeSize = 0;

    void pruneSmall() {
        while(!small.empty()) {
            int num = small.top();

            if(delayed.count(num)) {
                delayed[num]--;

                if(delayed[num] == 0) {
                    delayed.erase(num);
                }

                small.pop();
            }
            else {
                break;
            }
        }
    }

    void pruneLarge() {
        while(!large.empty()) {
            int num = large.top();

            if(delayed.count(num)) {
                delayed[num]--;

                if(delayed[num] == 0) {
                    delayed.erase(num);
                }

                large.pop();
            }
            else {
                break;
            }
        }
    }

    void balance() {

        if(smallSize > largeSize + 1) {

            large.push(small.top());
            small.pop();

            smallSize--;
            largeSize++;

            pruneSmall();
        }

        else if(smallSize < largeSize) {

            small.push(large.top());
            large.pop();

            smallSize++;
            largeSize--;

            pruneLarge();
        }
    }

    void addNum(int num) {

        if(small.empty() || num <= small.top()) {
            small.push(num);
            smallSize++;
        }
        else {
            large.push(num);
            largeSize++;
        }

        balance();
    }

    void removeNum(int num) {

        delayed[num]++;

        if(num <= small.top()) {
            smallSize--;

            if(num == small.top()) {
                pruneSmall();
            }
        }
        else {
            largeSize--;

            if(num == large.top()) {
                pruneLarge();
            }
        }

        balance();
    }

    double getMed(int k) {

        if(k % 2 == 1) {
            return small.top();
        }

        return ((double)small.top() + large.top()) / 2.0;
    }

    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> ans;

        for(int i=0;i<k;i++)
        {
            addNum(nums[i]);
        }
        ans.push_back(getMed(k));

        for(int i=k;i<nums.size();i++)
        {
            addNum(nums[i]);
            removeNum(nums[i-k]);
            ans.push_back(getMed(k));
        }
        return ans;
    }
};