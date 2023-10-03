# TASK --- Hacker Rank
# Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers,
# 0 being the first number.
# Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        return []
    fibonacci_list = [0]
    a, b = 0, 1

    for _ in range(1, n):
        fibonacci_list.append(b)
        a, b = b, a + b

    return list(map(cube, fibonacci_list))


print(fibonacci(0))
