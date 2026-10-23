def count_odds_evens(num: int) -> dict:
    if type(num) is not int or num < 0:
        raise TypeError('Число должно быть целым и неотрицательным')

    ans = {'odds': 0, 'evens': 0}

    if num == 0:
        return {'odds': 0, 'evens': 1}

    while num > 0:
        dig = num % 10
        if dig % 2 == 0:
            ans['evens'] += 1
        else:
            ans['odds'] += 1
        num //= 10
    return ans

print(count_odds_evens(1012))
print(count_odds_evens(-120.5))