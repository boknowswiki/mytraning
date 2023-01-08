# hash map and dfs
# time O(4^n*n)

#Time complexity: O(4N⋅N)O(4^N \cdot N)O(4 
#N
# ⋅N), where NNN is the length of digits. Note that 444 in this expression is referring to the maximum value length in the hash map, and not to the length of the input.

#The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to NNN to build the combination. This problem can be generalized to a scenario where numbers correspond with up to MMM digits, in which case the time complexity would be O(MN⋅N)O(M^N \cdot N)O(M 
#N
# ⋅N). For the problem constraints, we're given, M=4M = 4M=4, because of digits 7 and 9 having 4 letters each.

# space O(n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0: 
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations
