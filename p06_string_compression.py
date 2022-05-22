def compress_string(str1: str) -> str:
    consecutive_count = 0
    result = ''

    for idx, char in enumerate(str1):
        consecutive_count += 1

        if idx + 1 >= len(str1) or char != str1[idx + 1]:
            result += f'{char}{consecutive_count}'
            consecutive_count = 0
    
    return result

def test_compress_string():
    assert compress_string('aabcccccaaa') == 'a2b1c5a3'