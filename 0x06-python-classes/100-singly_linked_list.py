#!/usr/bin/python3
''' Singly linked list Node Class'''


class Node:
    ''' Define a Node.
        Attributes:
            data (int): Data of node.
            next_node (Node): Next node.
    '''

    def __init__(self, data, next_node=None):
        ''' Initialize Node.
            Args:
                data (int): Data of node.
                next_node (Node): Next node.

            Raises:
                TypeError: If data is not an integer.
                TypeError: If next_node is not a Node object.
        '''
        self.data = data
        self.next_node = next_node

    ''' Instance property: data '''
    @property
    def data(self):
        ''' Retrieve data '''
        return self.__data

    ''' Instance method: data setter '''
    @data.setter
    def data(self, value):
        ''' Set data as integer
            Args:
                value (int): Data of node.

            Raises:
                TypeError: If data is not an integer.
        '''
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    ''' Instance property: next_node '''
    @property
    def next_node(self):
        ''' Retrieve next_node '''
        return self.__next_node

    ''' Instance method: next_node setter '''
    @next_node.setter
    def next_node(self, value):
        ''' Set next_node as Node
            Args:
                value (Node): Next node.

            Raises:
                TypeError: If next_node is not a Node object.
        '''
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


''' Singly linked list Class '''


class SinglyLinkedList:
    ''' Define a SinglyLinkedList.
        Attributes:
            head (Node): Head of singly linked list.
    '''

    def __init__(self):
        ''' Initialize SinglyLinkedList.
            Args:
                None.
        '''
        self.__head = None

    ''' Instance method: sorted_insert '''
    def sorted_insert(self, value):
        ''' Insert node in sorted position
            Args:
                value (int): Data of node.

            Raises:
                TypeError: If data is not an integer.
        '''
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None:
                if current.next_node.data > value:
                    break
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    ''' Magic method: __str__ '''
    def __str__(self):
        ''' Return string representation of singly linked list '''
        current = self.__head
        string = ''
        while current is not None:
            string += str(current.data) + '\n'
            current = current.next_node

        # neglect last '\n'
        return string[:-1]
