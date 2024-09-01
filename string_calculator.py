def add(numbers):
    if numbers == "":
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    numbers = numbers.replace("\n", delimiter)
    nums = numbers.split(delimiter)
    nums = [int(num) for num in nums if num]
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(
            f"Negative numbers not allowed: {', '.join(map(str, negatives))}"
        )
    return sum(nums)
