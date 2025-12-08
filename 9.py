#9.	Extract the length of each word in a list using map().
list_of_words = ["Paris","London","Madrid","Milan","Coopenhagen"]
length_each_word = map(lambda x : len(x),list_of_words)
print(tuple(length_each_word))