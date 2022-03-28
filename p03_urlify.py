def urlify(str: str) -> str:
    split_str = str.strip().split()
    return '%20'.join(split_str)

def urlify_pythonic(str: str, length: int) -> str:
    return str[:length].replace(' ', '%20')

def urlify_algorithm(string: str, length: int) -> str:
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])

    

def test_urlify():
    assert urlify('wow hello there') == 'wow%20hello%20there'
    assert urlify('dog cat ') == 'dog%20cat'
    assert urlify('person doing something') == 'person%20doing%20something'

    assert urlify_pythonic('wow hello there', 15) == 'wow%20hello%20there'
    assert urlify_pythonic('dog cat ', 7) == 'dog%20cat'
    assert urlify_pythonic('person doing something', 22) == 'person%20doing%20something'

    assert urlify_algorithm('wow hello there      ', 15) == 'wow%20hello%20there'
    assert urlify_algorithm('dog cat   ', 7) == 'dog%20cat'
    assert urlify_algorithm('person doing something      ', 22) == 'person%20doing%20something'