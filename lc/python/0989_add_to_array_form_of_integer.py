# math and array
# time O(n)
# space O(n)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        while k:
            k, a = divmod(k, 10)
            num = [a] + num
        return num

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        val = 0

        for n in num:
            val *= 10
            val += n

        val += k

        ret = []

        while val > 0:
            v = val%10
            val = val // 10
            ret.append(v)

        return ret[::-1]
