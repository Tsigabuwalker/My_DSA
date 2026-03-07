class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        def f(s: str) -> int:
            return s.count(min(s))
        
        word_freqs = sorted(f(w) for w in words)
        
        answer = []
        for q in queries:
            q_freq = f(q)
            left, right = 0, len(word_freqs)
            while left < right:
                mid = (left + right) // 2
                if word_freqs[mid] <= q_freq:
                    left = mid + 1
                else:
                    right = mid
            answer.append(len(word_freqs) - left)
        
        return answer