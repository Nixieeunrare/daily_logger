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
            if value <= 0:
                print("------------")
                print("Ошибка! Введите число(int) больше 0.")
                print("------------")
                continue
            else:
                return value
        except ValueError:
            print("------------")
            print("Ошибка! Введите число(int).")
            print("------------")

def show_statistics(doing: str, stats: dict):
    if "err" in stats:
        print()
        print(f"Данные по делу {doing} -- отсутствуют.")
        return
    print()
    print(f"\n📊 Статистика по '{doing}':")
    print(f"- Всего дней: {stats['total_days']}")
    print(f"- Всего: {stats['total_value']}")
    print(f"- Среднее: {stats['average']}")
    print(f"- Последняя запись: {stats['last_date']} — {stats['last_value']}")
    if stats['today_value'] is not None:
        print(f"- Сегодня: ✅ {stats['today_value']}")
    else:
        print("- Сегодня: ❌ не отмечено")
