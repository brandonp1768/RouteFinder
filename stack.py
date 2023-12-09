import copy


class Stack:
    """
    The Stack Class represents a linear data structure that uses LIFO that to take in elements and put
    them back out. Has a base and a top, to access the base you have to access everything above it first.
    """

    def __init__(self):
        """
        Initializer (Constructor) for the Stack Class

        Parameters:

        Returns:
            Nothing
        """
        self.data = []

    def push(self, item):
        """
        push methods for Stack -- supports adding elements to the stack

        Parameters:
            item: represents the item that you wish to add to the stack

        Returns:
            Nothing
        """
        self.data.append(item)

    def pop(self):
        """
        pop method for Stack -- supports removing and returning an item form the stack

        Parameters:

        Returns:
            Nothing
        """
        return self.data.pop()

    def __str__(self):
        """
        str method for Stack -- supports returning a string representation of the stack

        Parameters:

        Returns:
            a string representation of the stack
        """
        return str(self.data)

    def __repr__(self):
        """
        repr method for Stack -- supports returning a string representation of an object

        Parameters:

        Returns:
            a string representation of the object
        """
        return str(self)

    def size(self):
        """
        size method for Stack -- supports finding the size of the stack

        Parameters:

        Returns:
            the size of the stack
        """
        return len(self.data)

    def is_empty(self):
        """
        is_empty method for Stack -- supports finding whether a stack is empty or not

        Parameters:

        Returns:
            True if the stack is empty
        """
        return self.data == []

    def peek(self):
        """
        peek method for Stack -- supports finding the element at the top of the stack

        Parameters:

        Returns:
            the element at the top of the stack
        """
        return self.data[-1]

    # return a deep copy of this Stack
    def clone(self):
        """
        clone method for Stack -- supports creating a new stack that is a clone of the one you are copying

        Parameters:

        Returns:
            the stack that has been cloned
        """
        s = Stack()
        s.data = copy.deepcopy(self.data)
        return s
