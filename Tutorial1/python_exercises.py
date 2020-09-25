
"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    return (x % 2 == 1)


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    for i in range(len(word) // 2):
        if (word[i] != word[len(word) - i - 1]):
            return False

    return True

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist
    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    new_list = []

    for i in numlist:
        if (i % 2 == 1):
            new_list.append(i)

    return new_list

def count_words(text):
    """
    return a dictionary of {word: count} in the text
    words should be split by spaces (and nothing else)
    words should be converted to all lowercase
    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    dict = {}
    text = text.lower()
    text_list = list(text.split(" "))

    for i in text_list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict


#if __name__ == "__main__":
#    print(is_odd(2))                                    #False
#    print(is_odd(3))                                    #True
#    print(is_palindrome("fuck"))                        #False
#    print(is_palindrome("shihs"))                       #True
#    print(only_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))   #[1, 3, 5, 7, 9]
#    print(count_words("How much wood would a woodchuck chuck"
#                    " if a woodchuck could chuck wood?"))
