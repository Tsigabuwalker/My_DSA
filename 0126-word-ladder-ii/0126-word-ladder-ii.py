from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Graph to store adjacency for backtracking
        tree = defaultdict(list)
        found = False
        queue = deque([beginWord])
        visited = set([beginWord])

        while queue and not found:
            local_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet and newWord not in visited:
                            tree[newWord].append(word)
                            if newWord == endWord:
                                found = True
                            local_visited.add(newWord)
                            queue.append(newWord)
            visited.update(local_visited)

        # Backtracking to build paths
        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in tree[word]:
                backtrack(parent, path + [parent])

        if found:
            backtrack(endWord, [endWord])
        return res
