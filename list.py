#Accept user input as list of integers
num = input("Enter numbers separated by spaces: ")
int_list = [int(x) for x in num.split()]

#compute the sum 
total_sum = sum(int_list)
print("The sum of the numbers is:", total_sum)