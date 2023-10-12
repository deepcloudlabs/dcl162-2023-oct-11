numbers = [4, 8, 15, 16, 23, 42]


def fun(nums: list[int]) -> list[int]:
    result = []
    for number in nums:
        result.append(number ** 3)
    return result


def gun(nums: list[int]) -> list[int]:
    for number in nums:
        cube = number ** 3
        print(f"[gun] number ** 3: {cube}")
        yield cube


for num in gun(numbers):
    print(f"[for loop] num: {num}")
