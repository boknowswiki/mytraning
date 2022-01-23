#!/usr/bin/python -t

# union find
# uf

# 强化班侯卫东老师的思路，用email做节点，集合的根节点返回账户名
# 注意，在得到正确的集合之后，需要用一个哈希表来记录由根节点账户到集合中所有email的映射，但由于账户可能重叠，所以这个哈希表的key不能是账户，可以是input的第几行
# 
# 二刷：修正了前面的答案里头别扭的思路，包括key不能是账户，union的方向之类的


import collections

class Solution:
    def __init__(self):
        self.father = {}

    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        if not accounts:
            return []

        for account in accounts:
            if not account or len(account) < 2:
                continue
            for email in account[1:]:
                self.father[email] = email

        for account in accounts:
            if not account or len(account) < 2:
                continue
            for i in range(2, len(account)):
                self.union(account[i-1], account[i])

        email_set = collections.defaultdict(set)
        email_to_acct = {}

        for account in accounts:
            if not account:
                continue

            name = account[0]
            for email in account[1:]:
                root_email = self.find(email)
                email_set[root_email].add(email)
                if root_email not in email_to_acct:
                    email_to_acct[root_email] = name

        ret = []

        for root_email in email_set:
            temp = [email_to_acct[root_email]] + sorted(list(email_set[root_email]))
            ret.append(temp)

        return ret

    def find(self, node):
        if node != self.father[node]:
            self.father[node] = self.find(self.father[node])

        return self.father[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

        return
