def print_upper_words(words, start):
    """Print each word on sep line, uppercased, if starts with one of given
    prefixes.
    """
    for word in words:
        for letter in start:
            if(word.startswith(letter)):
                print(word.upper())
                break

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],start={"h", "y"})