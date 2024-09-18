import unittest
from mobius_linked_list import MobiusLinkedList

class TestMobiusLinkedList(unittest.TestCase):
    def test_append_and_length(self):
        mlist = MobiusLinkedList()
        self.assertEqual(mlist.length(), 0)
        mlist.append('A')
        self.assertEqual(mlist.length(), 1)
        mlist.append('B')
        self.assertEqual(mlist.length(), 2)

    def test_traverse_orientation(self):
        mlist = MobiusLinkedList()
        mlist.append('A')
        mlist.append('B')
        mlist.append('C')
        orientations = []
        mlist.traverse(cycles=2)
        # Here you can capture the output and assert the orientations

if __name__ == '__main__':
    unittest.main()
