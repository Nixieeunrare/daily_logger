import json
import csv
import os

DOINGS_FILE_PATH = os.path.join("config", "doings.json")
DATA_FILE_PATH = os.path.join("data", "data.csv")


def init_project():
    os.makedirs("data", exist_ok=True)
    os.makedirs("config", exist_ok=True)

    if not os.path.exists(DATA_FILE_PATH):
        with open(DATA_FILE_PATH, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["doings", "date", "value"])

    if not os.path.exists(DOINGS_FILE_PATH):
        default_config = {
            "Здоровье": ["Отжимания"],
            "Учеба": ["Программирование(Python)", "3D Моделирование(Blender)"],
            "Хобби": ["Музыка(FLStudio)"],
            "Игры": ["PC"],
        }
        with open(DOINGS_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(default_config, f, ensure_ascii=False, indent=2)


def load_categories() -> dict:
    with open(DOINGS_FILE_PATH, "r", encoding="utf-8") as file:
        categories = json.load(file)
        return categories


def load_from_data():
    data = list()
    with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def save_to_data(data: list):
    with open(DATA_FILE_PATH, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        try:
            writer.writerows(data)
            print("Данные загружены!")
        except Exception as e:
            print(f"Ошибка! {e}")
