#include <queue>

class KthLargest {

public:
    priority_queue<int, greater<int>> minHeap;
    int k;
public:
    KthLargest(int k, vector<int>& nums) {
            this->k = k;
            for(int num: nums){
                add(num);
            }    
    }
    
    int add(int val) {

        minHeap.push(val);
        if (minHeap.size() > k){
            minHeap.pop();
        }
        return minHeap.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */