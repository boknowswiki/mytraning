# two pointers

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, n = 0, "0"
        for c in abbr:
            if c.isdigit():
                if n == c:
                    return False
                n += c
            else:
                i += int(n)
                if i>=len(word) or word[i] != c:
                    return False
                i += 1
                n = '0'
                
        return i+int(n)== len(word)
