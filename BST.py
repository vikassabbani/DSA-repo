class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def findvalue(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + 'Not Found'
            return self.left.findvalue(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + 'Not Found'
            return self.right.findvalue(val)

    def minn(self):
        if self.left is not None:
             return self.left.minn()
        return self.data

    def maxx(self):
        if self.right is not None:
            return self.right.maxx()
        return self.data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Node(10)
root.insert(6)
root.insert(15)
print(root.maxx())
print(root.minn())
root.PrintTree()