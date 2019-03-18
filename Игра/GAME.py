
# coding: utf-8

# In[237]:


import os
import sys
import pygame
from pygame import *
from math import tan, radians, degrees, copysign
from pygame.math import Vector2
from random import randint

#тушение происходит при соприкосновении автомобиля со зданием

#первые 5 переменных можно менять, игра адаптируется
width = 8
height = 5 #ALARM!!!!!!!! Если слишком большой размер, лагает не по-детски (слишком много объектов на карте)
                #Update!!!!!!!!!!!!!!!!!!!! больше лагать НЕ будет
fire_to_win = 10 #сколько надо потушить для победы
lives = 3 #количество жизней
timeout = 10000 #через сколько секунд загорится рандомное здание
                            #(возгарание просиходит не всегда через
                            #заданное время, оно происходит также на рандоме)
                            #и усилится возгарание остальных

road_width = 0
road_height = 1
crossroad = 2
building = [3, 4, 5, 6, 7, 8]

#map_generator
tilemap=[[building[0] for j in range(width)] for i in range(height)]
count_width = 1
count_height = 1
for n in range(height): #пройти по высоте
    for i in range(width): #пройти по длине
        if n != count_height: 
            if i == count_width: #если высота не равна заданной и длина равна заданной
                tilemap[n][i]=road_height #вывести дорогу
                count_width += 3 #длина+3
        else:
            if i != count_width: #если высота равна заданной и длина не равна заданной
                tilemap[n][i]=road_width #вывести дорогу
            else:
                tilemap[n][i]=crossroad
                count_width += 3
            if i == width-1:
                count_height += 3 #ОТДЕБАЖЕНО. НЕ ТРОГАТЬ!
    count_width = 1
#end map_generator

window = pygame.display.set_mode((width*90+90, height*90))
screen =pygame.Surface((width*90+90, height*90))

roads = pygame.sprite.Group()
entitles = pygame.sprite.Group() 
buildings = []
fire_buildings = []
walls = []
fired = []

class Road_Width(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((90,90))
        self.image = image.load('0.png')
        self.rect = Rect(x, y, 90, 90)
        
class Road_Heigh(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((90,90))
        self.image = image.load('1.png')
        self.rect = Rect(x, y, 90, 90)        

class Road_Crossroad(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((90,90))
        self.image = image.load('2.png')
        self.rect = Rect(x, y, 90, 90)

class Wall(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('back.png')
        self.rect = self.image.get_rect(center=(x+45, y+45)) 
        self.mask = pygame.mask.from_surface(self.image, 50)
        
class Building(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.a = 3
        self.image = image.load(str(self.a)+'.png')
        self.rect = self.image.get_rect(center=(x+45, y+45)) 
        self.mask = pygame.mask.from_surface(self.image, 50)
    def update_plus(self):
        if self.a <= 7:
            self.a +=1
            self.image = image.load(str(self.a)+'.png')
    def update_minus(self):
        if self.a > 3:
            self.a -=1
            self.image = image.load(str(self.a)+'.png')
     
class Car:
    def __init__(self, x, y, car_image, angle=0.0):
        #initialize
        self.orig_image = car_image
        self.image = car_image
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.acceleration = 0.0
        self.steering = 0.0
        self.mask = pygame.mask.from_surface(self.image, 50)

    def update(self, dt):
        #update car variables
        self.velocity = Vector2(self.acceleration, 0)
        angular_velocity = self.steering * dt * self.velocity.x
        self.position += self.velocity.rotate(-self.angle) * dt
        self.rect.center = self.position  # Update the rect each frame.
        self.angle += degrees(angular_velocity) * dt
        # Rotate the orig image, rect and mask.
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image, 50)
                   
for n in range(width):
    for i in range(height):
        if tilemap[i][n]==0:
            roads.add(Road_Width(n*90, i*90))
        elif tilemap[i][n]==1:
            roads.add(Road_Heigh(n*90, i*90))
        elif tilemap[i][n]==2:
            roads.add(Road_Crossroad(n*90, i*90))
        elif ((tilemap[i][n]>=3)&(tilemap[i][n]<=8)):
            pf = Building(n*90, i*90)
            entitles.add(pf)
            buildings.append(pf)

for i in range(width):
    pf = Wall(i*90, height*90)
    walls.append(pf)
    entitles.add(pf)
for i in range(height):
    pf = Wall(width*90, i*90)
    walls.append(pf)
    entitles.add(pf)
                 
def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def message_display(text, size, wid, hei):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((wid),(hei))
    window.blit(TextSurf, TextRect)
    
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hello")
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False
        self.timetext = 10000
        self.DOIT = 1

    def run(self, fire_to_win, lives):
        deadline = 0
        image_path = os.path.join("car.png")
        car_image = pygame.image.load(image_path).convert_alpha()
        car = Car(40, 120, car_image)

        while not self.exit:
            dt = self.clock.get_time() / 1000
            timer = pygame.time.get_ticks
            
            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
 
            # User input
            if (lives <=0) or (len(buildings)==len(fired)):
                now = timer()
                if self.DOIT == 1:
                    self.timetext += now
                    self.DOIT +=1
                window.fill((0, 0, 0))
                message_display("ВЫ ПРОИГРАЛИ!", 20 , (width*90)/2, (height*90)/2)
                if now > self.timetext:
                    break
            elif fire_to_win <=0:
                now = timer()
                if self.DOIT == 1:
                    self.timetext += now
                    self.DOIT +=1
                window.fill((0, 0, 0))
                message_display("ВЫ ПОБЕДИЛИ!", 20 , (width*90)/2, (height*90)/2)
                now = timer()
                if now > self.timetext:
                    break
            else:
                window.fill((0, 255, 0))
                roads.draw(window)
                entitles.draw(window)
                pressed = pygame.key.get_pressed()

                #Acceleration logic
                if pressed[pygame.K_UP]:
                    car.acceleration += 40 * dt
                elif pressed[pygame.K_DOWN]:
                    car.acceleration -= 40 * dt
                else:
                    car.acceleration *= 0.99

                #Steering logic
                if pressed[pygame.K_RIGHT]:
                    car.steering -= 15 * dt
                elif pressed[pygame.K_LEFT]:
                    car.steering += 15 * dt
                else:
                    car.steering = 0

                #Update the car
                car.update(dt)
                
                #Calculate offset
                for i in range(len(buildings)):
                    offset_x = car.rect[0] - buildings[i].rect[0]
                    offset_y = car.rect[1] - buildings[i].rect[1]

                #Check for overlap
                    overlap = buildings[i].mask.overlap(car.mask, (offset_x, offset_y)) #МИНУС 40 ЧАСОВ ЖИЗНИ!!!!!!! Зачем я вообще согласился это делать
                    if ((overlap)or(car.rect[0]<0)or(car.rect[1]<0)):
                        car.acceleration = 0
                        if buildings[i] in fire_buildings:
                            if buildings[i].a <= 7:
                                buildings[i].update_minus()
                                if buildings[i].a <= 3:
                                    fire_to_win -=1
                                    fire_buildings.remove(buildings[i])
                for i in range(len(walls)):
                    of_x = car.rect[0] - walls[i].rect[0]
                    of_y = car.rect[1] - walls[i].rect[1]
                    ov = walls[i].mask.overlap(car.mask, (of_x, of_y))
                    if ov:
                        car.acceleration = 0
                now = timer()
                if now > deadline:
                    deadline = now + timeout
                    for i in fire_buildings:
                        i.update_plus()
                        if i.a == 8:
                            lives -= 1
                            fire_buildings.remove(i)
                            fired.append(i)
                            i.a = 9
                    index = randint(0, len(buildings)-1)
                    if buildings[index] not in fire_buildings:
                        fire_buildings.append(buildings[index])
                        buildings[index].update_plus()
                window.blit(car.image, car.rect)
#                 for point in car.mask.outline(8): # маска автомобиля, можно сделать аналогично со зданием
#                     pygame.draw.rect(window, (255, 0, 0), (point+Vector2(car.rect.topleft), (2, 2))) 
            message_display("ЖИЗНИ", 13, width*90+45, height+10)
            message_display(str(lives), 13, width*90+45, height+30)
            message_display("ДО ПОБЕДЫ", 13, width*90+45, height+50)
            message_display(str(fire_to_win), 13, width*90+45, height+70)
            pygame.display.update()
            self.clock.tick(self.ticks)
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run(fire_to_win, lives)

