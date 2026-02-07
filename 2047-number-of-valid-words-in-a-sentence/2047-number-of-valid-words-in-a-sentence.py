class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split()
        valid_count = 0

        for token in tokens:
            # Rule 1: token should not contain digits
            if any(char.isdigit() for char in token):
                continue

            # Rule 2: hyphen rules
            hyphen_count = token.count('-')
            if hyphen_count > 1:
                continue
            if hyphen_count == 1:
                hyphen_index = token.index('-')
                # Hyphen cannot be at start or end
                if hyphen_index == 0 or hyphen_index == len(token) - 1:
                    continue
                # Hyphen must be surrounded by letters
                if not (token[hyphen_index - 1].isalpha() and token[hyphen_index + 1].isalpha()):
                    continue

            # Rule 3: punctuation rules
            punctuation = ['!', '.', ',']
            punct_count = sum(token.count(p) for p in punctuation)
            if punct_count > 1:
                continue
            if punct_count == 1:
                # Punctuation must be at the end
                if token[-1] not in punctuation:
                    continue

            # If all rules passed, it's valid
            valid_count += 1

        return valid_count
