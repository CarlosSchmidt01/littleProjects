class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return '{} not found'.format(lkpval)
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return '{} not found'.format(lkpval)
            return self.right.findval(lkpval)
        else:
            return '{} is found'.format(self.data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data) ,
        if self.right:
            self.right.printTree()

    def getHeight(self, tree):
        if tree != None:
            return max( tree.getHeight(tree.left), tree.getHeight(tree.right)) + 1
        else:
            return 0

    def isBST(self, node):
        min = float('-inf')
        max = float('inf')
        if node.data <= min:
            return False

        if node.data >= max:
            return False

        left_ok = True
        right_ok = True

        if node.left is not None:
            left_ok = node.isBST(node.left)
        if node.right is not None:
            right_ok = node.isBST(node.right)

        return left_ok and right_ok

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(11)
root.insert(17)
root.insert(1)
root.insert(7)
root.insert(20)
root.insert(22)
root.insert(25)

#root.printTree()
#print(root.findval(7))
#print(root.findval(14))
#root.printTree()
#print(root.getHeight(root))

print(root.isBST(root))
