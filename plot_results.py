import pandas as pd
import matplotlib.pyplot as plt

# Построение графиков для каждого задания
def plot_task(filename, title, xlabel):
    data = pd.read_csv(filename)
    plt.figure(figsize=(10, 6))
    plt.plot(data['n'], data['time'], 'bo-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Time, sec')
    plt.grid(True)
    plt.savefig(f'{filename[:-4]}.png')
    plt.show()

# Графики для всех заданий
plot_task('task_1_1.csv', 'Доступ к элементу по индексу', 'Number of elements')
plot_task('task_1_4.csv', 'Метод Горнера', 'Number of elements')
plot_task('task_1_5.csv', 'Поиск максимума', 'Number of elements')
plot_task('task_1_7.csv', 'Среднее арифметическое', 'Number of elements')
plot_task('task_2.csv', 'Матричное умножение', 'Matrix size (n x n)')