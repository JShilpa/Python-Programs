#


class BinaryTree:
    def __init__(self, val):
        self.value = val
        self.l_child = None
        self.r_child = None

    def get_left_child(self):
        return self.l_child

    def get_right_child(self):
        return self.r_child

    def get_root(self):
        return self.value

    def insert_left(self, value):
        if self.l_child is None:
            self.l_child = value
        else:
            new_node = BinaryTree(value)
            new_node.l_child = self.l_child
            self.l_child = new_node

    def insert_right(self, value):
        if self.r_child is None:
            self.r_child = value
        else:
            new_node = BinaryTree(value)
            new_node.r_child = self.r_child
            self.r_child = new_node


def print_tree(tree):
    if tree is not None:
        print(tree.get_left_child())
        print(tree.get_root())
        print(tree.get_right_child())

def testTree():
    my_tree = BinaryTree("Maud")
    my_tree.insert_left("Bob")
    my_tree.insert_right("Tony")
    print_tree(my_tree)

testTree()
