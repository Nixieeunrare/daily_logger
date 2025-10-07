import time
from src.storage import load_from_data, save_to_data


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
