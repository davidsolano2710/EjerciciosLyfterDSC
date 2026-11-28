class Node:
    data: str

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
	head: Node

	def __init__(self, head):
		self.head = head

class Stack(LinkedList):
    def push(self, node):
        node.next = self.head       #the new node points to the current head
        self.head = node            #the new node becomes the new head
        return
    
    def pop(self):
        pop_node = self.head        #the node to be popped is the current head
        self.head = self.head.next  #the new head is the next node in the list
        return pop_node

    def print_stack_with_counter(self):
        current_node = self.head
        counter = 1
        while current_node is not None:
            print(f"Node {counter}:")
            print(current_node.data)
            current_node = current_node.next
            counter += 1

    def print_stack(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


#####################TESTS#####################
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

my_stack = Stack(node1)
my_stack.push(node2)
my_stack.push(node3)
my_stack.push(node4)
my_stack.push(node5)

print("First stack print:")
my_stack.print_stack_with_counter()
my_stack.pop()
my_stack.pop()
my_stack.push(node6)
print("Second stack print:")
my_stack.print_stack()

