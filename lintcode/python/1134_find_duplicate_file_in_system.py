#!/usr/bin/python -t

# hash table


import collections

class Solution:
    """
    @param paths: a list of string
    @return: all the groups of duplicate files in the file system in terms of their paths
    """
    def findDuplicate(self, paths):
        # Write your code here
        d = collections.defaultdict(list)
        #ret = []
        
        for p in paths:
            p_list = p.split(" ")
            root_dir = p_list[0]
            for f in p_list[1:]:
                f_name, f_content = f.split("(")
                d[f_content].append(root_dir+ "/" + f_name)
                
        #print d
        #for k in d:
        #    ret.append(d[k])
            
        #print ret

        return [d[k] for k in d if len(d[k]) > 1]
        
        
