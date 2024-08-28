def filter_even_numbers(numbers):
    even_numbers = tuple(num for num in numbers if num % 2 == 0)
    return even_numbers

numbers = (1, 2, 3, 4, 5, 6)
result = filter_even_numbers(numbers)
print(result)