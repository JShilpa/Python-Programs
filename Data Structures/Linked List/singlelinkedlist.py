class Node:

    def __init__(self, val):
        self.data = val
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next(self):
        return self.next

    def set_next(self, val):
        self.next = val


class LinkedList:

    def __init__(self):
        self.head = None;

    def add_element(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
       # print(new_node.get_next())

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.get_next()
        return count

    def print_element(self):
        current = self.head;
        while current is not None:
            print(current.get_data())
            current = current.get_next()

if __name__ == '__main__':
        myList = LinkedList()
        myList.add_element('L')
        myList.add_element('I')
        print(myList.size())
        myList.print_element()