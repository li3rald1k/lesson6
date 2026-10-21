tasks = []

tasks_list = [
    {'id': 1, 'title': 'Учеба', 'description': 'Сделать задание', 'status': 'новая'},
    {'id': 2, 'title': 'Уборка', 'description': 'Убраться дома', 'status': 'в процессе'},
    {'id': 3, 'title': 'Покупки', 'description': 'Купить продукты', 'status': 'выполнена'}
]


def all_tasks(lst):
    for i in lst:
        for k, v in i.items():
            print(f'{k}-{v}')


all_tasks(lst=tasks_list)


def selection(lst, tasks):
    for i in lst:
        tasks.append(i)


selection(tasks_list, tasks)

print(f'Созданные задачи - {tasks}')
print('-'*20)
print(f'Список задач - {tasks_list}')
print('-'*20)
