from typing import Iterable
def subtract_lists(first: Iterable, second: Iterable ) -> list:

    ans = []
    second = list(second)
    for item in first:
        if item in second:
            second.remove(item)
        else:
            ans.append(item)

    return ans

print(subtract_lists('qwerty','defxyz'))
print(subtract_lists(('one', 'two', 'three'), ('two', 'five', 'seven')))
print(subtract_lists([1,2,3,4,5],[2,3,7,8]))
print(subtract_lists({1:1, 2:2, 3:3},{2:2, 4:4}))
print(subtract_lists('ww','w'))
print(subtract_lists('wwewwe', 'e'))
