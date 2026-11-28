class Node:
    data: str

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
	head: Node

	def __init__(self, head):
		self.head = head

class DoubleEndedQueue(DoubleLinkedList):
    def push_left(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node

    def push_right(self, node):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
        node.prev = current_node

    def pop_left(self):
        pop_node = self.head
        self.head = self.head.next
        self.head.prev = None
        return pop_node
    
    def pop_right(self):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        pop_node = current_node
        current_node.prev.next = None
        return pop_node

    def print_left_right(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_right_left(self):     #Just to check id the prev pointers are working correctly
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev


#####################TESTS#####################

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

my_double_queue = DoubleEndedQueue(node1)
my_double_queue.push_right(node2)
my_double_queue.push_right(node3)
my_double_queue.push_right(node4)
my_double_queue.push_right(node5)
my_double_queue.push_right(node6)

print("Queue from left to right:")
my_double_queue.print_left_right()

print("Queue from right to left:")
my_double_queue.print_right_left()

my_double_queue.pop_left()
my_double_queue.pop_right()

print("Queue from left to right after popping left and right:")
my_double_queue.print_left_right()

#Testing the push_left method
node1_2 = Node("A")
node2_2 = Node("B")
node3_2 = Node("C")
node4_2 = Node("D")
node5_2 = Node("E")
node6_2 = Node("F")

my_double_queue2 = DoubleEndedQueue(node1_2)
my_double_queue2.push_left(node2_2)
my_double_queue2.push_left(node3_2)
my_double_queue2.push_left(node4_2)
my_double_queue2.push_left(node5_2)
my_double_queue2.push_left(node6_2)

print("Queue from left to right after pushing left:")
my_double_queue2.print_left_right()

print("Queue from right to left after pushing left:")
my_double_queue2.print_right_left()