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
        print("Value found " + str(found))
        print("Time taken " + str(end_time - start_time))


    def bubble_sort(self, data):
        for i in range(len(data)):
            for j in range(len(data)-i-1):
                if data[j] > data[ j + 1]:
                    temp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = temp
        print(data)



if __name__ == '__main__':
    big_o = BigONotation(100000)
    big_o.generate_random_no()
    #print(big_o.get_array_value())
    big_o.linear_search_el(20)

    big_o1 = BigONotation(200000)
    big_o1.generate_random_no()
    big_o1.linear_search_el(20)
    big_o1.bubble_sort([5,2,10,1,7, 3])

