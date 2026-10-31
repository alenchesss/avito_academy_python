def main():
    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    print('Выручка за всю неделю =', sum(day['revenue'] for day in days))

    max_revenue = max(day['revenue'] for day in days)
    max_day = [day['day'] for day in days if day['revenue'] == max_revenue]
    print('День с самой большой выручкой =', ','.join(max_day))

    average_revenue = {
        day['day']: day['revenue'] / day['orders']
        for day in days
    }

    print('Cредняя выручка на один заказ в каждый день:')
    for day, revenue in average_revenue.items():
        print(f'День: {day}, средняя выручка: {revenue}')

    print('Дни, где возвратов больше 20% заказов:')
    for day in days:
        if day['returns'] / day['orders'] > 0.2:
            print(day['day'])


if __name__ == '__main__':
    main()
