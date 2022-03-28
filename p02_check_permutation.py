def check_permutation(str1, str2):
    char_count_1 = {}
    char_count_2 = {}
    
    for char in str1.lower():
        if char in char_count_1:
            char_count_1[char] += 1
        else:
            char_count_1[char] = 1

    for char in str2.lower():
        if char in char_count_2:
            char_count_2[char] += 1
        else:
            char_count_2[char] = 1

    if char_count_1 == char_count_2:
        print('char_count_2: ', char_count_2)
        print('char_count_1: ', char_count_1)
        return True
        
    return False

def check_permutation_sorted(str1, str2):
    sorted_str1 = sorted(str1.lower())
    sorted_str2 = sorted(str2.lower())

    if len(sorted_str1) == len(sorted_str2):
        if sorted_str1 == sorted_str2:
            return True
    return False
            


def test_check_permutation():
    assert check_permutation('hello', 'olleh') == True
    assert check_permutation('dog', 'god') == True
    assert check_permutation('Mac', 'cam') == True
    assert check_permutation('wawa', 'wawe') == False
    # sorting algorithm
    assert check_permutation_sorted('hello', 'olleh') == True
    assert check_permutation_sorted('dog', 'god') == True
    assert check_permutation_sorted('Mac', 'cam') == True
    assert check_permutation_sorted('wawa', 'wawe') == False
