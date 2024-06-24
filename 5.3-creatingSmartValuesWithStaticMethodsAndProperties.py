class TextPreprocessing:

    def remove_apostrophe(self, word):
        return word.replace("'", "")

    @staticmethod
    def remove_spaces(word: str):
        return word.replace(" ", "")

preprocessor = TextPreprocessing()
print(preprocessor.remove_apostrophe("Rudy's"))
# TextPreprocessing.remove_apostrophe("Rudy's") Error

print(TextPreprocessing.remove_spaces("Mary had a little lamb"))


class NumberStore:
    number = 0

    def __init__(self, n):
        self.number = n

    def get_number(self):
        print(f"Number stored: {self.number}")

    @property
    def decorated_number(self):
        return f"Number stored: {self.number}"

ns = NumberStore(10)
print(ns.decorated_number)
