#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param cpdomains: a list cpdomains of count-paired domains
    @return: a list of count-paired domains
    """
    def subdomainVisits(self, cpdomains):
        # Write your code here
        d = {}
        ret = []
        
        for ele in cpdomains:
            e = ele.split()
            visits = int(e[0])
            url = e[1]
            
            url_list = url.split('.')
            tmp = ""
            
            for i in range(len(url_list)-1, -1, -1):
                if tmp == "":
                    tmp = url_list[i]
                else:
                    tmp = url_list[i] + "." + tmp
                if tmp not in d:
                    d[tmp] = visits
                else:
                    d[tmp] += visits
                    
        #print d
        
        for k in d:
            ret.append(str(d[k]) + " " + k)
            
        return ret
        
        
