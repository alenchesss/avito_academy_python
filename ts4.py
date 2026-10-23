def split_to_digits(num: int) -> list:
    if type(num) is not int or num < 0:
        raise ValueError('Число должно быть целым и неотрицательным')

    if num == 0:
        return [0]

    ans = []
    while num > 0:
        ans.insert(0, num % 10)
        num //= 10

    return ans

print(split_to_digits(105))
print(split_to_digits('105.1'))
#print(split_to_digits(105.1))
#print(split_to_digits(-105))
