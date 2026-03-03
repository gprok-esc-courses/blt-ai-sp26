
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 
        self.height = 1

    def __str__(self):
        return str(self.value)


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height 
    
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def insert(self, node, value):
        if node is None:
            return TreeNode(value)
        elif value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.inser(node.right, value)

        # Update the height
        node.height = 1 + max(self.height(node.left), self.height(node.right))  
        balance = self.balance(node) 

        # Right rotate
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        
        # Left rotate
        if balance < -1 and value > node.right.value:
            pass

        # Left Right rotate 
        if balance > 1 and value > node.right.value: 
            pass 

        # Right Left rotate
        if balance < -1 and value < node.left.value:
            pass

        return node
    
    def right_rotate(self, node):
        temp = node.left
        node.left = temp.right 
        temp.right = node

        temp.height = 1 + max(self.height(temp.left), self.height(temp.right))
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        return temp

    def insert_value(self, value):
        self.root = self.insert(self.root, value)
