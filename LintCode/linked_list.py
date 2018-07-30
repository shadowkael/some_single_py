class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :param index: int
        :return: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :param val: int
        :return: None
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :param val: int
        :return: None
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the lentgth of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :param index: int
        :param val: int
        :return: void
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        if index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(1, index):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :param index: int
        :return: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

    def getAll(self):
        a = []
        curr = self.head
        for i in range(self.size):
            a.append(curr.val)
            curr = curr.next
        print(a)


if __name__ == "__main__":
    test = MyLinkedList()
    print(test.addAtHead(1))
    test.getAll()
    print(test.addAtIndex(1, 2))
    test.getAll()
    print(test.get(1))
    test.getAll()
    print(test.get(0))
    test.getAll()
    print(test.get(2))
