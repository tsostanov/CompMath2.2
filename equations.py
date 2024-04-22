import numpy as np


def first_system(x, y):
    equation1 = np.sin(x + 0.5) - y
    equation2 = np.cos(y - 2) + x
    return equation1, equation2


def second_system(x, y):
    equation1 = np.cos(x + 0.5) - y
    equation2 = np.sin(y - 2) + x
    return equation1, equation2


def first_jacobi_for_first(x, y):
    return np.cos(x + 0.5), -1


def second_jacobi_for_first(x, y):
    return 1, -1 * np.sin(y - 2)


def first_jacobi_for_second(x, y):
    return -1 * np.sin(x + 0.5), -1


def second_jacobi_for_second(x, y):
    return 1, np.cos(y - 2)

def print_first_system_description():
    print("Первая система уравнений:")
    print("/sin(x + 0.5) - y = 0")
    print("\cos(y - 2) + x = 0\n")


def print_second_system_description():
    print("Вторая система уравнений:")
    print("/cos(x + 0.5) - y = 0")
    print("\sin(y - 2) + x = 0\n")
