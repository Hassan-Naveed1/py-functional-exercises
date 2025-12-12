#25.	Keep only numbers ending with digit 5.
string_list = [12345,123,234,11,65,105]
string_list2 = []
for i in string_list:
        string_list2.append(str(i))
print(string_list2)
ending_5 = filter(lambda x : x[-1] == "5",string_list2)
print(tuple(ending_5))