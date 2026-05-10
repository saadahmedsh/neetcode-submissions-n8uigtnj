class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for word in words for c in word}


        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            n1, n2 = len(w1), len(w2)
            min_len = min(n1, n2)

            if n1 > n2 and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    char_out = w1[j]
                    char_in = w2[j]
                    if char_in not in adj[char_out]:
                        adj[char_out].add(char_in)
                        in_degree[char_in] += 1
                
                    break

        q = deque([c for c in in_degree if in_degree[c] == 0])
        result = []

        while q:
            curr_char = q.popleft()
            result.append(curr_char)

            for nei in adj[curr_char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        if len(result) != len(in_degree):
            return ""
        
        return "".join(result)
        

                