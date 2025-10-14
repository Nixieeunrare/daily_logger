import matplotlib.pyplot as plt

def visualization_subcategory_bar(data: list, category: str):
    data.pop(0)
    dates = [i[1] for i in data if i[0] == category]
    values = [int(i[2]) for i in data if i[0] == category]
    if dates == []:
        print("Нет данных по этому занятию.")
        return
    else:
        fig, ax = plt.subplots()
        bars = ax.bar(dates, values, 0.3)
        ax.bar_label(bars, padding=0.1)
        ax.set_title(f"Визуализация для {category}")
        plt.gca().get_yaxis().set_visible(False)
        plt.show()
