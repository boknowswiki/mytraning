#!/usr/bin/python -t

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def __init__(self):
        self.operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }

    def evalRPN(self, tokens):
        if not tokens:
            return 0

        stack = []

        for token in tokens:
            if token in self.operators:
                stack.append(self.operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[0]

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = {'+', '-', '*', '/'}
        st = []
        for token in tokens:
            if token in s:
                a = st.pop()
                b = st.pop()
                if token != '/':
                    ret = str(eval(b + token + a))
                else:
                    ret = str(int(float(b)/float(a)))
                st.append(ret)
            else:
                st.append(token)

        return int(st.pop())


if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.evalRPN(['0', '3', '/'])))
    print('%s\n' % (s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])))



class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for token in tokens:
            if token in "+-*/":
                a = st.pop()
                b = st.pop()
                if token == "+":
                    st.append(a+b)
                if token == "-":
                    st.append(b-a)
                if token == "*":
                    st.append(a*b)
                if token == "/":
                    st.append(int(float(b)/float(a)))
            else:
                st.append(int(token))

        return st.pop()


