# bit
# time O(1)
# space O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        
        for _ in range(32):
            ret = (ret << 1) + (n&1)
            n >>= 1
            
        return ret
