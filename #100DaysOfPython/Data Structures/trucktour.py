# Python program for implementing below HacekerRank challenge
# https://www.hackerrank.com/challenges/truck-tour/problem

from collections import defaultdict

n = int(input("Enter no of petrol pumps on circle"))
queue = defaultdict(list)
for i in range(n):
    data = input("Enter petrol pump data")
    #print(data)
    data_list = data.split();
    node_data = list(map(int, data_list))
    #(node_data)
    queue[i] = node_data
print(queue)
total_distance=0
for k,v in queue.items():
    total_distance = total_distance + v[1]
print(total_distance)
while len(queue) != 0:
    for k,v in queue.items():
