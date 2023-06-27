#!/usr/bin/python3
"""linked list"""


class Node:
    """Node"""

    def __init__(self, data, next_node=None):
        """Node
            Args:
                data: data of the node
                next_node: pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """new_node setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Linked list"""

    def __init__(self):
        """new linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert in sorted way
        Args:
            value: the value of the new node
        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
        elif value < self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            node.next_node = temp.next_node
            temp.next_node = node

    def __str__(self):
        """print the object"""
        data = []
        tmp = self.__head
        while tmp is not None:
            data.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(data)
