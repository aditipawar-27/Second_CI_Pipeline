def most_frequent(numbers):
    if not numbers:
        return None

    return max(set(numbers), key=numbers.count)