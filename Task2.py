import random
import scipy.integrate as spi


def f(x):
    return x ** 2


def main():
    # Межі інтегрування та кількість випадкових точок
    a = 0
    b = 2
    num_experiments = 500_000

    # Максимальне значення функції на відрізку [0, 2] — f(2) = 4
    min_y = 0
    max_y = f(b)

    # Генерація випадкових точок і підрахунок тих, що потрапили під криву
    inside_points = 0
    for _ in range(num_experiments):
        x_rand = random.uniform(a, b)
        y_rand = random.uniform(min_y, max_y)

        if y_rand <= f(x_rand):
            inside_points += 1

    # Площа прямокутника, у якому генеруються точки
    rectangle_area = (b - a) * (max_y - min_y)

    # Оцінка площі під кривою методом Монте-Карло
    monte_carlo_result = rectangle_area * (inside_points / num_experiments)
    print(f"Результат методом Монте-Карло: {monte_carlo_result}")

    # Перевірка через SciPy (spi.quad)
    result, error = spi.quad(f, a, b)
    print("Аналітичний розрахунок (quad):", result, f"(похибка: {error})")


if __name__ == "__main__":
    main()
