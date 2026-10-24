import csv


def read_file(csv_file: str) -> tuple[dict[str, set], dict[str, list]]:
    """Читает файл и формирует словари департаментов и зарплат"""
    hierarchy = {}
    info = {}

    with open(csv_file, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)

        for row in reader:
            if row[1] not in hierarchy:
                hierarchy[row[1]] = set()
                info[row[1]] = []

            hierarchy[row[1]].add(row[2])
            info[row[1]].append(int(row[5]))

    return hierarchy, info


def show_hierarchy(hierarchy: dict) -> None:
    """Выводит департаменты и входящие в них команды"""
    for department, teams in hierarchy.items():
        teams_str = ', '.join(teams)
        print(f'{department}: {teams_str}')


def calculate_metrics(info: dict) -> dict:
    """Рассчитывает статистику по зарплатам для каждого департамента"""
    info_metrics = {}

    for department, salaries in info.items():
        info_metrics[department] = [len(salaries), min(salaries), max(salaries),
                                    sum(salaries) / len(salaries)]
    return info_metrics


def show_statistik(info_metrics: dict) -> None:
    """Выводит отчёт по департаментам"""
    for department, metrics in info_metrics.items():
        print(department)
        print(f'Кол-во сотрудников: {metrics[0]}')
        print(f'Минимальная заработная плата = {metrics[1]}')
        print(f'Максимальная заработная плата = {metrics[2]}')
        print(f'Средняя заработная плата = {metrics[3]}')
        print('____________________________________________')


def save_statistik(info_metrics: dict, filename: str) -> None:
    """Выводит и сохраняет отчёт в csv-файл"""
    with open(filename, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Департамент', 'Кол-во сотрудников', 'Min зарплата',
                         'Max зарплата', 'Average зарплата'])

        for department, metrics in info_metrics.items():
            writer.writerow([department] + metrics)


def main() -> None:
    """Выводит меню и запрашивает нужный отчёт"""
    print('1. Вывести иерархию команд')
    print('2. Вывести сводный отчёт по департаментам')
    print('3. Сохранить сводный отчёт в CSV')

    try:
        num = int(input('Выберите пункт меню: '))
    except ValueError:
        print('Введите число от 1 до 3')
        return

    if num not in (1, 2, 3):
        print('Введите число от 1 до 3')
        return

    hierarchy, info = read_file('Corp_Summary.csv')

    if num == 1:
        show_hierarchy(hierarchy)

    elif num == 2:
        info_metrics = calculate_metrics(info)
        show_statistik(info_metrics)

    elif num == 3:
        info_metrics = calculate_metrics(info)
        save_statistik(info_metrics, 'information.csv')


if __name__ == '__main__':
    main()
