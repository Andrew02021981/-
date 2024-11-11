def game():
    import random
    import time
    print('Приветствую Вас, мой Друг!')
    time.sleep(1)
    n = int(input('Выберите уровень сложности от 1 до 3: '))
    if n == 1:
        a = int(input('Я загадал число от 1 до 100. Угадайте его!  '))
        b = random.randint(1, 100)
    elif n == 2:
        a = int(input('Я загадал число от 100 до 1000. Угадайте его!  '))
        b = random.randint(100, 1000)
    elif n == 3:
        a = int(input('Я загадал число от 1000 до 1000000. Угадайте его!  '))
        b = random.randint(1000, 1000000)
#print(b)
    counter = 1
    if b == a:
        print('Супер! Да Вы просто Вольф Мессинг!')
    elif a > b:
        print('Ваше число больше!')
    elif a < b:
        print('Ваше число меньше!')
    while a != b:
        a = int(input('Попробуйте еще раз! '))
        counter = counter + 1
        if a > b:
            print('Ваше число больше!')
        elif a < b:
            print('Ваше число меньше!')
    if counter % 10 in (0,5,6,7,8,9):
        print('Отлично, Вы угадали число за', counter, 'ходов!')
    elif counter % 10 in (2,3,4):
        print('Отлично, Вы угадали число за', counter, 'хода!')
        return counter
#с = counter


#def rank():
    #dict_1 = {name: counter}
    #result = dict_1.update({name: counter})
       # return result
#print(dict_1)

#from module_1 import record
#record()