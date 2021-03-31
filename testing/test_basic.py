import unittest
from pythonds.basic import StackLL, Stack, FifoLL, Fifo

class BasicTest(unittest.TestCase):
    def setUp(self):
        print("===========================================================")
        print(self._testMethodName)

    # basic run thru most of the StackLL functions
    def test_StackLL(self):
        # Create the Stack
        s = StackLL()
        for i in range(11):
            s.push(i)
        self.assertEqual(s.peek(), 10, f'Value not matching: received {s.peek()} expected 10')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Stack Contents: {str(s)}")
        for i in range(5):
            v = s.pop()
            expect = 10 - i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.peek(), 5, f'Value not matching: received {s.peek()} expected 5')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 6, f"Value not matching: received size {s.size()} expected 6")
        print(f"Stack Contents: {str(s)}")
        for i in range(6):
            v = s.pop()
            expect = 5 - i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Stack Contents: {str(s)}")

    # basic run thru most of the Stack functions
    def test_Stack(self):
        # Create the Stack
        s = Stack()
        for i in range(11):
            s.push(i)
        self.assertEqual(s.peek(), 10, f'Value not matching: received {s.peek()} expected 10')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Stack Contents: {str(s)}")
        for i in range(5):
            v = s.pop()
            expect = 10 - i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.peek(), 5, f'Value not matching: received {s.peek()} expected 5')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 6, f"Value not matching: received size {s.size()} expected 6")
        print(f"Stack Contents: {str(s)}")
        for i in range(6):
            v = s.pop()
            expect = 5 - i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Stack Contents: {str(s)}")

    # basic run thru most of the FifoLL functions
    def test_FifoLL(self):
        # Create the Stack
        s = FifoLL()
        for i in range(11):
            s.push(i)
        self.assertEqual(s.peek(), 0, f'Value not matching: received {s.peek()} expected 10')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Fifo Contents: {str(s)}")
        for i in range(5):
            v = s.pop()
            expect = i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.peek(), 5, f'Value not matching: received {s.peek()} expected 5')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 6, f"Value not matching: received size {s.size()} expected 6")
        print(f"Fifo Contents: {str(s)}")
        for i in range(6):
            v = s.pop()
            expect = 5 + i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Fifo Contents: {str(s)}")

    # basic run thru most of the Fifo functions
    def test_Fifo(self):
        # Create the Stack
        s = Fifo()
        for i in range(11):
            s.push(i)
        self.assertEqual(s.peek(), 0, f'Value not matching: received {s.peek()} expected 10')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Fifo Contents: {str(s)}")
        for i in range(5):
            v = s.pop()
            expect = i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.peek(), 5, f'Value not matching: received {s.peek()} expected 5')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 6, f"Value not matching: received size {s.size()} expected 6")
        print(f"Fifo Contents: {str(s)}")
        for i in range(6):
            v = s.pop()
            expect = 5 + i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Fifo Contents: {str(s)}")


if __name__ == "__main__":
    unittest.main()