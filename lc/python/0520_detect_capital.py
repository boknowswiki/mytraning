# string
# time O(n)
# space O(1)

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        has_capitcal = False
        has_lower = False

        if word[0].isupper():
            for i in range(1, len(word)):
                if word[i].isupper():
                    has_capitcal = True
                else:
                    has_lower = True
                if has_capitcal and has_lower:
                    return False
        else:
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False

        return True
