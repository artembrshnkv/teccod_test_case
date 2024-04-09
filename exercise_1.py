def find_unique_elements1(array: list[int]) -> list[int]:
    return list(set(array))


# without using built-in set function
def find_unique_elements2(array: list[int]) -> list[int]:
    sorted_array = []
    for number in array:
        if number not in sorted_array:
            sorted_array.append(number)

    return sorted_array
