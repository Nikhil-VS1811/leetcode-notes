class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minDist = grid
        directions = [0, 1, 0, -1, 0]

        q = deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append(r * N + c)
                    minDist[r][c] = 0
                else:
                    minDist[r][c] = -1

        while q:
            node = q.popleft()
            r, c = divmod(node, N)
            for i in range(4):
                r2, c2 = r + directions[i], c + directions[i + 1]
                if 0 <= r2 < N and 0 <= c2 < N and minDist[r2][c2] == -1:
                    minDist[r2][c2] = minDist[r][c] + 1
                    q.append(r2 * N + c2)

        maxHeap = [(-minDist[0][0], 0)]
        safeFactor = [0] * (N * N)
        safeFactor[0] = minDist[0][0]

        while maxHeap:
            dist, node = heapq.heappop(maxHeap)
            dist = -dist
            r, c = divmod(node, N)
            if r == N - 1 and c == N - 1:
                return dist
            if safeFactor[node] > dist:
                continue

            for i in range(4):
                r2, c2 = r + directions[i], c + directions[i + 1]
                node2 = r2 * N + c2
                if 0 <= r2 < N and 0 <= c2 < N:
                    dist2 = min(dist, minDist[r2][c2])
                    if dist2 > safeFactor[node2]:
                        safeFactor[node2] = dist2
                        heapq.heappush(maxHeap, (-dist2, node2))

        return 0 