import pygame
import random
import os

pygame.mixer.init()
pygame.init()

width=1000
height=500
gameWindow=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
bgimg = pygame.image.load("back.png")
bgimg = pygame.transform.scale(bgimg, (width,height)).convert_alpha()

welimg = pygame.image.load("welcome.png")
welimg = pygame.transform.scale(welimg, (width,height)).convert_alpha()

#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#Game specific variables
Score=0
exit_game=False
game_over=False
snake_x=20
snake_y=40
snake_size=15
fps=50
vel_x=0
vel_y=0
increment=5
food_x=random.randint(50,width-20)
food_y=random.randint(150,height-20)
snk_list = []
snk_length = 1

try:
    file = open("highscore.txt", "x") 
    file.write("0")
    file.close()
except:
    print("")

def Game_vars():
    Score=0
    exit_game=False
    game_over=False
    snake_x=20
    snake_y=40
    snake_size=15
    fps=50
    vel_x=0
    vel_y=0
    increment=5
    food_x=random.randint(50,width-20)
    food_y=random.randint(50,height-20)
    snk_list = []
    snk_length = 1
Game_vars()



def plot_snake(gameWindow, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,(10,100,0), [x, y, snake_size, snake_size])

def text_display(text,x,y):
    font=pygame.font.SysFont(None,35)
    screen_text=font.render(text,True,(0,0,0))
    gameWindow.blit(screen_text,[x,y])

clock=pygame.time.Clock()
#Game Loop



def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        gameWindow.blit(welimg, (0, 0))

        font=pygame.font.SysFont(None,55)
        screen_text=font.render("Welcome to Snake Game",True,(10,10,255))
        gameWindow.blit(screen_text,[330,50])

        font=pygame.font.SysFont(None,50)
        screen_text=font.render("Press Space Bar To Start",True,(0,0,0))
        gameWindow.blit(screen_text,[330,400])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('start.mp3')
                    pygame.mixer.music.play()
                    exit_game=True
                    break

        pygame.display.update()
        clock.tick(60)

welcome()

while not exit_game:
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    for event in pygame.event.get():
        # print(event)
        if event.type ==pygame.QUIT:
            exit_game=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_x=increment
                vel_y=0
            if event.key == pygame.K_LEFT:
                vel_x=-increment
                vel_y=0
            if event.key == pygame.K_UP:
                vel_y=-increment
                vel_x=0
            if event.key == pygame.K_DOWN:
                vel_y=increment
                vel_x=0

    snake_x=snake_x+vel_x
    snake_y=snake_y+vel_y
    if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
        pygame.mixer.music.load('point.mp3')
        pygame.mixer.music.play()
        Score+=1
        print("Score: ",Score)
        if Score>int(highscore):
            highscore=Score
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
        snk_length+=5
        food_x=random.randint(10,width-10)
        food_y=random.randint(10,height-10)


    gameWindow.fill(white)
    gameWindow.blit(bgimg, (0, 0))
    text_display("Score: "+str(Score)+"   HighScore: "+ str(highscore),5,5)
    pygame.draw.rect(gameWindow,(139,69,19),[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]

    if(snake_x>width or snake_x<0 or snake_y>height or snake_y<0 or head in snk_list[:-1]):
            
            text_display("Game Over!",width/2-100,height/2)
            pygame.display.update()
            pygame.mixer.music.load('game_over.mp3')
            pygame.mixer.music.play()
            pygame.time.delay(1200)
            exit_game=True
            pygame.quit()
            quit()
            # Game_vars()
            # gameWindow.fill(white)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Game_vars()

    plot_snake(gameWindow,snk_list,snake_size)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()