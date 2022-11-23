"""lmpthw: building a custom queue exercise 15"""

class MyQueue():

    def __init__(self):

        """Create an empty list"""

        self.mq = []

    def __str__(self):

        """Print out an a string representation of the the queue"""

        return f"{self.mq}"

    def enqueue(self, element):

        """Append something to the end of the queue (Last In, Last Out"""

        #append the element to the end of the list
        self.mq.append(element)
        return f"{element} was enqueued", element

    def dequeue(self):

        """Pop from the front of the queue (First In, First Out)"""

        #check if queue is empty
        if not self.mq:
            raise Exception("Queue is empty")

        #pop the element off the front of the list
        dequeue = self.mq.pop(0)
        return f"{dequeue} was dequeued"

    def is_empty(self):
        
        """"Check if the queue is empty"""

        if self.mq == None:
            return True 

    def peek(self):

        """Peek at the first element in the queue"""

        return self.mq[0]


