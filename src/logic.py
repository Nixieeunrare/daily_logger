import time
import json
import os
from src.storage import load_from_data, save_to_data

DOINGS_FILE_PATH = os.path.join("config", "doings.json")


def log_activity(doing, value):
    current_time_seconds = time.time()
    formatted_time_local = time.localtime(current_time_seconds)
    main_time_formatter = time.strftime("%Y-%m-%d", formatted_time_local)

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


def statistics(doing: str, data: list) -> dict:
    current_time_seconds = time.time()
    formatted_time_local = time.localtime(current_time_seconds)
    main_time_formatter = time.strftime("%Y-%m-%d", formatted_time_local)
    stats = list()
    today_value = None

    for row in data[1:]:
        if row[0] == doing:
            stats.append(row)
            if row[1] == main_time_formatter:
                today_value = int(row[2])

    if not stats:
        return {"err": "no data"}

    values = [int(i[2]) for i in stats]
    dates = [j[1] for j in stats]

    return {
        "total_days": len(stats),
        "total_value": sum(values),
        "average": round(sum(values) / len(values), 1),
        "last_date": dates[-1],
        "last_value": values[-1],
        "today_value": today_value,
    }

def add_new_category(category: str):
    with open(DOINGS_FILE_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data[category] = []
        with open(DOINGS_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

def add_new_subcategory(category: str, subcategory: str):
    with open(DOINGS_FILE_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data[category].append(subcategory)
        with open(DOINGS_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
