#!/usr/bin/python -t

class inter:
    def __init__(self):
        self.k = []
        self.v = []

    def form(self, l):
        if l == None:
            return

        #print l
        for ele in l:
            level = []
            self.dfs(ele, level, '')
            self.v.append(list(level))

        #print self.k
        #print self.v
        return

    def dfs(self, ele, level, pre_key):
        if type(ele) == dict:
            for key in ele:
                #print pre_key, key
                if len(pre_key) != 0:
                    save_key = pre_key + '.' + key
                else:
                    save_key = key
                self.k.append(save_key)
                self.dfs(ele[key], level, save_key)
        elif type(ele) == list:
            for e in ele:
                self.dfs(e, level, pre_key)
        elif type(ele) == str:
            level.append(ele)

        return

if __name__ == '__main__':
    s = [
            {'f1': 'v1',
             'f2': [{'f3':'v2'}, 'v3'],
             'f3': {'f4': 'v4', 'f5':'v5', 'f6': [{'f7':'v7'}]}},
            {'f1': 'a1',
             'f2': [{'f3':'a2'}, 'a3'],
             'f3': {'f4': 'a4', 'f5': 'a5', 'f6': [{'f7':'a7'}]}},
        ]

    # expect
    # f1, f2, f2.f3, f3, f3.f4, f3.f5, f3.f6, f3.f6.f7
    # v1, v2, v3, v4, v5, v7
    # a1, a2, a3, a4, a5, a7
 
    ss = inter()
    #print "answer is %s" % ss.form(s)
    ss.form(s)
    print ss.k
    print ss.v
