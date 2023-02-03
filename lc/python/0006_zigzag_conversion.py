# string
# time O(n)
# space O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if n < 2:
            return s

        if numRows == 1:
            return s

        ret = [[] for _ in range(numRows)]
        #print(f"ret {ret}")
        cur_row = 0
        nxt_row = 1
        for i in range(n):
            if cur_row == 0:
                nxt_row = 1
            if cur_row == numRows-1:
                nxt_row = -1

            #print(f"cur_row {cur_row}, i {s[i]}")
            ret[cur_row].append(s[i])
            cur_row += nxt_row

        ret_str = ""
        for i in range(numRows):
            ret_str += "".join(ret[i])

        return ret_str
      
      
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        answer = []
        n = len(s)
        chars_in_section = 2 * (numRows - 1)

        for curr_row in range(numRows):
            index = curr_row
            while index < n:
                answer.append(s[index])

                # If curr_row is not the first or last row,
                # then we have to add one more character of current section.
                if curr_row != 0 and curr_row != numRows - 1:
                    chars_in_between = chars_in_section - 2 * curr_row
                    second_index = index + chars_in_between
                    
                    if second_index < n:
                        answer.append(s[second_index])
                # Jump to same row's first character of next section.
                index += chars_in_section
                
        return "".join(answer)
