#23.	Keep only words longer than 5 characters.
strings_list = ["Hello","Tulsi","Beautiful","Python"]
longer_5 = filter(lambda x : len(x) > 5,strings_list)
print(tuple(longer_5))