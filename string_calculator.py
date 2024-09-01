def add(numbers):
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
        numbers = numbers.replace(delimiter, ",")
    else:
        numbers = numbers.replace("\n", ",")
    nums = map(int, numbers.split(","))
    return sum(nums)


