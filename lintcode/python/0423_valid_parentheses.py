#!/usr/bin/python -t

# stack and string

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        n = len(s)
        if n < 2:
            return False

        st = []
        for ss in s:
            if ss == "(" or ss == "[" or ss == "{":
                st.append(ss)
            if ss == ")":
                if len(st) == 0 or st[-1] != "(":
                    return False
                st.pop()
            if ss == "]":
                if len(st) == 0 or st[-1] != "[":
                    return False
                st.pop()
            if ss == "}":
                if len(st) == 0 or st[-1] != "{":
                    return False
                st.pop()

        return len(st) == 0

        
if __name__ == '__main__':
    s = Solution()
    a = "([)]"
    #a = "()[]{}"
    a = "()"
    print(s.isValidParentheses(a))