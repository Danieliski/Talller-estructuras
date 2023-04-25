class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self, n):
        self.head = None
        self.size = n

        for i in range(n):
            row_head = None
            for j in range(n):
                node = Node(None)
                if not self.head:
                    self.head = node
                if not row_head:
                    row_head = node
                if i > 0:
                    prev_node = self.get_node(i-1, j)
                    if prev_node:
                        prev_node.down = node
                if j > 0:
                    prev_node = row_head.right
                    if prev_node:
                        prev_node.right = node
                row_head.right = node
                node.down = row_head

    def get_node(self, i, j):
        if i < 0 or j < 0 or i >= self.size or j >= self.size:
            return None

        node = self.head
        for _ in range(i):
            node = node.down
        for _ in range(j):
            node = node.right
        return node


matrix = LinkedList(4)