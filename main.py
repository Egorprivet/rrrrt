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
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 625: 
            self.rect.y += self.speed

# Players 2
class Player2(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 625: 
            self.rect.y += self.speed

# ball
class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y > 650 or self.rect.y < 0:
            speed_y *= -1
        if self.rect.x < 0:
            window.blit(lose1, (200, 200))
            game_over()
        if self.rect.x > 500:
            window.blit(lose2, (200, 200))
            game_over()

def game_over():
    global game
    game = False

# Window
window = display.set_mode((500, 700))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('table.png'), (500, 700))


font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))

# Таймер
clock = time.Clock()
FPS = 60


speed_x = 3
speed_y = 3

# Создание  объектов
player = Player('rocket.jpg', 15, 218, 15)
player2 = Player2('rocket.jpg', 420, 217, 15)
ball = Ball('ball.png', 250, 350, 0, 50, 50)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
        if sprite.collide_rect(ball, player) or sprite.collide_rect(ball, player2):
            speed_x *= -1



        display.update()
        clock.tick(FPS)


