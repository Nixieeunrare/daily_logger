from src.logic import log_activity, statistics
from src.storage import load_categories, load_from_data
from src.ui import pick_category, pick_doings, how_much_value, show_statistics


def main():

    while True:
        print("Tracker by nixie -- pre-alpha(0.1.2)")
        print("\n1. Записать активность")
        print("2. Посмотреть статистику")
        print("3. Выход")

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
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
