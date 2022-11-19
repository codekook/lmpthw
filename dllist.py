"""lmpthw: double linked list exercise 14"""

class Node(object):

    """Node class made of up the node, pointer to next and pointer to previous"""

    def __init__(self, dataval=None, nextval=None, prevval=None):

        self.dataval = dataval
        self.nextval = nextval
        self.prevval = prevval

    def __repr__(self):
        return repr(self.dataval)

class DoubleLinkedList(object):

    """Double linked list class"""

    def __init__(self):

        """Instantiate a double linked list"""

        self.head = None
        self.end = None
        self.count = 0

    def __repr__(self):

        """Create a string representation of the data in the linked list"""

        nodes = []

        current_node = self.head

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.nextval

        current_node = self.end

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.prevval

        return "[" + "->".join(nodes) + "]"

    def append(self, dataval):

        """Appends a new element to the end of the double linked list"""

        #set the pointer to what is currently the end of the linked list
        self.end = Node(dataval=dataval, prevval=self.end)
        print(self.end)

        #count dynamically the length of the list
        self.count += 1

    def prepend(self, dataval):

        """Prepends a new element to the beginning of the double linked list"""

        self.head = Node(dataval=dataval, nextval=self.head)
        print(self.head)
        self.count += 1
