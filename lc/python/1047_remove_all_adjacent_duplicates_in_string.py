
# stack
# time O(n)
# space O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        
        s_list = list(s)
        #print(f"list {s_list}")
        stack = []
        
        for i in range(len(s_list)):
            #print(f"stack {stack}, i {s_list[i]}")
            if stack and stack[-1] == s_list[i]:
                stack.pop()
                continue
            stack.append(s_list[i])
            
        return "".join(stack)
