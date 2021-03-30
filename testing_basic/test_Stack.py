import unittest
from pythonds.basic import Stack

class StackTest(unittest.TestCase):
    def setUp(self):
        print("===========================================================")
        print("self._testMethodName")

    def test_create_load_peek_unload_partial_finish_unload_check_empty(self):
        # Create the Stack
        s = Stack()
        for i in range(11):
            s.push(i)
        print(f"Should be 10: {s.peek()}")
        print(f"Should be false: {s.is_empty()}")
        for i in range(6):
            s.pop
        print(f"Should be 5: {s.peek()}")
        print(f"Should be false: {s.is_empty()}")
        for i in range(6):
            s.pop
        print(f"Should be true: {s.is_empty()}")

if __name__ == "__main__":
    unittest.main()