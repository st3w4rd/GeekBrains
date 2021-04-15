def my_pow_func(x, y):
    return 1 if y == 0 else my_pow_func(x, y + 1) * 1 / x

print(my_pow_func(2, -3))