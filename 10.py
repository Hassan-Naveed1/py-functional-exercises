#10.	Convert a list of lowercase words to uppercase using map().
list_of_words = ["paris","london","madrid","milan","coopenhagen"]
upper_case_words = map(lambda x:x.upper(),list_of_words)
print(tuple(upper_case_words))