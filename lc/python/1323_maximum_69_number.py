
# math
# time O(n)
# space O(1)

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Since we start with the lowest digit, initialize curr_digit = 0.
        curr_digit = 0
        index_first_six = -1
        num_copy = num
        
        # Check every digit of 'num_copy' from low to high.
        while num_copy:
            # If the current digit is '6', record it as the highest digit of 6.
            if num_copy % 10 == 6:
                index_first_six = curr_digit
            
            # Move on to the next digit.
            num_copy //= 10
            curr_digit += 1
        
        # If we don't find any digit of '6', return the original number,
        # otherwise, increment 'num' by the difference made by the first '6'.
        return num if index_first_six == -1 else num + 3 * 10 ** index_first_six

# math
# time O(n)
# space O(n)

class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))
        
        for i, cur in enumerate(num_list):
            if cur == "6":
                num_list[i] = "9"
                break
                
        return int("".join(num_list))
