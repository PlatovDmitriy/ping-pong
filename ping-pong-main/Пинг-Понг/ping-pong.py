from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 105:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 105:
            self.rect.y += self.speed
font.init()
font1 = font.SysFont('Arial',40)
win_1 = font1.render('Player1 WIN',True,(0,200,200))
win_2 = font1.render('Player2 WIN',True,(200,200,0))
win_width = 650
win_height = 500
run = True
player = Player('player.png', 10,200,10,100,15)
player2 = Player('player.png', 630,200,10,100,15)
finish = False
background = transform.scale(image.load('bg.jpg'), (win_width, win_height))
window = display.set_mode((win_width, win_height))
corxy = [10,-10]
ran = randint(1,2)
speedx = corxy[ran-1]
rad = randint(1,2)
speedy = corxy[rad-1]
push = 0
i = 0
ball = GameSprite('tennis.png',250,200,50,50,0)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
        player.reset()
        player.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()
        ball.rect.x += speedx
        ball.rect.y += speedy
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speedy *= -1
        if sprite.collide_rect(ball,player) or sprite.collide_rect(ball,player2):
            speedx *= -1
            push += 1
            i += 1
        if sprite.collide_rect(ball,player) or sprite.collide_rect(ball,player2) and push == i:
            if speedx > 0:
                speedx += 1
            elif speedx < 0:
                speedx -= 1
        if ball.rect.x < -20:
            window.blit(win_2,(250,200))
            finish = True
        if ball.rect.x > 630:
            window.blit(win_1,(250,200))
            finish = True
    display.update()
    time.delay(50)
