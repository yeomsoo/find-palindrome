
word = str(input("Write your word: "))

def is_palindrome(word):
    left, right = 0, len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left, right = left + 1, right - 1
    return True
