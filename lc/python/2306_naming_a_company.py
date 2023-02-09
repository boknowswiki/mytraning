# hash map

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Group idea by their initials.
        initial_groups = [set() for _ in range(26)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])
        
        answer = 0
        # Calculate number of valid names from every pair of groups.
        for i in range(25):
            for j in range(i + 1, 26):
                # Get the number of mutual suffixes.
                num_of_mutual = len(initial_groups[i] & initial_groups[j]) 
                
                # Valid names are only from distinct suffixes in both groups.
                # Since we can swap a with b and swap b with a to create two valid names, multiple answer by 2.
                answer += 2 * (len(initial_groups[i]) - num_of_mutual) * (len(initial_groups[j]) - num_of_mutual)
                
        return answer


# Time Limit Exceeded
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideas_set = set(ideas)

        ret = 0

        def is_valid(a, b):
            new_a = a[0]+b[1:]
            new_b = b[0] + a[1:]
            return new_a not in ideas_set and new_b not in ideas_set

        for first in ideas_set:
            for second in ideas_set:
                if second == first:
                    continue

                if is_valid(first, second):
                    ret += 1

        return ret
