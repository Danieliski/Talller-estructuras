class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def traverse(self):
    current = self.head
    if(current is None):
      return
    else:
      while(current is not None):
        print(current.value)
        current = current.next
  def add_at_tail(self, value):
    if(self.head is None):
      self.head = Node(value)
    else:
      current = self.head
      while(current.next is not None):
        current = current.next
      current.next = Node(value)

  def rec_add_at_tail(self,value, current=None):
    if(self.head is None):
      self.head = Node(value)
      return
    if(current.next is None):
      current.next = Node(value)
      return
    else:
      self.rec_add_at_tail(value, current.next)

  def rec_traverse(self, current):
    if(current is None):
      return
    else:
      print(current.value)
      self.rec_traverse(current.next)
# 
# ll = LinkedList()
# ll.rec_add_at_tail(5, ll.head)
# ll.rec_add_at_tail(6, ll.head)
# ll.rec_add_at_tail(7, ll.head)
# ll.rec_traverse(ll.head)

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DLinkedList:
  def __init__(self):
    self.header = Node(None)
    self.trailer = Node(None)
    self.header.next = self.trailer
    self.trailer.prev = self.header

  def traverse(self):
    current = self.header.next
    while(current != self.trailer):
      print(current.value, "<=>", end=" ")
      current = current.next
  
  def add_at_head(self, value):
    #está vacía?
    if(self.header.next == self.trailer):
      #agrego el primer elemento
      new_node = Node(value)
      self.header.next = new_node
      new_node.prev = self.header
      new_node.next = self.trailer
      self.trailer.prev = new_node
    else:
      new_node = Node(value)
      old_head = self.header.next
      self.header.next = new_node
      new_node.prev = self.header
      new_node.next = old_head
      old_head.prev = new_node

# dll = DLinkedList()
# dll.add_at_head(5)
# dll.add_at_head(6)
# dll.add_at_head(7)
# dll.traverse()