#!/usr/bin/python -t

#Build a dynamic programming array bottom up from 1 to N.
#For each index i, find all factors of j that divide i evenly, and see if we can guarantee a win. (That is, see if there exists dp[i-j] that is False) If so, set it to true.
#Finally, return dp[N].

#dp[i] = ~dp[i-j] for j from 1 to i//2+1

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        #dp = [False] * (N+1)
        dp = [False for i in range(N+1)]
        
        for i in range(1, N+1):
            for j in range(1, i//2+1):
                if i % j == 0 and (not dp[i-j]):
                    dp[i] = True
                    break
                    
        return dp[N]


def divisorGame(self, N):
        count = 0   #Determine who is playing: count is even, when Alice is playing, and vice versa.
        x = 1   #Mathematically, it is safe to select 1, because it guarantees N % 1 = 0.
        while N > 1:
            if N % x != 0:   #rule of the game is not satisfied so the playing person is the loser
                if count % 2 == 0: return False   #count is even, meaning Alice is playing, so she loses.
                else: return True   #count is odd, meaning Bob is playing, so Alice wins.
            else:   
                N = N - x  #The game continues by replacing N with the new value.  
                count += 1 #Change the player
            if N == 1:  #The rest just checks if N = x to determine the winner.
                if count % 2 == 0: return False
                else: return True  

#Now that you looked at the flow of the game, you might guess the above code can be reduced furhter more, because we always get N % x = 0, since x =1:

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        count, x = 0, 1
        
        while N > 1:
            N, count = N-x, count+1
            
            if N == 1:
                if count%2 == 0:
                    return False
                else:
                    return True

if __name__ =='__main__':
    s = Solution()
    print('answer is %r' % s.divisorGame(2))
