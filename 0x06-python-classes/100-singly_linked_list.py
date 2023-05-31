#!/usr/bin/python3

"""Defines Classes for a singly list"""


class Node:
    """represents a node for a singly list"""

    def __init__(self, data, next_node=None):
        """
            Initialize a new Node.
            Args:
                data (int): new node's data.
                next_node (Node): the new node's next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve the node's data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets the node's data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves the next node for the current node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the next node for the current node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initalizes a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp_h = self.__head
            while (temp_h.next_node is not None and
                    temp_h.next_node.data < value):
                temp_h = temp_h.next_node
            new_node.next_node = temp_h.next_node
            temp_h.next_node = new_node

    def __str__(self):
        """Define the print()/string representation of a SinglyLinkedList."""
        vals = []
        temp_h = self.__head
        while temp_h is not None:
            vals.append(str(temp_h.data))
            temp_h = temp_h.next_node
        return ('\n'.join(vals))
