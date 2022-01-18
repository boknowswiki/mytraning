#!/usr/bin/python -t

# union find and dp

# 考点:
# 
# dp
# 并查集
# 题解：
# 本题强调相似的定义和性质，若相似具有传递性，就可以利用并查集维护相似的字符串。寻找最长公共子序列即为经典的dp问题。
# 此处选择使用map将字符串与数字映射，方便判断以及并查集维护。
# 
#  最长公共子序列状态转移方程：
#    dp[i][j]=0  (i=0||j=0)
# dp[i][j]=max(dp[i-1][j],dp[i][j-1])  (a[i]!=b[j])
# dp[i][j]=dp[i-1][j-1]+1 (a[i]=b[j])

class Node :
    def __init__(self) :
        self.fa=[]
        for i in range(6200) :
             self.fa.append(i)
    def find(self,x) :
        if self.fa[x]==x :
            return x
        else :
            self.fa[x]=self.find(self.fa[x])
            return self.fa[x]
    def unity(self,x,y) :
        x=self.find(x)
        y=self.find(y)
        self.fa[x]=y
class Solution:
    """
    @param words1: the words in paper1
    @param words2: the words in paper2
    @param pairs: the similar words pair
    @return: the similarity of the two papers
    """
    def getSimilarity(self, words1, words2, pairs):
        # Write your code here
        ans=Node()
        cnt=0
        a=[]
        b=[]
        s={}
        a.append(0)
        b.append(0)
        for i in pairs:
            if s.__contains__(i[0])==0 :
                cnt+=1
                s[i[0]]=cnt
            if s.__contains__(i[1])==0 :
                cnt+=1
                s[i[1]]=cnt
            ans.unity(s[i[0]],s[i[1]])
        for i in words1 :
            if s.__contains__(i)==0:
                cnt+=1
                s[i]=cnt
            a.append(s[i])
        for i in words2 :
            if s.__contains__(i)==0 :
                cnt+=1
                s[i]=cnt
            b.append(s[i])
        dp=[[0]*1000 for i in range(1000)]
        for i in range(1,len(words1)+1) :
            for j in range(1,len(words2)+1) :
                x=ans.find(a[i])
                y=ans.find(b[j])
                if x==y :
                    dp[i][j]=dp[i-1][j-1]+1
                else :
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        res=dp[len(words1)][len(words2)]*2.0/(len(words1)+len(words2))
        return res
