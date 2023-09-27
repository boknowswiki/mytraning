# stack
# time O(n)
# space O(1)

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        # Find size = length of decoded string
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1


# hit memory limitation

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        if k == 0:
            return "" if not s else s[0]
        
        st = ""

        for c in s:
            #print(f"c is {c}, st {st}")
            if not c.isdigit():
                st += c
            else:
                cnt = int(c)-1
                
                cur_s = st
                #print(f"cnt {cnt}, cur_s {cur_s}")
                while cnt:
                    st += cur_s
                    cnt -= 1
            if len(st) >= k:
                break

        #print(f"st {st}")
        return st[k-1]
