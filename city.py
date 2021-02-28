from pygame import *
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  #конструктор класса
  def __init__(self, player_image, player_x, player_y, player_speed, player_h, player_w):
      # Вызываем конструктор класса (Sprite):
      super().__init__()
 
      # каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (player_h, player_w))
      self.speed = player_speed
 
      # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   #метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
  def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
          self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < win_width - 80:
          self.rect.x += self.speed
      if keys[K_UP] and self.rect.y > 5:
          self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < win_height - 80:
          self.rect.y += self.speed
#класс спрайта-врага    
class Enemy(GameSprite):
  side = "left"
  def update_x(self,min_x,max_x):
      if self.rect.x <= min_x:
          self.side = "right"
      if self.rect.x >= max_x:
          self.side = "left"
      if self.side == "left":
          self.rect.x -= self.speed
      else:
          self.rect.x += self.speed

  def update_y(self,min_y,max_y):
      if self.rect.y <= min_y:
          self.side = "up"
      if self.rect.y >= max_y:
          self.side = "down"
      if self.side == "down":
          self.rect.y -= self.speed
      else:
          self.rect.y += self.speed

#класс элемента стены
class Wall(sprite.Sprite):
  def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
 
       # картинка стены - прямоугольник нужных размеров и цвета
       self.image = Surface([self.width, self.height])
       self.image.fill((color_1, color_2, color_3))
 
       # каждый спрайт должен хранить свойство rect - прямоугольник
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
 
  def draw_wall(self):
      draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))
#Создаем окошко
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт Карасуно")
#создаем стены
w1 = Wall(255, 215, 0, 0, 0, 1280, 10)
w2 = Wall(255, 215, 0, 410, 130, 10, 600)
w3 = Wall(255, 215, 0, 0, -50, 10, 400)
w4 = Wall(255, 215, 0, 100, 710, 1500, 10)
w5 = Wall(255, 215, 0, 90, 550, 10, 200)
w6 = Wall(255, 215, 0, 90, 550, 100, 10)
w7 = Wall(255, 215, 0, 90, 350, 10, 100)
w8 = Wall(255, 215, 0, 0, 350, 100, 10)
w9 = Wall(255, 215, 0, 90, 250, 10, 200)
w10 = Wall(255, 215, 0, 90, 250, 220, 10)
w11 = Wall(255, 215, 0, 190, 460, 10, 100)
w12 = Wall(255, 215, 0, 100, 350, 100, 10)
w13 = Wall(255, 215, 0, 190, 560, 10, 50)
w14 = Wall(255, 215, 0, 200, 350, 100, 10)
w15 = Wall(255, 215, 0, 300, 350, 10, 230)
w16 = Wall(255, 215, 0, 1270, 0, 10, 720)
w17 = Wall(255, 215, 0, 90, 130, 320, 10)
w18 = Wall(255, 215, 0, 530, 10, 10, 300)
w19 = Wall(255, 215, 0, 530, 450, 10, 400)
w20 = Wall(255, 215, 0, 530, 300, 110, 10)
w21 = Wall(255, 215, 0, 640, 300, 10, 280)
w22 = Wall(255, 215, 0, 750, 130, 10, 600)
w23 = Wall(255, 215, 0, 865, 0, 10, 580)
w24 = Wall(255, 215, 0, 980, 570, 180, 10)
w25 = Wall(255, 215, 0, 1160, 570, 10, 200)
w26 = Wall(255, 215, 0, 980, 120, 10, 460)

monsters = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26]

#создаем спрайты
bokuto = Player('bokuto.png', 5, 600, 20, 50, 70)
keishin = Enemy('keishin.png', 1190, 470, 15, 55, 100)
kageyama = Enemy('kageyama.png', 110, 610, 5, 50, 105)
nishinoya = Enemy('nishinoya.png', 300, 257, 15, 50, 95)
sugawara = Enemy('sugawara.png', 1080, 610, 5, 40, 100)
asahi = Enemy('asahi.png', 560, 190, 20, 50, 110)
daichi = Enemy('daichi.png', 440, 610, 15, 60, 100)
tsukishima = Enemy('tsukishima.png', 1000, 460, 25, 45, 110)

walls = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26]

sprites = [bokuto,keishin,kageyama,nishinoya,sugawara,asahi,daichi,tsukishima]

monsters = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,
            w13,w14,w15,w16,w17,w18,w19,
            w20,w21,w22,w23,w24,w25,w26,keishin,
            kageyama,nishinoya,sugawara,asahi,
            daichi,tsukishima]



final_sprite = GameSprite('kuroo.png', 1185, 590, 0, 60, 120)
 
#переменная, отвечающая за то, как кончилась игра
finish = False
#игровой цикл
run = True
while run:
  #цикл срабатывает каждую 0.05 секунд
  time.delay(50)
   #перебираем все события, которые могли произойти
  for e in event.get():
      #событие нажатия на кнопку “закрыть”
      if e.type == QUIT:
          run = False
 
#проверка, что игра еще не завершена
  if not finish:
      #обновляем фон каждую итерацию
      window.fill((169, 169, 169))
       #рисуем стены

      for wal in walls:
          wal.draw_wall()
 
       #запускаем движения спрайтов
      bokuto.update()
      keishin.update_x(1000,1195)
      kageyama.update_x(110,345)
      nishinoya.update_x(110,345)
      sugawara.update_x(775,1090)
      asahi.update_y(10,190)
      daichi.update_y(10,610)
      tsukishima.update_y(20,460)
    
       #обновляем их в новом местоположении при каждой итерации цикла
      final_sprite.reset()
      for spr in sprites:
          spr.reset()
 
      #Проверка столкновения героя с врагом и стенами
      for mons in monsters:
          if sprite.collide_rect(bokuto,mons):

            finish = True
            #вычисляем отношение
            img = image.load('sad.jpg')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (280, 0))
 
      if sprite.collide_rect(bokuto, final_sprite):
          finish = True
          img = image.load('Friend.png')
          window.fill((255, 255, 255))
          window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
 
  display.update()
