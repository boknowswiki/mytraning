# hash map

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = collections.defaultdict(set)

        for word in dictionary:
            self.d[self.get_abbre(word)].add(word)

        print(f"d {self.d}")
        return

    def isUnique(self, word: str) -> bool:
        word_abbre = self.get_abbre(word)
        return len(self.d[word_abbre]) == 0 or (len(self.d[word_abbre]) == 1 and word in self.d[word_abbre])
    def get_abbre(self, word):
        if len(word) <= 2:
            return word
        word_list = list(word)
        return word[0] + str(len(word)-2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

# faster one

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviation_words = {}
        for word in dictionary:
            abbreviation = (word[0], word[-1], len(word))
            abbreviation_word = self.abbreviation_words.get(abbreviation)

            # if abbreviation_word is not None and word != abbreviation_word:
            if abbreviation_word not in (None, word):
                self.abbreviation_words[abbreviation] = ""
            else:
                self.abbreviation_words[abbreviation] = word


    def isUnique(self, word: str) -> bool:
        abbreviation = (word[0], word[-1], len(word))
        abbreviation_word = self.abbreviation_words.get(abbreviation)
        unique = abbreviation_word is None or abbreviation_word == word
        return unique
