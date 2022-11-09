# stack
# time O(n)
# space O(n)

class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        ret = 1
        while self.stack and self.stack[-1][0] <= price:
            ret += self.stack.pop()[1]
            
        self.stack.append([price, ret])
        
        return ret
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
