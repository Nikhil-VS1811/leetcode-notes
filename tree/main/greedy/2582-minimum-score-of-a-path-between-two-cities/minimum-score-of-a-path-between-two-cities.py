class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        res = float("inf")
        visit = [False] * (n + 1)
        q = deque([1])
        visit[1] = True

        while q:
            node = q.popleft()
            for nei, dist in adj[node]:
                res = min(res, dist)
                if not visit[nei]:
                    visit[nei] = True
                    q.append(nei)

        return res  