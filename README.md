# Data-Structures-in-Python

These are a list of data structures written in python for self learning

## [basic.py](pythonds/basic.py) contents

### LinkedList Class

* __init__: this includes a count of items, a head and tail pointer
* __str__: this returns a string representation of the entire list; this is useful for debug
* get_count: this returns the number of items in the list
* is_empty: this returns a boolean on whether the list is empty or not
* peek_head: this returns the value at the head of the list
* peek_tail: this returns the value as the tail of the list; the tail pointer comes in handy for this
* _reset_tail_pointer: this makes sure the tail pointer is actually pointing to the tail; this is useful for some of the insertion and deletion functions
* add_to_head: this adds an item to the head of the list
* add_before_item: this add a data item before another data item that matches the value passed in
* add_after_item: this add a data item after another data item that matches the value passed in
* add_at_index: this adds a data item to the point in the list matching the index passed in
* add_to_tail: this adds an item to the tail of the list
* del_from_head: this deletes the head item
* del_from_tail: this deletes the tail item
* del_by_value: this deletes an item from the list that matches the value pass in
* reverse_list: this simply reverses the list

### OrderedLinkedList Class

* __init__: this includes a count of items, a head and tail pointer
* __str__: this returns a string representation of the entire list; this is useful for debug
* get_count: this returns the number of items in the list
* is_empty: this returns a boolean on whether the list is empty or not
* peek_head: this returns the value at the head of the list
* peek_tail: this returns the value as the tail of the list
* add: add data to the list in order
* remove: delete a node with a specific value
* search: returns True if the value is in the list, False otherwise
* index: returns the position of the item in the list
* del_from_tail: removes the last item from the list
* del_by_index: removes the data corresponding to the index passed in

### DoublyLinkedList Class

* __init__: this includes a count of items, a head and tail pointer
* __str__: this returns a string representation of the entire list; this is useful for debug
* get_count: this returns the number of items in the list
* is_empty: this returns a boolean on whether the list is empty or not
* peek_head: this returns the value at the head of the list
* peek_tail: this returns the value as the tail of the list; the tail pointer comes in handy for this
* _reset_tail_pointer: this makes sure the tail pointer is actually pointing to the tail; this is useful for some of the insertion and deletion functions
* add_to_head: this adds an item to the head of the list
* add_before_item: this add a data item before another data item that matches the value passed in
* add_after_item: this add a data item after another data item that matches the value passed in
* add_at_index: this adds a data item to the point in the list matching the index passed in
* add_to_tail: this adds an item to the tail of the list
* del_from_head: this deletes the head item
* del_from_tail: this deletes the tail item
* del_by_value: this deletes an item from the list that matches the value pass in
* reverse_list: this simply reverses the list

### StackLL - a stack class based on the LinkedList Class

* __init__ : initialize the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* push: adds an entry to the tail of the list
* pop: pops an entry from the tail of the list
* peek: returns the value at the tail of the list
* size: returns the size of the list

### StackDLL - a stack class based on the DoublyLinkedList Class

* __init__ : initialize the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* push: adds an entry to the tail of the list
* pop: pops an entry from the tail of the list
* peek: returns the value at the tail of the list
* size: returns the size of the list

### Stack - a stack class based on the python arrays

* __init__ : initialize the array
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* push: adds an entry to the tail of the list
* pop: pops an entry from the tail of the list
* peek: returns the value at the tail of the list
* size: returns the size of the list

### FifoLL - a fifo class based on the LinkedList Class

* __init__ : initialize the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* push: adds an entry to the tail of the list
* pop: pops an entry from the head of the list
* peek: returns the value at the head of the list
* size: returns the size of the list

### FifoDLL - a fifo class based on the DoublyLinkedList Class

* __init__ : initialize the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* push: adds an entry to the tail of the list
* pop: pops an entry from the head of the list
* peek: returns the value at the head of the list
* size: returns the size of the list

### Fifo - a fifo class based on python arrays

* __init__ : initialize the array
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* push: adds an entry to the tail of the list
* pop: pops an entry from the head of the list
* peek: returns the value at the head of the list
* size: returns the size of the list

### QueueLL - a queue class based on the LinkedList Class

* __init__ : initialize the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* enqueue: adds an entry to the tail of the list
* dequeue: pops an entry from the head of the list
* peek: returns the value at the head of the list
* size: returns the size of the list

### QueueDLL - a queue class based on the DoublyLinkedList Class

* __init__ : initialize the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* enqueue: adds an entry to the tail of the list
* dequeue: pops an entry from the head of the list
* peek: returns the value at the head of the list
* size: returns the size of the list

### Queue - a queue class based on the python arrays

* __init__ : initialize the array
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* enqueue: adds an entry to the tail of the list
* dequeue: pops an entry from the head of the list
* peek: returns the value at the head of the list
* size: returns the size of the list

### DequeLL - a deque based upon the LinkedList Class

* __init__: set up the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* add_rear: add an item to the head of the list
* add_front: add an item to the tail of the list
* remove_rear: remove the head item
* remove_front: remove the tail item
* peek_rear: return the head item value
* peek_front: return the tail item value
* size: return the size of the list

### DequeDLL - a deque based upon the DoublyLinkedList Class

* __init__: set up the linked list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* add_rear: add an item to the head of the list
* add_front: add an item to the tail of the list
* remove_rear: remove the head item
* remove_front: remove the tail item
* peek_rear: return the head item value
* peek_front: return the tail item value
* size: return the size of the list

### Deque - a deque based upon python lists

* __init__: set up the list
* __str__ : this returns a string representation of the entire list; this is useful for debug
* is_empty: this returns a boolean on whether the list is empty or not
* add_rear: add an item to the head of the list
* add_front: add an item to the tail of the list
* remove_rear: remove the head item
* remove_front: remove the tail item
* peek_rear: return the head item value
* peek_front: return the tail item value
* size: return the size of the list
