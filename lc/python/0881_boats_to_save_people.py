
# sort and two pointers
# time O(nlogn)
# space O(logn)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

# sort and two pointers
# Time Limit Exceeded

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if max(people) > limit:
            return -1

        ret = 0
        v = set()
        people.sort()

        def find_people(index):
            nonlocal v, people, limit

            l = index
            r = n-1

            while l < r:
                if l in v:
                    l += 1
                    continue
                if r in v:
                    r -= 1
                    continue

                w = people[l] + people[r]
                if w <= limit:
                    v.add(l)
                    v.add(r)
                    return
                else:
                    r -= 1

            v.add(l)
            return

        for i in range(n):
            if i not in v:
                find_people(i)
                ret += 1

        return ret
