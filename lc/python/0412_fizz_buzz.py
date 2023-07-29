# array
# time O(n)
# space O(1)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []

        for i in range(1, n+1):
            if (i % 3 == 0) and (i%5 == 0):
                ret.append("FizzBuzz")
            elif (i%3 == 0):
                ret.append("Fizz")
            elif (i%5 == 0):
                ret.append("Buzz")
            else:
                ret.append(str(i))

        return ret

  class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # ans list
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            num_ans_str = ""

            if divisible_by_3:
                # Divides by 3
                num_ans_str += "Fizz"
            if divisible_by_5:
                # Divides by 5
                num_ans_str += "Buzz"
            if not num_ans_str:
                # Not divisible by 3 or 5
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)  

        return ans
