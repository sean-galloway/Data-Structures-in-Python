import unittest
from pythonds.basic import StackLL, StackDLL, Stack, FifoLL, FifoDLL, Fifo, QueueLL, QueueDLL, Queue, DequeLL, DequeDLL, Deque

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


    # basic run thru most of the StackDLL functions

    def test_StackDLL(self):
        # Create the Stack
        s = StackDLL()
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


    # basic run thru most of the FifoDLL functions
    def test_FifoDLL(self):
        # Create the Stack
        s = FifoDLL()
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


    # basic run thru most of the Queue functions
    def test_QueueLL(self):
        # Create the Stack
        s = QueueLL()
        for i in range(11):
            s.enqueue(i)
        self.assertEqual(s.peek(), 0, f'Value not matching: received {s.peek()} expected 10')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Queue Contents: {str(s)}")
        for i in range(5):
            v = s.dequeue()
            expect = i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.peek(), 5, f'Value not matching: received {s.peek()} expected 5')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 6, f"Value not matching: received size {s.size()} expected 6")
        print(f"Queue Contents: {str(s)}")
        for i in range(6):
            v = s.dequeue()
            expect = 5 + i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Queue Contents: {str(s)}")


    # basic run thru most of the Queue functions
    def test_QueueDLL(self):
        # Create the Stack
        s = QueueDLL()
        for i in range(11):
            s.enqueue(i)
        self.assertEqual(s.peek(), 0, f'Value not matching: received {s.peek()} expected 10')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Queue Contents: {str(s)}")
        for i in range(5):
            v = s.dequeue()
            expect = i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.peek(), 5, f'Value not matching: received {s.peek()} expected 5')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 6, f"Value not matching: received size {s.size()} expected 6")
        print(f"Queue Contents: {str(s)}")
        for i in range(6):
            v = s.dequeue()
            expect = 5 + i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Queue Contents: {str(s)}")


    # basic run thru most of the Queue functions
    def test_Queue(self):
        # Create the Stack
        s = Queue()
        for i in range(11):
            s.enqueue(i)
        self.assertEqual(s.peek(), 0, f'Value not matching: received {s.peek()} expected 10')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Queue Contents: {str(s)}")
        for i in range(5):
            v = s.dequeue()
            expect = i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.peek(), 5, f'Value not matching: received {s.peek()} expected 5')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 6, f"Value not matching: received size {s.size()} expected 6")
        print(f"Queue Contents: {str(s)}")
        for i in range(6):
            v = s.dequeue()
            expect = 5 + i
            self.assertEqual(expect, v, f'Value not matching: received {v} expected {expect}')
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Queue Contents: {str(s)}")


    # basic run thru most of the Deque functions
    def test_DequeLL(self):
        # Create the Stack
        s = DequeLL()
        for i in range(11):
            s.add_front(i)
        self.assertEqual(s.peek_front(), 10, f'Value not matching: received {s.peek_front()} expected 10')
        self.assertEqual(s.peek_rear(), 0, f'Value not matching: received {s.peek_rear()} expected 0')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Deque Contents: {str(s)}")
        for i in range(11, 21, 1):
            s.add_rear(i)
        self.assertEqual(s.peek_front(), 10, f'Value not matching: received {s.peek_front()} expected 10')
        self.assertEqual(s.peek_rear(), 20, f'Value not matching: received {s.peek_rear()} expected 20')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 21, f"Value not matching: received size {s.size()} expected 21")
        print(f"Deque Contents: {str(s)}")
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        self.assertEqual(s.peek_front(), 5, f'Value not matching: received {s.peek_front()} expected 5')
        self.assertEqual(s.peek_rear(), 14, f'Value not matching: received {s.peek_rear()} expected 14')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 10, f"Value not matching: received size {s.size()} expected 10")
        print(f"Deque Contents: {str(s)}")
        for i in range(10):
            s.remove_front()
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Deque Contents: {str(s)}")


    # basic run thru most of the Deque functions
    def test_DequeDLL(self):
        # Create the Stack
        s = DequeDLL()
        for i in range(11):
            s.add_front(i)
        self.assertEqual(s.peek_front(), 10, f'Value not matching: received {s.peek_front()} expected 10')
        self.assertEqual(s.peek_rear(), 0, f'Value not matching: received {s.peek_rear()} expected 0')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Deque Contents: {str(s)}")
        for i in range(11, 21, 1):
            s.add_rear(i)
        self.assertEqual(s.peek_front(), 10, f'Value not matching: received {s.peek_front()} expected 10')
        self.assertEqual(s.peek_rear(), 20, f'Value not matching: received {s.peek_rear()} expected 20')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 21, f"Value not matching: received size {s.size()} expected 21")
        print(f"Deque Contents: {str(s)}")
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        self.assertEqual(s.peek_front(), 5, f'Value not matching: received {s.peek_front()} expected 5')
        self.assertEqual(s.peek_rear(), 14, f'Value not matching: received {s.peek_rear()} expected 14')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 10, f"Value not matching: received size {s.size()} expected 10")
        print(f"Deque Contents: {str(s)}")
        for i in range(10):
            s.remove_front()
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Deque Contents: {str(s)}")


    # basic run thru most of the Deque functions
    def test_Deque(self):
        # Create the Stack
        s = Deque()
        for i in range(11):
            s.add_front(i)
        self.assertEqual(s.peek_front(), 10, f'Value not matching: received {s.peek_front()} expected 10')
        self.assertEqual(s.peek_rear(), 0, f'Value not matching: received {s.peek_rear()} expected 0')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 11, f"Value not matching: received size {s.size()} expected 11")
        print(f"Deque Contents: {str(s)}")
        for i in range(11, 21, 1):
            s.add_rear(i)
        self.assertEqual(s.peek_front(), 10, f'Value not matching: received {s.peek_front()} expected 10')
        self.assertEqual(s.peek_rear(), 20, f'Value not matching: received {s.peek_rear()} expected 20')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 21, f"Value not matching: received size {s.size()} expected 21")
        print(f"Deque Contents: {str(s)}")
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_front()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        s.remove_rear()
        self.assertEqual(s.peek_front(), 5, f'Value not matching: received {s.peek_front()} expected 5')
        self.assertEqual(s.peek_rear(), 14, f'Value not matching: received {s.peek_rear()} expected 14')
        self.assertEqual(s.is_empty(), False, "Value not matching: received empty when expected not empty")
        self.assertEqual(s.size(), 10, f"Value not matching: received size {s.size()} expected 10")
        print(f"Deque Contents: {str(s)}")
        for i in range(10):
            s.remove_front()
        self.assertEqual(s.is_empty(), True, "Value not matching: received not empty when expected empty")
        self.assertEqual(s.size(), 0, f"Value not matching: received size {s.size()} expected 0")
        print(f"Deque Contents: {str(s)}")


if __name__ == "__main__":
    unittest.main()