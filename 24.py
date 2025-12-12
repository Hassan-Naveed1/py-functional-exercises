#24.	Remove empty strings from a list.
string_list = ["Hello","","Yes",""]
remove_empty = filter(lambda x : len(x) > 0, string_list)
print(tuple(remove_empty))