


def my_length(word):
    if type(word) in [int,float]:
        raise ValueError("argument must be iterable")
    count = 0
    for letter in word:
        count += 1

    return count

