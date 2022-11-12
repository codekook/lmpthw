"""lmpthw: exercise 13 uses classes to create a list"""

class SingleLinkedListNode(object):

    """Linked list node made up of the data and the pointer"""

    def __init__(self, dataval=None, nextval=None):

        self.dataval = dataval
        self.nextval = nextval

    def __repr__(self):
        return repr(self.dataval)


class SingleLinkedList(object):

    """Create a new single linked list"""

    def __init__(self):

        self.head = None
        self.end = None

    def __repr__(self):

        """Create a string representation of the data in the linked list"""

        nodes = []
        current_node = self.head

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.nextval

        return "[" + "->".join(nodes) + "]"

    def append(self, dataval):

        """Appends a new element on the end of the list."""

        #check if the head of the linked list is null
        if not self.head:
            self.head = SingleLinkedListNode(dataval = dataval)
            return

        #point to the node currently iterating over
        current_node = self.head

        #iterate over until the end of the linked list
        while current_node.nextval:
            current_node = current_node.nextval

        #initialize the new node
        current_node.nextval = SingleLinkedListNode(dataval = dataval)

    def count(self):

        """Counts the number of elements in the list"""

        if self.head == None:
            return 0
        else:
            #point to the node currently iterating over
            current_node = self.head
            counter = 0
            while current_node != None:
                current_node = current_node.nextval
                counter += 1

        return counter

    def remove(self, data):

        """Remove the first occurance of elements in the list"""

        current_node = self.head
        previous = None

        while current_node and current_node.dataval != data:
            previous = current_node
            current_node = current_node.nextval

        if previous is None:
            self.head = current_node.nextval
        else:
            previous.nextval = current_node.nextval
            current_node.nextval = None

    def prepend(self, dataval):

        """Insert a new element at the beginning of the list"""

        self.head = SingleLinkedListNode(dataval = dataval, nextval = self.head)

    def find(self, data):

        """Search for the first argumetn with dataval matching data.
        Return None if not found."""

        current_node = self.head

        while current_node and current_node.dataval != data:
            current_node = current_node.nextval

        return current_node

    def add_after(self, middle_dataval, dataval):

        """Insert a new element after the node middle_dataval"""

        if middle_dataval is None:
            print("data to insert after not specified")
            return

        current_node = self.head

        while current_node and current_node.dataval != middle_dataval:
            current_node = current_node.nextval

        new_node = SingleLinkedListNode(dataval = dataval)

        new_node.nextval = current_node.nextval
        current_node.nextval = new_node
