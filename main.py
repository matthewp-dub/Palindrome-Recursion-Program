def enter_word():
    return input("Enter your word here: ").strip().lower()


def is_palindrome(text=enter_word(), low=0, high=None):
    if high is None:
        high = len(text) - 1
    if low > high:
        print("Its a palindrome")
        exit()
    elif text[low] == text[high]:
        print('Same')
        is_palindrome(text, low + 1, high - 1)
    else:
        print("Different")
        print("Not a palindrome")
        exit()


if __name__ == '__main__':
    is_palindrome()
