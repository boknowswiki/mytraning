# bucket sort
# time O(n)
# space O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return s
    
        # Determine the frequency of each character.
        counts = collections.Counter(s)
        max_freq = max(counts.values())

        print(f"{counts}")
        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            #print(f"c {c}, i {i}")
            buckets[i].append(c)

        #print(f"buckets {buckets}")
        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)

        return "".join(string_builder)
