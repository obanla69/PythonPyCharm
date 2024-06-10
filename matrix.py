

def even_list(oba):
    even_numbers = []
    for number in oba:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = list(range(1,51))
print(numbers)
print(even_list(numbers))