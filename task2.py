def main():
    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone',
    ]
    queries_dict = {}
    for item in queries:
        queries_dict[item] = queries_dict.get(item, 0) + 1

    print('Общее число поисковых запросов:', len(queries))
    for query, count in queries_dict.items():
        print(f'Запрос: \'{query}\', количество: {count}')

    frequent_query = max(queries_dict, key=queries_dict.get)
    print(
        f'Самый частый запрос: \'{frequent_query}\', '
        f'{queries_dict[frequent_query]}'
    )

    print(
        f'Доля \'{frequent_query}\' = '
        f'{round(queries_dict[frequent_query] / len(queries), 4)}'
    )

    for query, count in queries_dict.items():
        if count == 1:
            print(f'Запрос \'{query}\' встретился один раз')


if __name__ == '__main__':
    main()
