def Vowels_String(string, vowels):
    results = [each for each in string if each in vowels]
    print(results)
string = "Umuzi"
vowels = "AaEeIiOoUu"
Vowels_String(string, vowels);