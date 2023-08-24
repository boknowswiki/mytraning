# hash table
# time O(n)
# space O(n)

import collections

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s1, s2 = dict(), collections.defaultdict(list)

        ret = sys.maxsize

        for i, l in enumerate(list1):
            if l not in s1:
                s1[l] = i

        for i, l in enumerate(list2):
            if l not in s2 and l in s1:
                s2[i+s1[l]].append(l)

        for v in s2:
            ret = min(ret, v)

        return s2[ret]

  public class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap < String, Integer > map = new HashMap < String, Integer > ();
        for (int i = 0; i < list1.length; i++)
            map.put(list1[i], i);
        List < String > res = new ArrayList < > ();
        int min_sum = Integer.MAX_VALUE, sum;
        for (int j = 0; j < list2.length && j <= min_sum; j++) {
            if (map.containsKey(list2[j])) {
                sum = j + map.get(list2[j]);
                if (sum < min_sum) {
                    res.clear();
                    res.add(list2[j]);
                    min_sum = sum;
                } else if (sum == min_sum)
                    res.add(list2[j]);
            }
        }
        return res.toArray(new String[res.size()]);
    }
}
