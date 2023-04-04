ages = [5, 12, 17, 18, 24, 32]

def my_func(x):
    if x > 17:
        return True
    else:
        return False

adults =filter(my_func, ages)
print((list(adults)))
