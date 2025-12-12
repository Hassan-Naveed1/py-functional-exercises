#21.	Keep only numbers greater than the average of the list.
list_nums = [1,2,3,4,5,6,7,8,9,10]
average_list = sum(list_nums) / len(list_nums)
num_greater_avg = filter(lambda x : x > average_list,list_nums)
print(tuple(num_greater_avg))