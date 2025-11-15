from typing import List
from collections import deque

class Solution:
    # BFS
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList_set = set(wordList)
        queue = deque([(beginWord, 0)])
        while queue:
            word, step = queue.popleft()
            for i in range(len(word)):
                for j in range(26):
                    if word[i] == chr(97 + j):
                        continue
                    new_word = word[:i] + chr(97 + j) + word[i + 1:]
                    if new_word == endWord:
                        return step + 2
                    if new_word in wordList_set:
                        queue.append((new_word, step + 1))
                        wordList_set.remove(new_word)
        return 0