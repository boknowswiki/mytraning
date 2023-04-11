# stack
# time O(n)
# space O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            #print(f"c {c}, st {st}")
            if c == "*" and len(st) > 0:
                st.pop()
            else:
                st.append(c)

        return "".join(st)
      
 # two pointers solution

class Solution {
    public String removeStars(String s) {
        char[] ch = new char[s.length()];
        int j = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '*') {
                j--;
            } else {
                ch[j++] = c;
            }
        }

        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < j; i++) {
            answer.append(ch[i]);
        }

        return answer.toString();
    }
}
