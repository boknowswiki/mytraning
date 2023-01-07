# hash map
# time O(n)
# space O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True

        note_dict = dict()
        mag_dict = dict()

        for c in ransomNote:
            note_dict[c] = note_dict.get(c, 0)+1

        for c in magazine:
            mag_dict[c] = mag_dict.get(c, 0)+1

        for k in note_dict:
            if k not in mag_dict:
                return False
            if note_dict[k] > mag_dict[k]:
                return False

        return True
      
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
    letters = collections.Counter(magazine)
    
    # For each character, c, in the ransom note:
    for c in ransomNote:
        # If there are none of c left, return False.
        if letters[c] <= 0:
            return False
        # Remove one of c from the Counter.
        letters[c] -= 1
    # If we got this far, we can successfully build the note.
    return True
