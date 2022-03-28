def convert_name_to_pig_latin(firstname, lastname):
    firstname_converted = convert_word_to_pig_latin(firstname)
    lastname_converted = convert_word_to_pig_latin(lastname)
    firstname_converted = firstname_converted.capitalize()
    return f"{firstname_converted}, {lastname_converted}"


def convert_word_to_pig_latin(word):
    new_word = word.lower()

    if word[0] in 'aeiou':
        return new_word + "ay"
    else:
        has_vowel = False

        for i, letter in enumerate(new_word):
            if letter in 'aeiou':
                new_word = new_word[i:] + new_word[:i] + "ay"
                has_vowel = True
                break

        if not has_vowel:
            new_word = new_word + "ay"

        return new_word
