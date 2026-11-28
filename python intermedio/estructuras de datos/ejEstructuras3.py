class TreeNode():
    data: int

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()  


class BinaryTree(TreeNode):
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)   #I know this is probably wrong bu i cant figure out how to use the insert
                                         #method from BinaryTree instead of TreeNode, but it works so im leaving it for now
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)


    # def print_tree_levels(self):      #tried to implement a level order traversal but couldn't get it to work

    #     print(self.data)
    #     if self.left:
    #         self.left.print_tree_levels()
    #     if self.right:
    #         self.right.print_tree()


my_tree = BinaryTree(10)
my_tree.insert(5)
my_tree.insert(15)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(12)
print("Binary Tree Print:")
my_tree.print_tree()
