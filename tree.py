
class Node:
    def __init__(self, datum):
        self.datum = datum
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self, data):
        if not data:
            self.root = None
        else:
            first = data[0]
            rest = data[1:]

        self.root = Node(first)
        for datum in rest:
            self.insert(datum)

    def insert(self, datum):
        current = self.root
        new = Node(datum)

        while current != None:

            if datum > current.datum:
                if current.right == None:
                    current.right = new
                    return
                else:
                    current = current.right
                
            elif current.left == None:
                current.left = new
                return

            else:
                current = current.left

    # applies proc to every piece of datum in the tree
    def apply(self, proc, root = None):
        if root == None:
            root = self.root
        
        if root.left != None:
            self.apply(proc, root.left)

        proc(root.datum)

        if root.right != None:
            self.apply(proc, root.right)

    # prints data in tree, sorted from smallest to largest
    def print(self, root = None):
        
        if root == None:
            root = self.root

        if root.left != None:
            self.print(root.left)

        print(root.datum)

        if root.right != None:
            self.print(root.right)



bt = binarySearchTree([6, 3, 4, 17, 14])
bt.print()
print()
bt.apply(lambda x : x + 1)
bt.print()



