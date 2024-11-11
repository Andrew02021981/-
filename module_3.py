from module_1 import game
#from module_1 import counter

m = int(input('Введите количество игр от 1 до 5:'))
dict_1 = {}
#from module_1 import game,result
for i in range (1,m+1):
    print('Введите имя',i,'игрока:')
    name = input()
    game()
    #dict_1.update({name: counter})
#print(dict_1)

