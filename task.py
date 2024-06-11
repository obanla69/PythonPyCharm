import random


from itertools import count
def count_random_number():
    random.seed(50)
    numbers_list = []
    for i in range(10):
        numbers = random.randint(1,50)

        numbers_list.append(numbers)

    return numbers_list
print(count_random_number())


def find_my_length(numbers_length):
    count = 0
    for number in numbers_length:
        count += 1
    return count

def find_sum_even_elements(numbers_length):
    sum = 0
    for even in numbers_length:
        if even % 2 == 0:
            sum += even
    return sum

def find_sum_odd_elements(numbers_length):
    sum = 0
    for odd in numbers_length:
        if odd % 2 != 0:
            sum += odd
    return sum

def find_multiply_element(numbers_list):
    for number in range(len(numbers_list)):
        if(number + 1) % 3 == 0:
            numbers_list[number]= numbers_list[number]*2
    return numbers_list


def find_average_element(numbers_list):
    average = sum(numbers_list)/len(numbers_list)
    return average


def find_largest_element(numbers_list):
    largest = max(numbers_list)
    return largest

def find_smallest_element(numbers_list):
    smallest = min(numbers_list)
    return smallest

def find_sequential_element(numbers_list):
    numrange = 15
    numsequence = [i for i in range(numrange)for _ in range(2)]
    return numbers_list




def numbers_in_a_list_without_duplicate(numbers):
    numbers += numbers
    return numbers






