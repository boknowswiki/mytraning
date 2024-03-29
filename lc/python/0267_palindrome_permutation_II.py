# hash map and backtracking

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counts = collections.Counter(s)
        ret = []

        def dfs(cur="", counts=counts):
            nonlocal ret
            if len(cur) == len(s):
                ret.append(cur)
                return
            
            if not cur and len(s) % 2:
                for key in counts:
                    counts[key] -= 1
                    dfs(key, counts)
                    counts[key] += 1
            else:
                for key, cnt in counts.items():
                    if cnt >= 2:
                        counts[key] -= 2
                        dfs(key+cur+key, counts)
                        counts[key] += 2

            return

        dfs()

        return ret

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
