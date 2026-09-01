import heapq


def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0]) if grid else 0

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_heap = []
    heapq.heappush(open_heap, (0, 0, start))
    came_from = {start: None}
    g_score = {start: 0}
    counter = 0

    while open_heap:
        _, _, current = heapq.heappop(open_heap)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return list(reversed(path))

        r, c = current
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                continue
            ng = g_score[current] + 1
            nxt = (nr, nc)
            if ng < g_score.get(nxt, 10**9):
                g_score[nxt] = ng
                came_from[nxt] = current
                counter += 1
                f = ng + heuristic(nxt, goal)
                heapq.heappush(open_heap, (f, counter, nxt))
    return None
