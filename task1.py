def main():
    moscow_products = {201, 202, 203, 204}
    kazan_products = {203, 204, 205, 206}

    print('Товары в любом из городов:', moscow_products & kazan_products)
    print('Товары только в Москве:', moscow_products - kazan_products)
    print('Товары только в Казани:', kazan_products - moscow_products)
    print('Количество разных товаров:', len(moscow_products | kazan_products))


if __name__ == '__main__':
    main()
