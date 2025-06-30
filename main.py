import pygame
import random
import os
import time
pygame.mixer.init() 
pygame.init()
window_width =  600
window_height = 400
game_window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")
screen_bg = (192,192,192)
black_color = (0,0,0)
snake_color = 0
white = (255,255,255)
clock = pygame.time.Clock()
font = pygame.font.Font("edu-font.ttf",25)
def score_screen( text , font_color , x  , y):
    game_score = font.render(text ,True, font_color)
    game_window.blit(game_score,[x,y])

def snake_plot(game_window , black_color ,snk_list, radius):
    for x,y in snk_list:
        snake = pygame.draw.circle(game_window , black_color ,[x ,y], radius)
def welcome():
    pygame.mixer.music.load("Snake-voice.wav")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        bg_img = pygame.image.load("hero.png")
        bg_img = pygame.transform.scale(bg_img,(window_width,window_height)).convert_alpha()
        game_window.fill((233,210,229))
        game_window.blit(bg_img ,(0,0))
        score_screen("Welcome to Snakes", black_color, 230, 160)
        score_screen("Press Space Bar To Play", black_color, 210, 210)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    lop = True
    game_over = False
    fps = 50
    score = 0
    velocity_x = 0
    velocity_y = 0 
    food_x = random.randint(10,window_width-10)
    food_y = random.randint(10,window_height-20)
    snake_x = 45
    snake_y = 80
    radius = 6
    snk_list = []
    snk_length = 1
    if not os.path.exists("high-score.txt"):
        with open("high-score.txt","w") as txt_file:
           txt_file.write("0")
   
    with open("high-score.txt","r") as score_file:
           high_score = score_file.read()
    while lop :
        
        if game_over == True:
                
                game_over_bg = pygame.image.load("totenkopf-tod-schadel-flache-vektor-icon-einfach-schwarzes-symbol-auf-weissem-hintergrund-w36p18.jpg")

                game_over_bg = pygame.transform.scale(game_over_bg,(200,200))
                if score > int(high_score):
                    high_score = score
                    with open("high-score.txt","w") as score_file:
                        score_file.write(str(score))
                game_window.fill(white)
                game_window.blit(game_over_bg,(200,40))
                score_screen("Game Over" , black_color , 235 , 190)
                score_screen("For Countinue Press Enter" , black_color , 160 , 232)
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            lop = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                gameloop()
                
                        
                    
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 3
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - 3
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 3
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = + 3
                        velocity_x = 0
                
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            game_bg = pygame.image.load("game-bg.png")
            game_bg = pygame.transform.scale(game_bg,(window_width,window_height)).convert_alpha()
            game_window.blit(game_bg,(0,0))
            score_screen(f"Score : {score}     High-score : {high_score}",black_color, 5,5)
            
            if (abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6):
                pygame.mixer.music.load("eating.wav")
                pygame.mixer.music.play()
                score = score + 6
                food_x = random.randint(10,window_width-10)
                food_y = random.randint(10,window_height-10)
                snk_length = snk_length + 5

            food = pygame.draw.circle(game_window , black_color ,(food_x ,food_y), radius)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load("game-over-sound-effect-online-audio-convertercom_vepQw8V7.wav")
                pygame.mixer.music.play()
                game_over = True

            if snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_height:
                pygame.mixer.music.load("game-over-sound-effect-online-audio-convertercom_vepQw8V7.wav")
                pygame.mixer.music.play()
                game_over = True
            snake_plot(game_window , black_color ,snk_list, radius)
            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
time.sleep(3)
welcome()