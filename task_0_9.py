def vowels_string(text):
    vowels = "aeiuo" 
    result = [letter for letter in text.lower() if letter in vowels]
    print("Vowels:",(result))
vowels_string("Umuzi")