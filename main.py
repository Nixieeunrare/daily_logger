from src.logic import log_activity
from src.storage import load_categories
from src.ui import pick_category, pick_doings, how_much_value


def main():
    print("Tracker by nixie -- pre-alpha(0.1)")
    print()
    while True:
        categories = load_categories()
        category = pick_category(categories)
        doing = pick_doings(categories, category)
        value = how_much_value()

        log_activity(doing, value)

        again = input("Еще запись? (y/n): ").lower()
        if again not in ("y", "yes", "да"):
            break
    print("Пока!")


if __name__ == "__main__":
    main()
