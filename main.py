from src.storage import init_project
from src.ui import (
    show_menu,
    add_log_flow,
    add_category_flow,
    add_subcategory_flow,
    show_plot_flow,
    show_statistics_flow,
    Menu,
)


def main():
    init_project()

    while True:
        show_menu()

        choice = input("\nВыберите действие: ")

        if choice == Menu.ADD_NEW_DOING_LOG:
            add_log_flow()
        elif choice == Menu.ADD_NEW_CATEGORY:
            add_category_flow()
        elif choice == Menu.ADD_NEW_SUBCATEGORY:
            add_subcategory_flow()
        elif choice == Menu.SHOW_STATISTIC:
            show_statistics_flow()
        elif choice == Menu.PLOT_VISUALIZATION:
            show_plot_flow()
        elif choice == Menu.QUIT:
            quit()
        else:
            print("Такого действия не существует!")


if __name__ == "__main__":
    main()
