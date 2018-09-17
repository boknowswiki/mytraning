#!/usr/bin/python -t

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


