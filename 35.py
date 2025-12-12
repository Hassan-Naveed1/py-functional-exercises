#35.	Filter words shorter than 6 letters and then convert them to uppercase.
words = ["Banana","Tulsi","StrawBerry","Game"]
filter_words_shorter = map(lambda x : x.upper(), filter(lambda x : len(x) < 6, words))
print(tuple(filter_words_shorter))