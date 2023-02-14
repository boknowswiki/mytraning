# string
# time O(n)
# space O(n)

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        if a_len == 0:
            return b
        if b_len == 0:
            return a

        new_a = a[::-1]
        new_b = b[::-1]

        ret = []
        c = 0
        cur = 0

        while cur < max(a_len, b_len):
            val_a = ord(new_a[cur]) - ord("0") if cur < a_len else 0
            val_b = ord(new_b[cur]) - ord("0") if cur < b_len else 0

            val = (val_a + val_b + c)%2
            c =  (val_a + val_b + c)//2
            ret.append(str(val))
            cur += 1

        if c:
            ret.append(str(c))

        #print(f"ret {ret}")
        return "".join(ret[::-1])
