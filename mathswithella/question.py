
import random

def order_positive_decimals():
    numbers = []
    for number in range(5):
        numbers.append(round(random.random(), 2))

    question = {
        'random_floats': numbers,
        'answer': sorted(numbers),
    }
    return question

def order_numbers():
    numbers = []
    for number in range(5):
        numbers.append(random.randint(-17, 20))

    question = {
        'random_floats': numbers,
        'answer': sorted(numbers),
    }
    return question

def convert_percentage():
    random_float = round(random.random(), 2)

    question = {
        'random_float': str(random_float),
        'answer': str(random_float*100)+'%',
    }
    return question