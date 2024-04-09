def sort_string_array(array: list[str], desc: bool = False) -> list[str]:
    sorted_array = sorted(array, key=lambda x: len(x))
    if desc:
        return list(reversed(sorted_array))

    return sorted_array
