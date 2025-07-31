#create an empty list
my_list = []

#append 10,20,30,40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
 #insert  15 at the second position in the list.
my_list.insert(1, 15)
print('List after inserting 15 at index 1:', my_list)

#Extend the list with 50,60,70
my_list.extend([50, 60, 70])
print('List after extending with 50, 60, 70:', my_list)

#Remove the last element from my_list.
my_list.pop()
print('List after removing the last element:', my_list)

#Sort my_list in ascending order.
my_list.sort()
print('List after sorting in ascending order:', my_list)

#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print('Index of 30 in my_list:', index_of_30)
