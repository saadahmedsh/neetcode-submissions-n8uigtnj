from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}


        for child, parent in prerequisites:
            indegree[child] += 1
            graph[parent].append(child)

        q = deque()

        for child, degree in indegree.items():
            if degree == 0:
                q.append(child)

        count = 0
        output = []

        while q:
            node = q.popleft()
            output.append(node)
            count += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if count == numCourses:
            return output

        return []            
            

