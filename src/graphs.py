import heapq
from collections import defaultdict, deque


def bfs(graph, start):
    seen = {start}
    order = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in graph.get(node, []):
            if nei not in seen:
                seen.add(nei)
                order.append(nei)
                q.append(nei)
    return order


def dfs(graph, start):
    seen = set()
    order = []

    def visit(node):
        seen.add(node)
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in seen:
                visit(nei)

    visit(start)
    return order


def dijkstra(graph, start):
    dist = defaultdict(lambda: float("inf"))
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dict(dist)
