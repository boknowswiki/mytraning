# sort
# time O(nlogn)
# space O(n)
# refer solution: https://leetcode.com/problems/put-marbles-in-bags/solutions/3734243/explain-partition-c-python-greedy-sort-vs-priority-queue/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        if n<=2 or n==k:
            return 0
        partition=[0]*(n-1)
        for i in range(n-1):
            partition[i]=weights[i]+weights[i+1]

        print(f"before part {partition}")
        partition.sort()

        print(f"after part {partition}")

        maxP=sum(partition[n-k:]) #without weights[0]+weights[n-1]
        minP=sum(partition[:k-1])
        return maxP-minP

# heap
# time O(nlogk)
# space O(n)

class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        int n=weights.size();
        if (n<=2) return 0;

        priority_queue<int> maxHeap;
        priority_queue<int, vector<int>, greater<int> > minHeap;
        long long maxP=0, minP=0;
        for (int i=0; i<k-1; i++){
            int partition=weights[i]+weights[i+1];
            maxP+=partition;
            maxHeap.push(partition);
            minHeap.push(partition);
        }
        minP=maxP; 

        //without weights[0]+weights[n-1]
        for(int i=k-1; i<n-1; i++){
            int partition=weights[i]+weights[i+1];
            maxHeap.push(partition);
            minP+=partition-maxHeap.top();
            maxHeap.pop();
            minHeap.push(partition);
            maxP+=partition-minHeap.top();
            minHeap.pop();
        }
        return maxP-minP;
    }
};
