#!/usr/bin/python -t

# stack

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0 or n % 2 == 1:
            return False

        st = []
        open = {"(", "{", "["}
        mapping = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in open:
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                if mapping[c] != st[-1]:
                    return False
                st.pop()

        return len(st) == 0
    
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        d = {"(": ")", "[": "]", "{": "}"}

        for i in s:
            if i in d:
                st.append(i)
            elif not st or d[st.pop()] != i:
                return False

        return True if not st else False

