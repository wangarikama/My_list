#input two sets
set1 = set(map(int, input("Enter integers for set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for set 2 separated by spaces: ").split()))

#find the common elements
common_set = set1 & set2
print("Common elements:", common_set)