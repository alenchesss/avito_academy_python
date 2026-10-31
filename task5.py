def main():
    reviews = [
        {'id': 1, 'product': 'Чехол', 'stars': 5},
        {'id': 1, 'product': 'Чехол', 'stars': 3},
        {'id': 1, 'product': 'Чехол', 'stars': 4},
        {'id': 2, 'product': 'Наушники', 'stars': 2},
        {'id': 2, 'product': 'наушники', 'stars': 2},
        {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
        {'id': 3, 'product': 'Планшет', 'stars': 5},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 5, 'product': 'Кабель', 'stars': 1},
    ]

    print('Средняя оценка каждого товара:')
    for review in reviews:
        review['product'] = review['product'].lower().capitalize()

    products = {}
    averages = {}
    for item in reviews:
        if item['product'] not in products:
            products[item['product']] = []

        products[item['product']].append(item['stars'])

    for product, stars in products.items():
        avg = sum(stars) / len(stars)
        averages[product] = avg
        print(f'{product}: {avg:.2f}')

    bad_product = min(
        (product for product in products if len(products[product]) >= 2),
        key=lambda product: averages[product]
    )

    print('Худший товар:', bad_product)

    negative_reviews = sum(
        1 for review in reviews
        if review['stars'] == 1 or review['stars'] == 2)
    print('Количество отзывов на 1 или 2 звезды:', negative_reviews)
    print('Они составляют долю =', negative_reviews / len(reviews))


if __name__ == '__main__':
    main()
