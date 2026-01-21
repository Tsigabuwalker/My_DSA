class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_words = []
            line_len = 0

            # Greedy word packing
            while i < n and line_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1

            spaces_needed = maxWidth - line_len
            gaps = len(line_words) - 1

            # Last line or single word → left-justified
            if i == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                space, extra = divmod(spaces_needed, gaps)
                line = []

                for idx in range(gaps):
                    line.append(line_words[idx])
                    line.append(" " * (space + (1 if idx < extra else 0)))

                line.append(line_words[-1])
                line = "".join(line)

            res.append(line)

        return res
