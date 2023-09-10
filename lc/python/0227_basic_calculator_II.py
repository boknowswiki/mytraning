# stack, string

# time O(n)
# space O(1)

class Solution {
    public int calculate(String s) {
        if (s == null || s.isEmpty()) return 0;
        int length = s.length();
        int currentNumber = 0, lastNumber = 0, result = 0;
        char operation = '+';
        for (int i = 0; i < length; i++) {
            char currentChar = s.charAt(i);
            if (Character.isDigit(currentChar)) {
                currentNumber = (currentNumber * 10) + (currentChar - '0');
            }
            if (!Character.isDigit(currentChar) && !Character.isWhitespace(currentChar) || i == length - 1) {
                if (operation == '+' || operation == '-') {
                    result += lastNumber;
                    lastNumber = (operation == '+') ? currentNumber : -currentNumber;
                } else if (operation == '*') {
                    lastNumber = lastNumber * currentNumber;
                } else if (operation == '/') {
                    lastNumber = lastNumber / currentNumber;
                }
                operation = currentChar;
                currentNumber = 0;
            }
        }
        result += lastNumber;
        return result;
    }
}

# time O(n)
# space O(n)

class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        st = []
        ret = 0
        cur = 0
        op = "+"

        for i in range(n):
            cur_c = s[i]
            if cur_c.isdigit():
                cur = cur*10 + int(cur_c)
            if (not cur_c.isdigit()) and (cur_c != " ") or (i == n-1):
                if op == "-":
                    st.append(-cur)
                elif op == "+":
                    st.append(cur)
                elif op == "*":
                    st.append(st.pop()*cur)
                elif op == "/":
                    st.append(st.pop()//cur)
                
                op = cur_c
                cur = 0

        while st:
            ret += st.pop()

        return ret
        
