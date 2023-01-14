# hash map and backtracking

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        output = []
        
        def backtrack(curr='', counter=counter):
            if len(curr) == len(s):
                output.append(curr)
                
			# Start with each letter if length is odd
            if not curr and len(s) % 2:
                for key in counter:
                    counter[key] -= 1
                    backtrack(key, counter)
                    counter[key] += 1
					
            # Build palindrome around current string  
            else:
                for key, count in counter.items():
                    if count >= 2:
                        counter[key] -= 2
                        backtrack(key + curr + key, counter)
                        counter[key] += 2
        
        backtrack()
        return output
