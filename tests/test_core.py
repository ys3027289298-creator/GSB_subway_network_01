import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_duplicate_node_rejected(self):
        state = core.new_game()
        self.assertTrue(core.add_node(state, 1))
        self.assertFalse(core.add_node(state, 1))

    def test_02_self_loop_rejected(self):
        state = core.new_game()
        core.add_node(state, 1)
        self.assertFalse(core.add_edge(state, 1, 1, 5))

    def test_03_negative_cost_rejected(self):
        state = core.new_game()
        core.add_node(state, 1)
        core.add_node(state, 2)
        self.assertFalse(core.add_edge(state, 1, 2, -1))

    def test_04_remove_node_cleans_edges(self):
        state = core.new_game()
        core.add_node(state, 1)
        core.add_node(state, 2)
        core.add_edge(state, 1, 2, 5)
        core.remove_node(state, 1)
        self.assertNotIn((1, 2), state["edges"])

    def test_05_path_exists(self):
        state = core.new_game()
        core.add_node(state, 1)
        core.add_node(state, 2)
        core.add_edge(state, 1, 2, 5)
        self.assertTrue(core.has_path(state, 1, 2))

    def test_06_path_cost(self):
        state = core.new_game()
        core.add_node(state, 1)
        core.add_node(state, 2)
        core.add_edge(state, 1, 2, 5)
        self.assertEqual(core.path_cost(state, 1, 2), 5)

    def test_07_shortest_path(self):
        state = core.new_game()
        core.add_node(state, 1)
        core.add_node(state, 2)
        core.add_edge(state, 1, 2, 5)
        self.assertEqual(core.shortest_path(state, 1, 2), 5)

    def test_08_nearest_other_node(self):
        state = core.new_game()
        core.add_node(state, 1)
        core.add_node(state, 2)
        self.assertEqual(core.nearest(state, 1), 2)

    def test_09_duplicate_edge_rejected(self):
        state = core.new_game()
        core.add_node(state, 1)
        core.add_node(state, 2)
        self.assertTrue(core.add_edge(state, 1, 2, 5))
        self.assertFalse(core.add_edge(state, 1, 2, 6))

    def test_10_load_preserves_id(self):
        state = core.new_game()
        state["next_id"] = 6
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["next_id"], 6)


if __name__ == "__main__":
    unittest.main()
