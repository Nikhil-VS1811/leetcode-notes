class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char,int>freq;
        for(char ch:s)
        {
            freq[ch]++;
        }

        priority_queue<pair<int,char>>maxheap;

        for(auto &entry:freq)
        {
            maxheap.push({entry.second,entry.first});
        }

        string ans="";

        int prevFreq=0;
        char prevChar='#';

        while(!maxheap.empty())
        {
            auto top=maxheap.top();
            maxheap.pop();

            int currFreq=top.first;
            char currChar=top.second;

            ans+=currChar;
            currFreq--;

            if(prevFreq>0)
            {
                maxheap.push({prevFreq,prevChar});
            }

            prevFreq=currFreq;
            prevChar=currChar;
        }

        if(s.length()!=ans.length()) return "";
        return ans;
    }
};