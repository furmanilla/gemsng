from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

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



win_width = 700 
win_height = 500 
 

window = display.set_mode((win_width, win_height))
display.set_caption('War')


background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


player = Player('rocket.png', 5, win_height - 80, 4) 


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

game = True
finish = False
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))  
        player.update()  
        player.reset()  
    display.update()  
    clock.tick(60)  

quit()
