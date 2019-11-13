"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.length += 1 
            self.head = new_node  
    
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            if self.tail is None:
                self.head = None
                self.length -= 1
            else:
                new_head = self.head.next
                new_head.prev = None
                self.head = new_head
                self.length -= 1
        return removed_value

    # Adds value to end of doubly linked list
    def add_to_tail(self, value):
        # create node for new value
        new_node = ListNode(value)
        # if the list is empty
        if self.length == 0:
            # set head and tail to new node and increment length by 1
            self.tail = new_node
            self.head = new_node
            self.length += 1
        # If list isn't empty
        else: 
            # And the tail is empty
            if self.tail is None:
                # Set the new nodes previous to the current head
                new_node.prev = self.head
                # Set the tail to the new node
                self.tail = new_node
                # Set the heads next to the new node
                self.head.next = new_node
                # Increment length by 1
                self.length += 1
            # If the tail isn't empty
            else:
                # Set new nodes previous to the current tail node
                new_node.prev = self.tail 
                # Set current tail nodes next to new node
                self.tail.next = new_node
                # Increment length by 1
                self.length += 1 
                # Set tail to new_node
                self.tail = new_node 

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail == self.head:
            removed_value = self.tail.value
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            removed_value = self.tail.value
            previous_node = self.tail.prev
            previous_node.next = None
            self.tail = previous_node
            self.length -= 1
        return removed_value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        if node.next == None:
            self.remove_from_tail()
            self.add_to_head(value)
        else:
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p
            self.add_to_head(value)
            self.length -= 1


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        if node.prev == None:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p
            self.add_to_tail(value)
            self.length -= 1


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        max_ = 0
        node = self.head
        while node != self.tail:
            if node.value > max_:
                max_ = node.value
            node = node.next
        if node.value > max_:
            max_ = node.value
        return max_