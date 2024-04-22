from equations import first_system, second_system, first_jacobi_for_first, second_jacobi_for_first, \
    first_jacobi_for_second, second_jacobi_for_second
import numpy as np
from tabulate import tabulate


def newton_solver(equation_system, x_guess, y_guess):
    max_iterations = 100
    tolerance = 1e-6

    data = []

    for iteration in range(max_iterations):
        equations = equation_system(x_guess, y_guess)

        if equation_system.__name__ == "first_system":
            jacobi_matrix = np.array([
                first_jacobi_for_first(x_guess, y_guess),
                second_jacobi_for_first(x_guess, y_guess)
            ])
        else:
            jacobi_matrix = np.array([
                first_jacobi_for_second(x_guess, y_guess),
                second_jacobi_for_second(x_guess, y_guess)
            ])

        deltas = np.linalg.solve(jacobi_matrix, -np.array(equations))

        x_guess += deltas[0]
        y_guess += deltas[1]

        # norm = np.linalg.norm(deltas) # norm = sqrt(Δx**2 + Δy**2) - евклидова норма

        data.append([iteration, x_guess, y_guess, deltas[0], deltas[1]])

        if max(abs(i) for i in deltas) < tolerance:
            print("Решение найдено:")
            print("x =", x_guess)
            print("y =", y_guess)
            break

    else:
        print("Достигнуто максимальное количество итераций. Решение не найдено.")

    headers = ['Итерация', 'x', 'y', 'Δx', 'Δy']
    print(tabulate(data, headers=headers, tablefmt='pretty'))

