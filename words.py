def print_upper_words(string):
    """Print each word on sep line, uppercased.

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """
    for str in string:
        print(str.upper())


def print_upper_words2(string):
    """Print each word on sep line if starts with E or e.

        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """

    index = 0
    
    for str in string:
        if str[index] == 'e':
            print(str)


def print_upper_words3(string, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given letters

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    index = 0

    for str in string:
        for letter in must_start_with:
            if letter.lower() == str[index].lower():
                print(str.upper())


