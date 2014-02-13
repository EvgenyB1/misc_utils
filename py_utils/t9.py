def key_combo(char):
    """ Converts char to T9 mobile keypad presses
    >>>t9.key_combo('a')
    2
    >>>t9.key_combo('B')
    22
    """
    if len(char) > 1:
        raise ValueError("Function expects single char")
    keypad = {"2": ["A", "B", "C"], "3": ["D", "E", "F"],
        "4": ["G", "H", "I"], "5": ["J", "K", "L"],
        "6": ["M", "N", "O"], "7": ["P", "Q", "R", "S"],
        "8": ["T", "U", "V"], "9": ["W", "X", "Y", "Z"],
        "0": [" "]}
    char = char.upper()
    for key in keypad:
        if char in keypad[key]:
            return key * (keypad[key].index(char) + 1)


def string(string):
    """ Returns T9 mobile keypad representation of string.
    Uses ' ' to indicate pause between characters on same key
    >>> t9.string('AA')
    2 2
    >>> t9.string('foo  bar')
    333666 6660 022 2777
    """
    keypad_string = [' ']
    for char in string:
        t9_key = key_combo(char)
        # If the last key_combo ends with
        # the first character of the current key_combo
        # append space for pause
        if keypad_string[-1].endswith(t9_key[:1]):
            keypad_string.append(' ')
        keypad_string.append(t9_key)
    return ''.join(keypad_string).lstrip()
