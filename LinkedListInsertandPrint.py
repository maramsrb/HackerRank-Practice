#LinkedList insert and print methods

class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None 

  def insert(self, data):
    newNode=Node(data)
    print("Nuevo Nodo:",newNode.data)
    if(self.head):
      current=self.head
      print("head:",current.data)      
      while(current.next):
        print("Si hay algo en next")
        current = current.next
        print("Current: ", current.data)
      current.next = newNode
      print("Current.next: ", current.next.data)
    else:
      self.head = newNode  
      print("es el HEAD: ", self.head.data)


  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next


LL=LinkedList()
LL.insert(10)
LL.printLL()
print("1------------")

LL.insert(20)
LL.printLL()
print("2--------------")

LL.insert(30)
LL.printLL()
print("3-------------")

LL.insert(40)
LL.printLL()
print("4-------------")

LL.insert(50)
LL.printLL()
print("5-------------")

#LL.printLL()

#printNodes()
#LL.printLL()

