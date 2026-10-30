def move_zeros(numbers):
    result = [num for num in numbers if num != 0]
    zero_count = numbers.count(0)

    return result + [0] * zero_count