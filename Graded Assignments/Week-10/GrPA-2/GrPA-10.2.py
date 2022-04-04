class StringManipulation:
    def __init__(self, words):
        self.words = words
    def total_words(self):
        return len(self.words)
    def count(self, some_word):
        n = 0
        for word in self.words:
            if word == some_word:
                n += 1
        return n
    def words_of_length(self, length):
        L = [ ]
        for word in self.words:
            if len(word) == length:
                L.append(word)
        return L
    def words_start_with(self, char):
        L = [ ]
        for word in self.words:
            if word[0] == char:
                L.append(word)
        return L
    def longest_word(self):
        maxword = self.words[0]
        for word in self.words:
            if len(word) > len(maxword):
                maxword = word
        return maxword
    def palindromes(self):
        L = [ ]
        for word in self.words:
            reverse = ''
            for char in word:
                reverse = char + reverse
            if word == reverse:
                L.append(word)
        return L
