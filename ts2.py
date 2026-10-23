def drop_dups(data : list | tuple | str) -> list | tuple | str:
    if not isinstance(data, (list, tuple, str)):
        raise TypeError('Нужна последовательность')

    res = []

    for el in data:
        if el not in res:
            res.append(el)

    return ''.join(res) if isinstance(data, str) else type(data)(res)

print(drop_dups('qqqqqaaaarraaaty'))
print(drop_dups(('one', 'two', 'one', 'two', 'three', 'one')))
#print(drop_dups(1111))
print(drop_dups({1:1, 2:2, 3:3}))