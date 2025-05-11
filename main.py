from pygame import *
from random import randint

#класс спрайта
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Player
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 15:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 485:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 15:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 485:
            self.rect.y += self.speed

a = randint(1, 2)

# ball
class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y, score1, score2
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y >= 480 or self.rect.y <= 20:
            speed_y *= -1
        if self.rect.x <= 0:
            score2 += 1
            self.rect.y = 218
            self.rect.x = 318  
        if self.rect.x >= 700:
            score1 +=1
            self.rect.y = 218
            self.rect.x = 318 

score1 = 0
score2 = 0
    
def game_over():
    if score1 >= 10 and score1 - score2 >= 1:
        window.blit(lose1, (260, 250))
        window.blit(win2, (260, 190))
    if score2 >= 10 and score2 - score1 >= 1:
        window.blit(lose2, (260, 250))
        window.blit(win1, (260, 190))

    

# Window
window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('images.jpg'), (700, 500))

font.init()
font1 = font.Font(None, 48)
win1 = font1.render('Player 1 win!', True, (255, 255, 255))
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))

font2 = font.Font(None, 48)
win2 = font2.render('Player 2 win!', True, (255, 255, 255))
lose2 = font2.render('Player 2 lose!', True, (180, 0, 0))

mixer.init()
mixer.music.load('mm.ogg')
mixer.music.play()

# Таймер
clock = time.Clock()
FPS = 60

lost1 = 0
lost2 = 0

speed_x = 5
speed_y = 5


cooldown = 0

# Создание  объектов
player = Player('pl1.png', 15, 218, 15)
player2 = Player2('pl2.png', 620, 217, 15)
ball = Ball('ball.png', 250, 350, 40, 50, 50)

game = True
finish = False
clock = time.Clock()
FPS = 60



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0,0)) 
        score_1 = font1.render('Player 1 score:'+str(score1), 1, (255, 255, 255))
        score_2 = font1.render('Player 2 score:'+str(score2), 1, (255, 255, 255))
        window.blit(score_1, (27, 27))
        window.blit(score_2,(403, 27))
        player.update()
        player.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
        game_over()
        if sprite.collide_rect(ball, player) and cooldown > 9:
            speed_x *= -1
            cooldown = 0
        if sprite.collide_rect(ball, player2) and cooldown > 9:
            speed_x *= -1
            cooldown = 0
    cooldown += 1
        
    display.update()
    clock.tick(60)




