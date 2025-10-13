from src.logic import log_activity, statistics, add_new_category, add_new_subcategory
from src.storage import load_categories, load_from_data
from src.ui import pick_category, pick_doings, how_much_value, show_statistics


def main():

    while True:
        print("Tracker by nixie -- pre-alpha(0.1.4)")
        print("\n1. Записать активность")
        print("2. Посмотреть статистику")
        print("3. Добавить новую категорию")
        print("4. Добавить новую подкатегорию")
        print("5. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            categories = load_categories()
            category = pick_category(categories)
            doing = pick_doings(categories, category)
            value = how_much_value()

            log_activity(doing, value)

            again = input("Еще запись? (y/n): ").lower()
            if again not in ("y", "yes", "да"):
                break
        elif choice == "2":
            categories = load_categories()
            category = pick_category(categories)
            doing = pick_doings(categories, category)
            data = load_from_data()
            stats = statistics(doing, data)
            show_statistics(doing, stats)
        elif choice == "3":
            add_new_category(input("Название категории: "))
        elif choice == "4":
            categories = load_categories()
            category = pick_category(categories)
            add_new_subcategory(category ,input("Название подкатегории: "))
        elif choice == "5":
            quit()
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
