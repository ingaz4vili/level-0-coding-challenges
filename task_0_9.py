from ntpath import join


def vowels_string(text):
    vowels = "aeiuo"
    result = list()
    for letter in text: 
        ln = letter.lower()
        if ( ln in vowels ) and (ln not in result ):
            result.append(ln)
    print(','.join(result))
vowels_string("Umuzi")