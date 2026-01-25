class Solution:
    def compress(self, chars):
        write = 0
        anchor = 0
        n = len(chars)

        for read in range(n):
            # If end of group OR end of array
            if read + 1 == n or chars[read] != chars[read + 1]:
                chars[write] = chars[anchor]   # write the character
                write += 1
                if read > anchor:  # group length > 1
                    count = str(read - anchor + 1)
                    for c in count:
                        chars[write] = c
                        write += 1
                anchor = read + 1  # move anchor to next group

        return write
