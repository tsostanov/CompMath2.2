import numpy as np
import matplotlib.pyplot as plt
from equations import first_system, second_system, print_first_system_description, print_second_system_description
from newton import newton_solver

def plot_equations(equation_system):
    x_values = np.linspace(-5, 5, 100)
    y_values = np.linspace(-5, 5, 100)

    X, Y = np.meshgrid(x_values, y_values)

    Z1, Z2 = equation_system(X, Y)

    plt.figure(figsize=(8, 6))
    plt.contour(X, Y, Z1, levels=[0], colors='blue', linewidths=2, linestyles='solid')
    plt.contour(X, Y, Z2, levels=[0], colors='red', linewidths=2, linestyles='solid')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График системы уравнений')
    plt.grid(True)
    plt.show()


def choose_equation_system():
    while True:
        print("Выберите систему уравнений:")
        print_first_system_description()
        print_second_system_description()

        choice = input("Введите номер системы (1 или 2): ")

        if choice == '1':
            print_first_system_description()
            return first_system
        elif choice == '2':
            print_second_system_description()
            return second_system
        else:
            print("Некорректный выбор. Пожалуйста, введите номер системы заново.")


def main():
    equation_system = choose_equation_system()
    if equation_system:
        print("Выбранная система:", equation_system.__name__)
        plot_equations(equation_system)

        while True:
            try:
                x_guess = float(input("Введите начальное приближение для переменной x: "))
                y_guess = float(input("Введите начальное приближение для переменной y: "))

                if not (np.isfinite(x_guess) and np.isfinite(y_guess)):
                    raise ValueError("Введены некорректные значения. Пожалуйста, введите числа.")

                print("Начальное приближение для x:", x_guess)
                print("Начальное приближение для y:", y_guess)

                break
            except ValueError as e:
                print(e)
        newton_solver(equation_system, x_guess, y_guess)


if __name__ == "__main__":
    main()
