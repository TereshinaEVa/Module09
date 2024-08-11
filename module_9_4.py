#Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

#замыкание:
def get_advanced_writer(file_name):
    def write_averything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for elem in data_set:
                f.writelines(str(elem))
                f.write('\n')
        return open(file_name, 'r').readlines()
    return write_averything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
from random import choice
class MysticBall():
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Конечно', 'Зависит от тебя')
print(first_ball())
print(first_ball())
print(first_ball())