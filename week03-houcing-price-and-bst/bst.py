# Binary Search Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 

    def __str__(self):
        return str(self.data) 
    
class BST:
    def __init__(self):
        self.root = None 

    def display(self):
        self.inorder(self.root)

    def inorder(self, root_node):
        if root_node.left is not None:
            self.inorder(root_node.left)
        print(root_node)
        if root_node.right is not None:
            self.inorder(root_node.right)

    def add(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node 
        else:
            iter = self.root
            while True:
                if iter.data > data:
                    if iter.left is None:
                        iter.left = node 
                        break
                    else:
                        iter = iter.left 
                else:
                    if iter.right is None:
                        iter.right = node 
                        break 
                    else:
                        iter = iter.right


tree = BST()
tree.add(100)
tree.add(67)
tree.add(230)
tree.add(31)
tree.add(55)
tree.add(150)
tree.add(256)
tree.add(81)
tree.display()