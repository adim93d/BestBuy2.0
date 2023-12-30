import products
import store


def menu_input():
    user_input = int(input("\n"
                           """Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
----------\nWhat would you like to do: """))
    return user_input


def menu_dispatch_table(user_input, shop):
    functions_dispatcher = {1: list_products,
                            2: show_inventory_quantity,
                            3: order
                            }
    if user_input in functions_dispatcher:
        return functions_dispatcher[user_input](shop)
    else:
        print("Invalid input. Try again.")
        return menu_dispatch_table(menu_input(), shop)


def list_products(shop):
    shop.get_all_products()
    user_input = menu_input()
    return menu_dispatch_table(user_input, shop)


def show_inventory_quantity(shop):
    shop.get_total_quantity()
    user_input = menu_input()
    return menu_dispatch_table(user_input, shop)


def order(shop):
    shop.order2()
    user_input = menu_input()
    return menu_dispatch_table(user_input, shop)


def start(shop):
    while True:
        user_input = menu_input()
        if user_input == 4:
            print("Goodbye!")
            break
        else:
            menu_dispatch_table(user_input, shop)


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
