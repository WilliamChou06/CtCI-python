def is_one_away(str1: str, str2: str) -> bool:
    edit_count = abs(len(str1) - len(str2))
    print('edit_count: ', edit_count)

    # Checking if there's a replacement in the string
    for idx, char in enumerate(str1):
        if char != str2[idx]:
            edit_count += 1

    if edit_count == 1:
        return True
    else:
        return False

def test_one_away():
    assert is_one_away('cat', 'bat') == True
    assert is_one_away('cat', 'bak') == False
    assert is_one_away('person', 'persona') == True