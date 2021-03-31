# This file contains basic data structure code for education purposes.
# Use at your own risk.


class Node(object):
    '''
    ###############################################################################\n
    # Node Object : This is just a simple node for use in the linked list class\n
    ###############################################################################\n
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeDLL(object):
    '''
    ###############################################################################\n
    # NodeDLL Object : This is just a simple node for use in the doubly linked list class\n
    ###############################################################################\n
    '''
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList(object):
    '''
    ###############################################################################\n
    # LinkedList Object : This is a versatile linked list object, with only a\n
    #                     modicum of error checking\n
    ###############################################################################\n
    '''

    def __init__(self):
        # init method : set up the head and tail pointers and initialize the count to 0
        self.head = None
        self.tail = None
        self.list_count = 0

    def __str__(self):
        # a string representation of the linked list; useful for printing out the
        # total contents
        n = self.head
        s = "Node List [ "
        while n != None:
            s += str(n.data) + " "
            n = n.next
        s += "]"
        return s

    def get_count(self):
        # get_count just returns the count; it's not rocket science
        return self.list_count

    def peek_head(self):
        # Return the contents of the head pointer
        return self.head.data

    def peek_tail(self):
        # Return the contents of the tail pointer
        return self.tail.data

    def add_to_head(self, data):
        # Add the passed in data to the head of the list
        n = Node(data)
        self.list_count += 1
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n

    def add_to_tail(self, data):
        # Add the passed in data to the tail of the list
        n = Node(data)
        self.list_count += 1
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def del_from_head(self):
        # delete the item from the head of the list and return the data
        if self.list_count > 0:
            data = self.head.data
            self.list_count -= 1
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                n = self.head.next
                self.head = n
            return data

    def del_from_tail(self):
        # delete the item from the tail of the list and return the data
        # This is the only tricky method in the bunch. One has to setup
        # two pointers, nth and nextToNth and walk them down to the end.
        # Once nth is at the end, nextToNth is one away from the end and
        # becomes the new tail.
        if self.list_count > 0:
            data = self.tail.data
            self.list_count -= 1
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                nextToNth = self.head
                nth = self.head.next
                while nth.next != None:
                    nextToNth = nth
                    nth = nth.next
                nextToNth.next = None
                self.tail = nextToNth
            return data


class DoublyLinkedList(object):
    '''
    ###############################################################################\n
    # Doubly LinkedList Object : This is a versatile doubly linked list object, with only a\n
    #                            modicum of error checking\n
    ###############################################################################\n
    '''

    def __init__(self):
        # init method : set up the head and tail pointers and initialize the count to 0
        self.head = None
        self.tail = None
        self.list_count = 0

    def __str__(self):
        # a string representation of the linked list; useful for printing out the
        # total contents
        n = self.head
        s = "Node List [ "
        while n != None:
            s += str(n.data) + " "
            n = n.next
        s += "]"
        return s

    def get_count(self):
        # get_count just returns the count; it's not rocket science
        return self.list_count

    def peek_head(self):
        # Return the contents of the head pointer
        return self.head.data

    def peek_tail(self):
        # Return the contents of the tail pointer
        return self.tail.data

    def add_to_head(self, data):
        # Add the passed in data to the head of the list
        n = Node(data)
        self.list_count += 1
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def add_to_tail(self, data):
        # Add the passed in data to the tail of the list
        n = Node(data)
        self.list_count += 1
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

    def del_from_head(self):
        # delete the item from the head of the list and return the data
        if self.list_count > 0:
            data = self.head.data
            self.list_count -= 1
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                n = self.head.next
                n.prev = None
                self.head = n
            return data

    def del_from_tail(self):
        # delete the item from the tail of the list and return the data
        if self.list_count > 0:
            data = self.tail.data
            self.list_count -= 1
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return data


class StackLL:
    '''
    ###############################################################################\n
    # Stack Class implemented using Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the tail of the list\n
    # peek returns data from the tail of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return f"Stack: {str(self.ll)}"

    def is_empty(self):
        return self.ll.list_count == 0

    def push(self, item):
        self.ll.add_to_tail(item)

    def pop(self):
        return self.ll.del_from_tail()

    def peek(self):
        return self.ll.peek_tail()

    def size(self):
        return self.ll.get_count()


class StackDLL:
    '''
    ###############################################################################\n
    # Stack Class implemented using Doubly Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the tail of the list\n
    # peek returns data from the tail of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = DoublyLinkedList()

    def __str__(self):
        return f"Stack: {str(self.ll)}"

    def is_empty(self):
        return self.ll.list_count == 0

    def push(self, item):
        self.ll.add_to_tail(item)

    def pop(self):
        return self.ll.del_from_tail()

    def peek(self):
        return self.ll.peek_tail()

    def size(self):
        return self.ll.get_count()


class Stack:
    '''
    ###############################################################################\n
    # Stack Class implemented using Python Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the tail of the list\n
    # peek returns data from the tail of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''

    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Stack: {str(tuple(self.items))}"

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class FifoLL:
    '''
    ###############################################################################\n
    # Fifo Class implemented using Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the head of the list\n
    # peek returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return f"Fifo: {str(self.ll)}"

    def is_empty(self):
        return self.ll.get_count() == 0

    def push(self, item):
        self.ll.add_to_tail(item)

    def pop(self):
        return self.ll.del_from_head()

    def peek(self):
        return self.ll.peek_head()

    def size(self):
        return self.ll.get_count()


class FifoDLL:
    '''
    ###############################################################################\n
    # Fifo Class implemented using Doubly Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the head of the list\n
    # peek returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = DoublyLinkedList()

    def __str__(self):
        return f"Fifo: {str(self.ll)}"

    def is_empty(self):
        return self.ll.get_count() == 0

    def push(self, item):
        self.ll.add_to_tail(item)

    def pop(self):
        return self.ll.del_from_head()

    def peek(self):
        return self.ll.peek_head()

    def size(self):
        return self.ll.get_count()


class Fifo:
    '''
    ###############################################################################\n
    # Fifo Class implemented using Python Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the head of the list\n
    # peek returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Fifo: {str(tuple(self.items))}"

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


class QueueLL:
    '''
    ###############################################################################\n
    # Queue Class implemented using Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the head of the list\n
    # peek returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return f"Queue: {str(self.ll)}"

    def is_empty(self):
        return self.ll.get_count() == 0

    def enqueue(self, item):
        self.ll.add_to_tail(item)

    def dequeue(self):
        return self.ll.del_from_head()

    def peek(self):
        return self.ll.peek_head()

    def size(self):
        return self.ll.get_count()


class QueueDLL:
    '''
    ###############################################################################\n
    # Queue Class implemented using Doubly Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # push adds the data to the tail of the list\n
    # pop returns data from the head of the list\n
    # peek returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = DoublyLinkedList()

    def __str__(self):
        return f"Queue: {str(self.ll)}"

    def is_empty(self):
        return self.ll.get_count() == 0

    def enqueue(self, item):
        self.ll.add_to_tail(item)

    def dequeue(self):
        return self.ll.del_from_head()

    def peek(self):
        return self.ll.peek_head()

    def size(self):
        return self.ll.get_count()


class Queue:
    '''
    ###############################################################################\n
    # Queue Class implemented using Python Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # enqueue adds the data to the tail of the list\n
    # dequeue returns data from the head of the list\n
    # peek returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Queue: {str(tuple(self.items))}"

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


class DequeLL:
    '''
    ###############################################################################\n
    # Deque Class implemented using Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # add_front adds the data to the tail of the list\n
    # add_rear adds the data to the head of the list\n
    # remove_front returns data from the tail of the list\n
    # remove_rear returns data from the head of the list\n
    # peek_front returns data from the tail of the list\n
    # peek_rear returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return f"Deque: {str(self.ll)}"

    def is_empty(self):
        return self.ll.get_count() == 0

    def add_rear(self, item):
        self.ll.add_to_head(item)

    def add_front(self, item):
        self.ll.add_to_tail(item)

    def remove_rear(self):
        return self.ll.del_from_head()

    def remove_front(self):
        return self.ll.del_from_tail()

    def peek_rear(self):
        return self.ll.peek_head()

    def peek_front(self):
        return self.ll.peek_tail()

    def size(self):
        return self.ll.get_count()


class DequeDLL:
    '''
    ###############################################################################\n
    # Deque Class implemented using Doubly Linked Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # add_front adds the data to the tail of the list\n
    # add_rear adds the data to the head of the list\n
    # remove_front returns data from the tail of the list\n
    # remove_rear returns data from the head of the list\n
    # peek_front returns data from the tail of the list\n
    # peek_rear returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.ll = DoublyLinkedList()

    def __str__(self):
        return f"Deque: {str(self.ll)}"

    def is_empty(self):
        return self.ll.get_count() == 0

    def add_rear(self, item):
        self.ll.add_to_head(item)

    def add_front(self, item):
        self.ll.add_to_tail(item)

    def remove_rear(self):
        return self.ll.del_from_head()

    def remove_front(self):
        return self.ll.del_from_tail()

    def peek_rear(self):
        return self.ll.peek_head()

    def peek_front(self):
        return self.ll.peek_tail()

    def size(self):
        return self.ll.get_count()


class Deque:
    '''
    ###############################################################################\n
    # Deque Class implemented using Python Lists\n
    # Notes:\n
    # __str__ returns a string representation of the entire list; useful for debug\n
    # add_front adds the data to the tail of the list\n
    # add_rear adds the data to the head of the list\n
    # remove_front returns data from the tail of the list\n
    # remove_rear returns data from the head of the list\n
    # peek_front returns data from the tail of the list\n
    # peek_rear returns data from the head of the list\n
    # is_empty returns a boolean indicating whether the list is empty or not\n
    # size returns an intger with the number of items in the list\n
    ###############################################################################\n
    '''
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Deque: {str(tuple(self.items))}"

    def is_empty(self):
        return self.items == []

    def add_rear(self, item):
        self.items.insert(0, item)

    def add_front(self, item):
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop(0)

    def remove_front(self):
        return self.items.pop()

    def peek_rear(self):
        return self.items[0]

    def peek_front(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

