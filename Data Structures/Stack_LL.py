class Node:
  def __init__(self , data):
    self.data = data
    self.next = None
  
class Stack:
  def __init__(self):  
    self.head = None
  def isempty(self):
    if self.head == None:
      return True
    else:
      return False
  def push(self):

    data = input('Enter a new data: ')

    if self.isempty():
      self.head = Node(data)
    else:
      NEWNODE = Node(data)
      NEWNODE.next = self.head
      self.head = NEWNODE
          
  def pop(self):

    if self.isempty():
      return None
    else:
      poppedNode = self.head
      self.head = self.head.next
      poppedNode.next = None
      return poppedNode.data

  def peek(self):
    if self.isempty():
      return None

    else:
      print('\n head node -> ',self.head.data)
  
  def display(self):
    if self.isempty():
      print('is empty')
    else:
      iternode = self.head
      while iternode:
        print(iternode.data , end='')
        iternode = iternode.next
        if iternode:
          print(' -> ',end='')
      return 


stack = Stack()
stack.push()
stack.push()
stack.push()
stack.push()

stack.display()

stack.pop()
stack.pop()

stack.peek()

stack.display()
