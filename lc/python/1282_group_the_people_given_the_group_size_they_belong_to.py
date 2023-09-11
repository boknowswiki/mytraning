# array, hash table
# time O(n)
# space O(n)

import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        if n == 0:
            return [[]]

        ret = collections.defaultdict(list)

        for g in groupSizes:
            if g not in ret:
                ret[g].append([])

        # print(f"ret {ret}")

        for i in range(n):
            g = groupSizes[i]
            if len(ret[g][-1]) == g:
                ret[g].append([i])
            else:
                ret[g][-1].append(i)

        ans = []
        for _, v in ret.items():
            for x in v:
                ans.append(x)

        return ans

  class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        List<List<Integer>> ans = new ArrayList<>();
        
        // A map from group size to the list of indices that are there in the group.
        Map<Integer, List<Integer>> szToGroup = new HashMap<>();
        for (int i = 0; i < groupSizes.length; i++) {
            if (!szToGroup.containsKey(groupSizes[i])) {
                szToGroup.put(groupSizes[i], new ArrayList<>());
            }
            
            List<Integer> group = szToGroup.get(groupSizes[i]);
            group.add(i);

            // When the list size equals the group size, empty it and store it in the answer.
            if (group.size() == groupSizes[i]) {
                ans.add(group);
                szToGroup.remove(groupSizes[i]);
            }
        }

        return ans;
    }
}
