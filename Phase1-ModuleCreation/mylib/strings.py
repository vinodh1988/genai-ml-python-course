def reverse_string(s):
    """Reverse a string"""
    return s[::-1]


def count_vowels(s):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def capitalize_words(s):
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in s.split())


def remove_whitespace(s):
    """Remove all whitespace from string"""
    return ''.join(s.split())


def is_palindrome(s):
    """Check if string is a palindrome"""
    clean = remove_whitespace(s).lower()
    return clean == clean[::-1]


def count_words(s):
    """Count number of words in string"""
    return len(s.split())


def replace_vowels(s, replacement="*"):
    """Replace all vowels with a character"""
    vowels = "aeiouAEIOU"
    return ''.join(replacement if char in vowels else char for char in s)