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
        """Prints the elements"""
        current = self.head;
        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def search_element(self, val):
        """Search for element in the list. If found, return True. It not found, return False"""
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() is val:
                found = True
            else:
                current = current.get_next()
        return found

    def remove_element(self, val):
        """Remove element from the list. If element not found, raise ValueError"""
        found = False
        previous = None
        current = self.head
        while current is not None and not found:
                if current.get_data() is val:
                    #previous.set_next(current.get_next())
                    found = True
                else:
                   previous = current
                   current = current.get_next()
        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        else:
            raise ValueError
            print("Value not found")
                   #print(current)
        #return removed




if __name__ == '__main__':
        myList = LinkedList()
        myList.add_element('S')
        myList.add_element('L')
        myList.add_element('I')
        print(myList.size())
        myList.print_element()
        print(myList.search_element('I'))
        print(myList.remove_element('I'))
        myList.print_element()