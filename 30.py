#30.	Keep only strings that start with a vowel.
strings = ["Hello","Tulsi","Movie","Friday","Fly","Gym","apple","Internet"]
vowels = ["A","I","E","O","U"]
no_vowel = filter(lambda x : x[0].upper() in vowels ,strings)
print(tuple(no_vowel))