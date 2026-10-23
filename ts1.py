def reverse_list(arr: list) -> list | None:
    if not isinstance(arr, list):
        raise TypeError('Нужен список')

    new_arr = []
    for i in range(len(arr) - 1, -1, -1):
        new_arr.append(arr[i])

    return new_arr

print(reverse_list([1, 2, 3, 4]))
print(reverse_list('aaa'))