from typing import Iterable
def count_nonunique(data: Iterable) -> int:
    counts = {}

    for el in data:
        counts[el] = counts.get(el, 0) + 1

    return sum(value > 1 for value in counts.values())

print(count_nonunique([1, 2, 3, 4, 5, 6, 1]))
print(count_nonunique('qqqwwertyyy'))
print(count_nonunique(('one', 'two', 'one', 'three')))