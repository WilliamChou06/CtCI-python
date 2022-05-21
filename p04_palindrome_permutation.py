def is_palindrome_permutation(str: str) -> str:
    stripped_str = str.replace(' ', '')
    char_count = {i : stripped_str.count(i) for i in stripped_str}

    char_list = sorted(char_count.values())

    if any(x % 2 != 0  for x in char_list[1:]):
        return False

    if char_list[0] == 1 and all(x % 2 == 0 for x in char_list[1:]):
        return True

def is_palindrome_permutation_pythonic(str: str) -> str:
    stripped_str = str.replace(' ', '')
    char_count = {i : stripped_str.count(i) for i in set(stripped_str)}
 
    return sum(x % 2 for x in char_count.values()) == 1
    

def test_palindrome_permutation():
    assert is_palindrome_permutation('taco cat') == True
    assert is_palindrome_permutation('dog cat') == False
    assert is_palindrome_permutation('madam') == True
    assert is_palindrome_permutation('racecar') == True
    assert is_palindrome_permutation('sausage') == False

    assert is_palindrome_permutation_pythonic('taco cat') == True
    assert is_palindrome_permutation_pythonic('dog cat') == False
    assert is_palindrome_permutation_pythonic('madam') == True
    assert is_palindrome_permutation_pythonic('raceeecar') == True
    assert is_palindrome_permutation_pythonic('sausage') == False
