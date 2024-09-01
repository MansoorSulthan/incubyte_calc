def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    nums = map(int, numbers.split(","))
    return sum(nums)


