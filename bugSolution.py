def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle it appropriately, perhaps by raising a custom exception or logging an error message.

result = my_function(10, 0)
print(result) # Output: 0