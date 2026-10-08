def main():
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]
    print("Сумма, на которую оформили возвраты:")
    print(sum(
        order["amount"] for order in orders
        if order["status"] == "returned"
    ))

    print("Кто хотя бы раз вернул заказ:")
    print(", ".join(
        order["buyer"] for order in orders
        if order["status"] == "returned"))

    print("Количество заказов, доставленных покупателю:")
    print(sum(1 for order in orders if order["status"] == "delivered"))

    print("Средний чек доставленных заказов:")
    delivered_orders = [order["amount"]
                        for order in orders
                        if order["status"] == "delivered"]
    print(sum(delivered_orders) / len(delivered_orders))


if __name__ == "__main__":
    main()
