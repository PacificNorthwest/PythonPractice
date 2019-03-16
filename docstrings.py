def is_palindrome(word):
    """
    Returns true if the word is a palindrome
    
    Args:
        word: A target word
    Returns:
        True if word is a palindrome. Othervise False
    """
    return word == word[::-1]

word = 'road'
is_palindrome(word)