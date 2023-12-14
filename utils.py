def max_numbers(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            max = number
    return max