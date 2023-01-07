# hash map

class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.index = 0
        self.cnt = 0
        self.c = ""
 
    def next(self) -> str:
        if not self.hasNext():
            return " "
        if self.cnt > 0:
            self.cnt -= 1
            return self.c
        self.c = self.s[self.index]
        self.index += 1
        start = self.index
        while self.index < len(self.s) and self.s[self.index].isnumeric():
            self.index += 1

        self.cnt = int(self.s[start:self.index])
        self.cnt -= 1
        print(f"cnt {self.cnt}, c {self.c}")
        return self.c
        

    def hasNext(self) -> bool:
        return self.index < len(self.s) or self.cnt > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()


public class StringIterator {
    String res;
    int ptr = 0, num = 0;
    char ch = ' ';
    public StringIterator(String s) {
        res = s;
    }
    public char next() {
        if (!hasNext())
            return ' ';
        if (num == 0) {
            ch = res.charAt(ptr++);
            while (ptr < res.length() && Character.isDigit(res.charAt(ptr))) {
                num = num * 10 + res.charAt(ptr++) - '0';
            }
        }
        num--;
        return ch;
    }
    public boolean hasNext() {
        return ptr != res.length() || num != 0;
    }
}
