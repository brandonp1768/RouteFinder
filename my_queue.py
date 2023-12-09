class MyQueue:
    """
    The MyQueue Class represents a linear data structure that uses FIFO method to take in elements
    and put them back out. Has a rear and a front, front has to be accessed before you can get to rear.
    """

    def __init__(self):
        """
        Initializer (Constructor) for the MyQueue Class

        Parameters:

        Returns:
            Nothing
        """
        self.data = []

    def enqueue(self, item):
        """
        enqueue method for MyQueue -- supports adding an element to the queue

        Parameters:
            item: represents the item that you want to add to the queue

        Returns:
            Nothing
        """
        self.data.append(item)

    def dequeue(self):
        """
        dequeue method for MyQueue -- supports removing the element at front of the queue

        Parameters:

        Returns:
            Nothing
        """
        if not len(self.data) == 0:
            item = self.data.pop(0)
            return item
        else:
            raise IndexError('Queue is Empty')

    def is_empty(self):
        """
        is_empty method for MyQueue -- supports finding whether the queue is empty or not

        Parameters:

        Returns:
            True if the queue is empty
        """
        return len(self.data) == 0

    def size(self):
        """
        size method for MyQueue -- supports finding the size of the queue

        Parameters:

        Returns:
            the size of the queue
        """
        return len(self.data)
