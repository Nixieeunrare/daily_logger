import os
import csv
import json
import time


os.makedirs("data", exist_ok=True)
os.makedirs("config", exist_ok=True)


if not os.path.exists("data/data.csv"):
    default_data = [["doings", "date", "value"], ["Заглушка", "2025-10-07", "0"]]
    with open("data/data.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(default_data)

if not os.path.exists("config/doings.json"):
    default_config = {
        "Здоровье": ["Отжимания"],
        "Учеба": ["Программирование(Python)", "3D Моделирование(Blender)"],
        "Хобби": ["Музыка(FLStudio)"],
        "Игры": ["PC"],
    }
    with open("config/doings.json", "w", encoding="utf-8") as file:
        json.dump(default_config, file, ensure_ascii=False, indent=2)


doings_file_path = os.path.join("config", "doings.json")
data_file_path = os.path.join("data", "data.csv")


current_time_seconds = time.time()
formatted_time_local = time.localtime(current_time_seconds)
main_time_formatter = time.strftime("%Y-%m-%d", formatted_time_local)


def load_categories() -> dict:
    with open(doings_file_path, "r", encoding="utf-8") as file:
        categories = json.load(file)
        return categories


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


def load_from_data():
    data = list()
    with open(data_file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def save_to_data(data: list):
    with open(data_file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        try:
            writer.writerows(data)
            print("Данные загружены!")
        except Exception as e:
            print(f"Ошибка! {e}")


def logging_today(doing, value):
    data = load_from_data()

    flag = False
    for i, dt in enumerate(data[1:], start=1):
        if dt[0] == doing and dt[1] == main_time_formatter:
            old_value = int(dt[2])
            new_value = old_value + value
            data[i][2] = str(new_value)
            flag = True
            break
    if not flag:
        data.append([doing, main_time_formatter, str(value)])

    save_to_data(data)
    print("Лог готов!")


def main():
    print("Tracker by nixie -- pre-alpha(0.1)")
    while True:
        categories = load_categories()

        category = pick_category(categories)
        doing = pick_doings(categories, category)
        value = how_much_value()

        logging_today(doing, value)

        again = input("Еще запись? (y/n): ").lower()
        if again not in ("y", "yes", "да"):
            break
    print("Пока!")


if __name__ == "__main__":
    main()
