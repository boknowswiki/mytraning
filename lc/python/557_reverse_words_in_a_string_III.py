#!/usr/bin/python -t


class Solution {

    public String reverseWords(String s) {
        int lastSpaceIndex = -1;
        char[] chArray = s.toCharArray();
        int len = s.length();
        for (int strIndex = 0; strIndex <= len; strIndex++) {
            if (strIndex == len || chArray[strIndex] == ' ') {
                int startIndex = lastSpaceIndex + 1;
                int endIndex = strIndex - 1;
                while (startIndex < endIndex) {
                    char temp = chArray[startIndex];
                    chArray[startIndex] = chArray[endIndex];
                    chArray[endIndex] = temp;
                    startIndex++;
                    endIndex--;
                }
                lastSpaceIndex = strIndex;
            }
        }
        return new String(chArray);
    }

}

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        ret = ""
        pos = 0
        index = 0

        while index < n:
            while index < n and s[index] == " ":
                index += 1

            start = index

            while index < n and s[index] != " ":
                index += 1
        
            ret += s[start:index][::-1]
            if index < n:
                ret += " "

        if ret[-1] == " ":
            ret = ret[:len(ret)-1]


        return ret

# two pointers

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        l = 0
        ret = ""
        
        for r in range(n):
            if s[r] == " ":
                ret += s[l:r][::-1]
                #print (f"ret {ret}")
                ret += " "
                l = r+1
            elif r == n-1:
                ret += s[l:r+1][::-1]

        return ret

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        new_s = s[::-1]
        j = n
        ret = ''
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                j = i
            elif i == 0 or s[i-1] == ' ':
                if len(ret) != 0:
                    ret = ret + ' '
                ret = ret + s[i:j]
                
        ret = ret[::-1]
        return ret


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ret = ''
        i = 0
        
        while i < n:
            j = i
            while i < n and s[i] != ' ':
                i = i + 1
                
            if j < i:
                word = s[j:i]
                ret = ret + word[::-1] + ' '
                
            while i < n and s[i] == ' ':
                i = i + 1
            
        ret = ret[:-1]
        return ret
