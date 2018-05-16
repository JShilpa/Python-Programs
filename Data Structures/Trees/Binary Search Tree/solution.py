# Binary Search Tree with Traversals

class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val


class BinarySearchTree:
    def insert(self, root, node):
        if root is None:
            return node

        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)
        return root

    def in_order_place(self, root):
        if root:
            self.in_order_place(root.l_child)
            print(root.val, end=' ')
            self.in_order_place(root.r_child)

    def pre_order_place(self, root):
        if not root:
            return None

        else:
            print(root.val, end=' ')
            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)

    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print(root.val, end=' ')


r = Node(3)
node = BinarySearchTree()
nodeList = [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]
for nd in nodeList:
    node.insert(r, Node(nd))
print("------In order ---------")
node.in_order_place(r)
print('\n')
print("------Pre order ---------")
node.pre_order_place(r)
print('\n')
print("------Post order ---------")
node.post_order_place(r)
