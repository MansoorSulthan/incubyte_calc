def add(numbers):
    if numbers == "":
        return 0
    nums = map(int, numbers.split(","))
    return sum(nums)


