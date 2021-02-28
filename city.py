from time import sleep
 
class Hero():
   #конструктор класса
   def __init__(self, name, health, armor):
       self.name = name
       self.health = health #число
       self.armor = armor #строка
   #печать параметров персонажа:
   def print_info(self):
       print('Уровень здоровья:', self.health)
       print('Класс брони:', self.armor, '\n')
 
 
class Warrior(Hero):
   def hello(self):
       print('-> НОВЫЙ ГЕРОЙ. Верхом на коне появился бравый воин по имени', self.name)
       self.print_info()
       sleep(4)
 
   def attack(self, enemy):
       print('-> УДАР! Храбрый воин', self.name, 'атакует', enemy.name, 'мечом!')
       enemy.armor -= 15 #сила удара для класса Воин
       if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0
       print('Страшный удар обрушился на противника. \nТеперь его броня: ' +
           str(enemy.armor) + ', а уровень здоровья: ' + str(enemy.health) + '\n')
       sleep(5)
 
class Magician(Hero):
   def hello(self):
       print('-> НОВЫЙ ГЕРОЙ. Откуда ни возьмись появился искусный волшебник', self.name)
       self.print_info()
       sleep(4)
 
   def attack(self, enemy):
       print('-> УДАР! Ловкий маг', self.name, 'накладывает заклинание на', enemy.name)
       enemy.armor -= 35 #сила удара для класса Маг
       if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0
       print('Сложное заклинание оглушило противника. \nТеперь его броня: ' +
           str(enemy.armor) + ', а уровень здоровья: ' + str(enemy.health) + '\n')
       sleep(5)
 
 
Warrior1 = Warrior('Henry', 100, 50)
Warrior1.hello()
 
Magician1 = Magician('Luke', 50, 20)
Magician1.hello()
 
Warrior1.attack(Magician1)
Magician1.attack(Warrior1)

 
