from functools import reduce


def composition(num1, num2):
    return num1 * num2


numbers = [number for number in range(100, 1001) if number % 2 == 0]

print(reduce(composition, numbers))
