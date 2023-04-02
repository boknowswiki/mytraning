# sort, binary search
# time O((m+n)⋅logn)
# space O(m)

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ret = []
        m = len(spells)
        if m == 0:
            return ret

        n = len(potions)
        if n == 0:
            return ret

        # spells.sort()
        potions.sort()

        def find(num, target):
            #print(f"target {target}")
            nonlocal potions

            l = 0
            r = n-1

            while l + 1 < r:
                mid = (l+r)//2
                if num * potions[mid] < target:
                    l = mid
                else:
                    r = mid

            if num * potions[l] >= target:
                return l
            if num * potions[r] >= target:
                return r
            return -1

        for i in range(m):
            #print(f"spell {spells[i]}")
            index = find(spells[i], success)
            #print(f"index {index}")
            if index == -1:
                ret.append(0)
            else:
                ret.append(n-index)

        return ret
      
# sort and two pointer
# time O(nlogn+mlogm)
# space O(n+logm) or O(n+m)

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedSpells = [(spell, index) for index, spell in enumerate(spells)]

        # Sort the 'spells with index' and 'potions' array in increasing order.
        sortedSpells.sort()
        potions.sort()

        answer = [0] * len(spells)
        m = len(potions)
        potionIndex = m - 1
        
        # For each 'spell' find the respective 'minPotion' index.
        for spell, index in sortedSpells:
            while potionIndex >= 0 and (spell * potions[potionIndex]) >= success:
                potionIndex -= 1
            answer[index] = m - (potionIndex + 1)
        
        return answer
