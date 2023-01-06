# hash map, string
# time O(n)
# space O(n)

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return False

        chars = dict()
        for c in s:
            chars[c] = chars.get(c, 0) + 1

        has_odd = False

        for _, n in chars.items():
            if n % 2 == 1 and has_odd:
                return False
            elif n%2 == 1 and not has_odd:
                has_odd = True

        return True
      
public class Solution {
    public boolean canPermutePalindrome(String s) {
        Set < Character > set = new HashSet < > ();
        for (int i = 0; i < s.length(); i++) {
            if (!set.add(s.charAt(i)))
                set.remove(s.charAt(i));
        }
        return set.size() <= 1;
    }
}
