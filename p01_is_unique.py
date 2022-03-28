def is_unique(str):
    unique_chars = []
    for char in str.lower():
        if char in unique_chars:
            return False

        unique_chars.append(char)

    return True


def test_is_unique():
    assert is_unique('hello') == False
    assert is_unique('person') == True
    assert is_unique('Mac') == True
    assert is_unique('Hhey') == False
