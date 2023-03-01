from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    """
    iterate over half of string, check that first character matches reverse index
    O(n) T | O(1) S
    SSH test
    """
    start, end = 0, -1
    for i in range(len(s) // 2):
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
