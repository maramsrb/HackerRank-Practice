#Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its  attribute, insert this node at the desired position and return the head node.


class Node:
  def __init__(self,data=0,next=None, pos=0):
    self.value= data
    self.next = next
    self.pos = pos

def insertNodeatPosition(headNode,z, x):
  currentNode = headNode
  
  if x == 1:
    newNode = Node()
    newNode.value = z
    newNode.next = currentNode
    headNode = newNode
  else:   
    i=2
    while(currentNode.next is not None):
      prev_Node = currentNode
      currentNode = currentNode.next        
      if i == x:
        temp_currentNode = currentNode       
        newNode = Node()
        newNode.value = z
        newNode.next = temp_currentNode
        prev_Node.next = newNode
      i+=1
  currentNode=headNode
  while(currentNode is not None):
    print(currentNode.value)
    currentNode = currentNode.next
    

node1=Node()
node2=Node()
node3=Node()
node4=Node()
node5=Node()
node6=Node()

node1.value = 10
node1.next = node2
node2.value = 20
node2.next = node3
node3.value = 30
node3.next = node4
node4.value = 40
node4.next = node5 
node5.value = 50
node5.next = node6
node6.value = 60
node6.next = None

insertNodeatPosition(node1,500,6)


