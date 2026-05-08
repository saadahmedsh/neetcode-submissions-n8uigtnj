from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)

        visit = set()
        q = deque()
        q.append((beginWord, 1))

        while q:
            curr_word, res = q.popleft()

            if curr_word == endWord:
                return res


            for j in range(len(curr_word)):
                pattern = curr_word[:j] + "*" + curr_word[j + 1:]
                for nei in adj[pattern]:
                    if nei not in visit:
                        q.append((nei, res + 1))
                        visit.add(nei)

        return 0


        
            




        