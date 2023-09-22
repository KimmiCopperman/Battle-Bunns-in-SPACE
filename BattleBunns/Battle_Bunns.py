import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Making the gmae 
bottom_panel = 150 
screen_width = 900
screen_height = 450 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle Bunns....IN SPACE!!!!!')

#fonts and colors
font = pygame.font.SysFont('Cyber Graph', 26)

#Background display and other graphic information
background_image = pygame.image.load('/Users/kimmi/Desktop/BattleBunns/Graphics/Background/space.png').convert_alpha()
panel_image = pygame.image.load('/Users/kimmi/Desktop/BattleBunns/Graphics/Background/panel.png').convert_alpha()

#Functions for displaying text and colors
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
blue = (0, 0, 255)
white = (255, 255, 255)
purple = (146, 85, 176)

#Functions for displaying graphics
def draw_bg():
    screen.blit(background_image, (0, 0))

def draw_panel():
    # panel retangle
    screen.blit(panel_image, (0, screen_height - bottom_panel))
    # player stats
    draw_text(f'{knight.name} HP: {knight.hp}', font, blue, 100, screen_height - bottom_panel +10 )
    for count, i in enumerate(bandit_list):
        #Show name and health
        draw_text(f'{i.name} HP: {i.hp}', font, blue, 550, (screen_height - bottom_panel +10) + count * 60 )
    
#player character
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
     self.name = name
     self.max_hp = max_hp
     self.hp = max_hp
     self.strength = strength
     self.start_potions = potions
     self.potions = potions
     self.alive = True
     self.animation_list = []
     self.frame_index = 0
     self.action = 0 #0=idle, 1=attack, 2=hurt, 3=dead
     self.update_time = pygame.time.get_ticks()
     #idle images
     temp_list = []
     for i in range(6):
         img = pygame.image.load(f'Graphics/{self.name}/Idle/{i}.png')
         new_width, new_height = 163, 320  
         resized_image = pygame.transform.scale(img, (new_width, new_height))
         temp_list.append(resized_image)
     self.animation_list.append(temp_list)
     #attack images
     temp_list = []
     for i in range(6):
         img = pygame.image.load(f'Graphics/{self.name}/Idle/{i}.png')
         new_width, new_height = 150, 200  
         resized_image = pygame.transform.scale(img, (new_width, new_height))
         temp_list.append(resized_image)
     self.animation_list.append(temp_list)
     #hurt images
     temp_list = []
     for i in range(6):
         img = pygame.image.load(f'Graphics/{self.name}/Idle/{i}.png')
         new_width, new_height = 150, 200  
         resized_image = pygame.transform.scale(img, (new_width, new_height))
         temp_list.append(resized_image)
     self.animation_list.append(temp_list)
     #death images
     temp_list = []
     for i in range(6):
         img = pygame.image.load(f'Graphics/{self.name}/Idle/{i}.png')
         new_width, new_height = 163, 320  
         resized_image = pygame.transform.scale(img, (new_width, new_height))
         temp_list.append(resized_image)
     self.animation_list.append(temp_list)
     self.image = self.animation_list[self.action][self.frame_index]
     self.rect = self.image.get_rect()
     self.rect.center = (x, y)

    
    
    def update(self):
        animation_cooldown = 100
        # update image animation
        self.image = self.animation_list[self.action][self.frame_index]
        
        #make sure enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        
        # loop animation
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0    

    def draw(self):
        screen.blit(self.image, self.rect)

class HeathBar():
    def __init__(self, x, y, hp, max_hp,):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
    
    def draw(self,hp):
        #update to show starting hp
        self.hp = hp
        # calculate damage
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, white, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, purple, (self.x, self.y, 150 * ratio, 20))
    
knight = Fighter(200, 260, 'Cosmic', 30, 10, 3)
bandit1 = Fighter(550, 270, 'Wraith', 20, 6, 1)
bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)
#bandit3 = Fighter(550, 270, 'Bandit', 20, 6, 1)
#bandit4 = Fighter(700, 270, 'Wraith', 20, 6, 1)
#bandit5 = Fighter(550, 270, 'Scavenger', 20, 6, 1)
#bandit6 = Fighter(700, 270, 'Turnip', 20, 6, 1)
#bandit7 = Fighter(550, 270, 'Wraith', 20, 6, 1)
#bandit8 = Fighter(700, 270, 'Bandit', 20, 6, 1)

bandit_list = []

bandit_list.append(bandit1)
bandit_list.append(bandit2)
#bandit_list.append(bandit3)
#bandit_list.append(bandit4)
#bandit_list.append(bandit6)
#bandit_list.append(bandit6)
#bandit_list.append(bandit7)
#bandit_list.append(bandit8)

knight_health_bar = HeathBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HeathBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HeathBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)
#bandit3_health_bar = HeathBar(550, screen_height - bottom_panel + 40, bandit3.hp, bandit3.max_hp)
#bandit4_health_bar = HeathBar(550, screen_height - bottom_panel + 100, bandit4.hp, bandit4.max_hp)
#bandit5_health_bar = HeathBar(550, screen_height - bottom_panel + 40, bandit5.hp, bandit5.max_hp)
#bandit6_health_bar = HeathBar(550, screen_height - bottom_panel + 100, bandit6.hp, bandit6.max_hp)
#bandit7_health_bar = HeathBar(550, screen_height - bottom_panel + 40, bandit7.hp, bandit7.max_hp)
#bandit8_health_bar = HeathBar(550, screen_height - bottom_panel + 100, bandit8.hp, bandit8.max_hp)

#Conditions to keep the screen open
run = True
while run:
    clock.tick(fps)
    #display backgroung
    draw_bg()
    draw_panel()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)

    # Display for fighters
    knight.update()
    knight.draw()
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
  
pygame.quit()
