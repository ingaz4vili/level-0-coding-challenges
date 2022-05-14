import collections as ct
def vowels_string(text):
    vowels = "aeiuo" 
    result = [letter for letter in text.lower() if letter in vowels]
    print(" ,".join(ct.OrderedDict.fromkeys(result)))
vowels_string("Umuzi")