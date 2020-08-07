class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """
    def hIndex(self, citations):
        # write your code here
        n = len(citations)
        if n == 0:
            return 0
            
        citations.sort()
        
        for i in range(n):
            if citations[i] >= n-i:
                return n-i
                
        return 0
            
