import random, time

class BigONotation:

    def __init__(self, size_limit):
        self.data = []
        self.size = size_limit

    def generate_random_no(self):
        for i in range(self.size):
           self.data.append(random.randint(1,21)*5)

    def get_array_value(self):
        return self.data

    # O(1): An algorithm that takes same time to execute irrespective of amount of data
    # This algorithm is not affected by the array size either.
    
    def add_el(self, item):
        self.data.append(item)

    # O(N) : An algorithm whose time to complete is directly proportional to amount of data it is processing.
    # Single for loops, linear search is an example of  linear time
    # In the below example, as array size increases, time to find the value increases

    def linear_search_el(self, item):
        found = False
        index_val = ''
        start_time = int(round(time.time() * 1000))
        for i in range(self.size):
            if self.data[i] is item:
                found = True
                index_val = index_val + str(i) + ' '
        end_time = int(round(time.time() * 1000))
        print("Value found: " + str(found))
        print("Time taken to search for element " + str(end_time - start_time))


    # O(n ^ 2) : An algorithm who time to complete is directly proportional to square of amount of data.
    # Each pass to outer loop O(n) requires to go through entire list through inner loop.
    # Nested for-loops are example of quadratic time as we run a linear operation within other linear operation

    def bubble_sort(self):
        start_time = int(round(time.time() * 1000))
        data = self.data
        for i in range(len(data)):
            for j in range(len(data)-i-1):
                if data[j] > data[j + 1]:
                    data[j], data[j+ 1] = data[j + 1], data[j]


        end_time = int(round(time.time() * 1000))
        print("Time taken for Bubble Sort " + str(end_time - start_time))
        print(data)



if __name__ == '__main__':
    big_o = BigONotation(2000)
    big_o1 = BigONotation(4000)

    #  O(n) Test
    big_o.generate_random_no()
    big_o.linear_search_el(20)
    big_o1.generate_random_no()
    big_o1.linear_search_el(20)

    # O(n ^ 2) Test
    big_o.bubble_sort()
    big_o1.bubble_sort()



