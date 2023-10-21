import unittest
from zad4 import Tree

class TestTree(unittest.TestCase):
    
    def test_Init(self):
        tree = Tree(3)
        self.assertEqual(tree.nodeVal, 3)

    def test_AddNode(self):
        tree = Tree(3)
        tree.AddNode(2)
        self.assertAlmostEqual(1, len(tree.nodes))
        self.assertAlmostEqual(tree.nodes[0].nodeVal, 2)


if __name__ == '__main__':
    unittest.main()