from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): 
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
    def  fire(self):
        pass
 


win_width = 700 
win_height = 500 
 

window = display.set_mode((win_width, win_height))
display.set_caption('War')

background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player('rocket.png', 5, win_height  -80, 4) 

finish = False


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True: 
            window.blit(background, (0, 0)) 
            player.update() 
       
            player.reset() 
        

    window.blit(background, (0, 0))  
    display.update()  

quit()  