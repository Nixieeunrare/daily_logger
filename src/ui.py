def pick_category(categories: dict) -> str:
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Введите номер категории: ")) - 1
            if 0 <= choice < len(categories):
                return tuple(categories.keys())[choice]
            else:
                print("------------")
                print("Ошибка! Неверный номер.")
                print("------------")
        except ValueError:
            print("------------")
            print("Ошибка! Введите число(int).")
            print("------------")


def pick_doings(categories: dict, category_name: str) -> str:
    doings = categories[category_name]
    print(f"Дела в категории '{category_name}': ")
    for i, doing in enumerate(doings, 1):
        print(f"{i}. {doing}")

    while True:
        try:
            choice = int(input("Введите номер дела в категории: ")) - 1
            if 0 <= choice < len(doings):
                return doings[choice]
            else:
                print("------------")
                print("Ошибка! Неверный номер.")
                print("------------")
        except ValueError:
            print("------------")
            print("Ошибка! Введите число(int).")
            print("------------")


def how_much_value() -> int:
    while True:
        try:
            value = int(
                input("Введите единицу потраченную на дело(минуты, кол-во и т.д.): ")
            )
            return value
        except ValueError:
            print("------------")
            print("Ошибка! Введите число(int).")
            print("------------")
