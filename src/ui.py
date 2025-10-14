from src.logic import (
    add_new_category,
    add_new_subcategory,
    load_from_data,
    log_activity,
    statistics,
)
from src.storage import load_categories
from src.visualization import visualization_subcategory_bar


class Menu:
    ADD_NEW_DOING_LOG = "1"
    ADD_NEW_CATEGORY = "2"
    ADD_NEW_SUBCATEGORY = "3"
    SHOW_STATISTIC = "4"
    PLOT_VISUALIZATION = "5"
    QUIT = "6"


def show_menu():
    print("\n===Daily Tracker by nixiee===")
    print(f"{Menu.ADD_NEW_DOING_LOG}. Записать активность")
    print(f"{Menu.ADD_NEW_CATEGORY}. Добавить новую категорию")
    print(f"{Menu.ADD_NEW_SUBCATEGORY}. Добавить новую подкатегорию")
    print(f"{Menu.SHOW_STATISTIC}. Посмотреть статистику активности")
    print(f"{Menu.PLOT_VISUALIZATION}. Посмотреть визуализацию активности")
    print(f"{Menu.QUIT}. Выход")


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
    if stats["today_value"] is not None:
        print(f"- Сегодня: ✅ {stats['today_value']}")
    else:
        print("- Сегодня: ❌ не отмечено")


def add_log_flow():
    categories = load_categories()
    category = pick_category(categories)
    doing = pick_doings(categories, category)
    value = how_much_value()
    print()
    log_activity(doing, value)


def add_category_flow():
    add_new_category(input("Название категории: "))


def add_subcategory_flow():
    categories = load_categories()
    category = pick_category(categories)
    add_new_subcategory(category, input("Название подкатегории: "))


def show_statistics_flow():
    categories = load_categories()
    category = pick_category(categories)
    doing = pick_doings(categories, category)
    data = load_from_data()
    stats = statistics(doing, data)
    print()
    show_statistics(doing, stats)


def show_plot_flow():
    categories = load_categories()
    category = pick_category(categories)
    doing = pick_doings(categories, category)
    data = load_from_data()
    visualization_subcategory_bar(data, doing)
