import unittest

from src.sorting import heap_sort, merge_sort, quick_sort
from src.graphs import bfs, dfs, dijkstra
from src.dp import coin_change_min, knapsack_01, lis_length
from src.structures import SegmentTree, UnionFind
from src.pathfinding import astar


class TestSorting(unittest.TestCase):
    def test_sorts(self):
        raw = [5, 1, 4, 2, 8, 0, 3]
        expected = sorted(raw)
        self.assertEqual(merge_sort(raw), expected)
        self.assertEqual(quick_sort(raw), expected)
        self.assertEqual(heap_sort(raw), expected)


class TestGraphs(unittest.TestCase):
    def test_bfs_dfs(self):
        g = {0: [1, 2], 1: [3], 2: [], 3: []}
        self.assertEqual(bfs(g, 0), [0, 1, 2, 3])
        self.assertEqual(dfs(g, 0), [0, 1, 3, 2])

    def test_dijkstra(self):
        g = {0: [(1, 1), (2, 4)], 1: [(2, 1)], 2: []}
        self.assertEqual(dijkstra(g, 0)[2], 2)


class TestDP(unittest.TestCase):
    def test_knapsack(self):
        self.assertEqual(knapsack_01([1, 2, 3], [6, 10, 12], 5), 22)

    def test_lis(self):
        self.assertEqual(lis_length([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_coins(self):
        self.assertEqual(coin_change_min([1, 2, 5], 11), 3)
        self.assertEqual(coin_change_min([2], 3), -1)


class TestStructures(unittest.TestCase):
    def test_uf(self):
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertFalse(uf.union(0, 1))
        self.assertEqual(uf.find(0), uf.find(1))

    def test_segtree(self):
        st = SegmentTree([1, 2, 3, 4])
        self.assertEqual(st.query(0, 3), 10)
        st.update(1, 10)
        self.assertEqual(st.query(0, 3), 18)


class TestPathfinding(unittest.TestCase):
    def test_astar(self):
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
        ]
        path = astar(grid, (0, 0), (2, 0))
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 0))


if __name__ == "__main__":
    unittest.main()
