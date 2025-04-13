from pygame import *
from random import randint

class GameSprite(sprite.Sprite): #Основной класс спрайта
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.x < 480:
            self.rect.x += self.speed
        
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 480:
            self.rect.x += self.speed
# window     
window = display.set_mode((500, 700))
display.set_caption('ping_pong')
background = transform.scale(image.load('table.png'), (500, 700))

lost = 0 # Счётчик пропущенных мячей
score = 0

game = True
finish = False
#Таймер
clock = time.Clock()
FPS = 60

player = Player('rocket.jpg', 15, 218, 15)
player2 = Player('rocket.jpg', 620, 217, 15)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0,0))
        player.update()
        player.reset()
        player2.update()
        player2.reset()
        
    display.update()
    clock.tick(FPS)