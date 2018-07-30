# 删除逻辑有错误，或许还有一吨的bug，不抢救了


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.node = []
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.head is None:
            return -1
        if self.length > index >= 0:
            get_node = self.node[self.head]
            for i in range(0, index):
                get_node = self.node[get_node[1]]
            return get_node[2]
        else:
            return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.length == 0:
            self.head = self.length
            self.tail = self.length
            self.node.append([None, None, val])
        else:
            self.node.append([None, self.head, val])
            self.node[self.head][0] = self.length
            self.head = self.length
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.node.append([self.tail, None, val])
        self.node[self.tail][1] = self.length
        if self.length == 0:
            self.head = 0
        self.tail = self.length
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will
        not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif self.length > index > 0:
            cur = self.length
            get_node = self.node[self.head]
            for i in range(0, index):
                get_node = self.node[get_node[1]]
            this_index = self.node[get_node[0]][1]
            self.node.append([get_node[0], self.node[get_node[0]][1], val])
            self.node[get_node[0]][1] = cur
            self.node[this_index][0] = cur
            self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.length:
            return
        if index == self.head and self.length == 1:
            self.node[self.head] = [None, None, None]
            self.head = None
            self.tail = None
        elif index == self.head:
            self.head = self.node[self.head][1]
            self.node[self.head][0] = None
        elif index < self.length:
            get_node = self.node[self.head]
            for i in range(0, index):
                get_node = self.node[get_node[1]]
            self.node[get_node[0]][1] = get_node[1]
            self.node[get_node[1]][0] = get_node[0]
        self.length -= 1


# 口月言水可以田国，你干嘛啦，可以啦，是不是好些了
# 你还唱啥歌不？我点一个？字暗不暗，要么进word聊？我喜欢这个，，好你让我适应一下
# 字体可以放大，要么放大些？好的好哎呀我就说好了好了，我傻了我觉得不小，好，我感觉没有大呀，哈哈哈哈
# 宝宝我们开始互相点歌吧，好呀我我下次要给你唱海芋恋，谁的歌，我还没听过萧敬腾，我给你唱王妃么，萧敬腾的歌都挺高
# 搜了一下，这首我听过，要不要配合个啥唱唱？我都行我的小哥哥我要你给我唱黄昏，小刚的？你怎么知道我会唱？哈哈哈哈是吗
# 当年我用这首歌圈粉那你圈圈我，好试试看，毕竟是很久很久的歌了，高中吧高一好像你那个年代，对，我高一的时候小刚才火
# 你应该是小学，哈哈哈哈，2003年吧，薛之谦的歌有喜欢的吗？还有陈奕迅，五月天，周杰伦自取，歌名自取？

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
if __name__ == "__main__":
    linkedList = MyLinkedList()
    print(linkedList.addAtHead(5))
    print(linkedList.addAtHead(2))
    print(linkedList.deleteAtIndex(1))
    print(linkedList.addAtIndex(1, 9))
    print(linkedList.addAtHead(4))
    print(linkedList.addAtHead(9))
    print(linkedList.addAtHead(8))
    print(linkedList.get(3))
    print(linkedList.addAtTail(1))
    print(linkedList.addAtIndex(3, 6))
    print(linkedList.addAtHead(3))
