#include <queue>
#include <cmath>
class Solution {
 
public:
    int lastStoneWeight(vector<int>& stones) {

            priority_queue<int> maxHeap(stones.begin(), stones.end());
            while(maxHeap.size() > 1){
                int val1 = maxHeap.top();
                maxHeap.pop();
                int val2 = maxHeap.top();
                maxHeap.pop();
                if (val1!=val2){
                int value = abs(val1 - val2);
                maxHeap.push(value);
                }
                
                }
            
            return maxHeap.empty() ? 0 : maxHeap.top();
    }

};