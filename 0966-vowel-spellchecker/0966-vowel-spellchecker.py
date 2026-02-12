class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = set('aeiou')

        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact_words = set(wordlist)
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            low = word.lower()
            if low not in case_map:
                case_map[low] = word
            dv = devowel(word)
            if dv not in vowel_map:
                vowel_map[dv] = word

        answer = []
        for query in queries:
            if query in exact_words:
                answer.append(query)
            elif query.lower() in case_map:
                answer.append(case_map[query.lower()])
            elif devowel(query) in vowel_map:
                answer.append(vowel_map[devowel(query)])
            else:
                answer.append("")
        return answer
