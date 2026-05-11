/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int>allvalues;
        for(auto list:lists)
        {
            while(list!=nullptr)
            {
            allvalues.push_back(list->val);
            list=list->next;
            }
        }
        sort(allvalues.begin(),allvalues.end());

        ListNode* dummy=new ListNode(0);
        ListNode* curr=dummy;

        for(int val:allvalues)
        {
            curr->next=new ListNode(val);
            curr=curr->next;
        }
        return dummy->next;
    }
};