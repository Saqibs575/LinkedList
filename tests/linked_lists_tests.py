from LinkedList.linked_list import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # Create an instance of LinkedList for testing
        self.ll = LinkedList()

    def test_empty_linked_list(self):
        self.assertEqual(len(self.ll), 0)
        with self.assertRaises(IndexError):
            self.ll[0]
        with self.assertRaises(IndexError):
            del self.ll[0]

    def test_insert_at_end(self):
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        self.assertEqual(len(self.ll), 3)
        self.assertEqual(self.ll[0], 10)
        self.assertEqual(self.ll[1], 20)
        self.assertEqual(self.ll[2], 30)

    def test_insert_at_beginning(self):
        self.ll.insert(10)
        self.ll.insert(20, 0)
        self.assertEqual(len(self.ll), 2)
        self.assertEqual(self.ll[0], 20)
        self.assertEqual(self.ll[1], 10)

    def test_insert_at_middle(self):
        self.ll.insert(10)
        self.ll.insert(30)
        self.ll.insert(20, 1)
        self.assertEqual(len(self.ll), 3)
        self.assertEqual(self.ll[0], 10)
        self.assertEqual(self.ll[1], 20)
        self.assertEqual(self.ll[2], 30)

    def test_insert_many(self):
        self.ll.insert([1, 2, 3, 4, 5])
        self.assertEqual(len(self.ll), 5)
        for i in range(1, 6):
            self.assertEqual(self.ll[i - 1], i)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.ll.insert(10, -2)
        with self.assertRaises(IndexError):
            self.ll.insert(20, 1)
        with self.assertRaises(IndexError):
            self.ll.insert(30, -5)

    def test_setitem(self):
        self.ll.insert(10)
        self.ll[0] = 20
        self.assertEqual(self.ll[0], 20)

    def test_setitem_invalid_index(self):
        self.ll.insert(10)
        with self.assertRaises(IndexError):
            self.ll[-2] = 20
        with self.assertRaises(IndexError):
            self.ll[1] = 30

    def test_delete_at_end(self):
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        del self.ll[2]
        self.assertEqual(len(self.ll), 2)
        self.assertEqual(self.ll[0], 10)
        self.assertEqual(self.ll[1], 20)

    def test_delete_at_beginning(self):
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        del self.ll[0]
        self.assertEqual(len(self.ll), 2)
        self.assertEqual(self.ll[0], 20)
        self.assertEqual(self.ll[1], 30)

    def test_delete_at_middle(self):
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        del self.ll[1]
        self.assertEqual(len(self.ll), 2)
        self.assertEqual(self.ll[0], 10)
        self.assertEqual(self.ll[1], 30)

    def test_delete_invalid_index(self):
        self.ll.insert(10)
        with self.assertRaises(IndexError):
            del self.ll[-1]
        with self.assertRaises(IndexError):
            del self.ll[1]

    def test_reversed(self):
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        reversed_list = reversed(self.ll)
        self.assertEqual(len(reversed_list), 3)
        self.assertEqual(reversed_list[0], 30)
        self.assertEqual(reversed_list[1], 20)
        self.assertEqual(reversed_list[2], 10)

    def test_sort_ascending(self):
        self.ll.insert(50)
        self.ll.insert(20)
        self.ll.insert(40)
        self.ll.sort()
        self.assertEqual(len(self.ll), 3)
        self.assertEqual(self.ll[0], 20)
        self.assertEqual(self.ll[1], 40)
        self.assertEqual(self.ll[2], 50)

    def test_sort_descending(self):
        self.ll.insert(50)
        self.ll.insert(20)
        self.ll.insert(40)
        self.ll.sort(reverse=True)
        self.assertEqual(len(self.ll), 3)
        self.assertEqual(self.ll[0], 50)
        self.assertEqual(self.ll[1], 40)
        self.assertEqual(self.ll[2], 20)

    def test_arithmetic_operations(self):
        self.ll.insert(10)
        self.ll.insert(20)
        self.ll.insert(30)
        # Test addition
        self.l = LinkedList()
        self.l.insert([40 , 50])
        result = self.ll + self.l
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 10)
        self.assertEqual(result[1], 20)
        self.assertEqual(result[2], 30)
        self.assertEqual(result[3], 40)
        self.assertEqual(result[4], 50)
        # Test multiplication
        result = self.ll * 2
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], 20)
        self.assertEqual(result[1], 40)
        self.assertEqual(result[2], 60)
        # Test division
        result = self.ll / 2
        self.assertEqual(len(result), 3 )
        self.assertEqual(result[0], 10.0)
        self.assertEqual(result[1], 20.0)
        self.assertEqual(result[2], 30.0)

    def test_empty_list_operations(self):
        with self.assertRaises(ValueError) :
            self.ll + LinkedList()
        result = LinkedList()
        self.assertEqual(len(result), len(self.ll))
        with self.assertRaises(ValueError) :
            self.ll * 5
        with self.assertRaises(ValueError):
            LinkedList() / 2

if __name__ == '__main__':
    unittest.main()
