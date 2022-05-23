import pygame
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
image_fond = pygame.image.load("fond.jpg")
 
clock = pygame.time.Clock()  #Créer un objet "horloge", trace du temps
 
snake_block = 10    
snake_speed = 20
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Ton_score(score:int)->int:  # Affichage du score, en haut à gauche
    """
    Affiche le score du Joueur en haut à gauche de l'écran de jeu
    """
    value = score_font.render("Score : " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
def le_snake(snake_block:int, snake_list:list):  # Création du serpent 
    """
    Dessine le serpent, snake_head prend en compte la position x et y, l'ajoute à la liste snake_list 
    """
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg:str, color:tuple):  # Message de fin
    """
    Affiche le message de fin, Game over, propose de rejouer ou de quitter le jeu 
    """
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 11, dis_height / 3])
 
 
def gameLoop():  
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_liste = []
    taille_snake = 1
 
    foodx = round(random.randrange(0, dis_width) / 10) * 10
    foody = round(random.randrange(0, dis_height) / 10) * 10
 
    while not game_over:
 
        while game_close == True:
            dis.blit(image_fond, (0,0))
            message("Game over ! C pour relancer ou Q pour quitter", red)
 
            pygame.display.update()
 
            for event in pygame.event.get():  #Touche de fin de jeu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():  #Touche de jeu
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= dis_width or x1 < 0:  #Délimitation du terrain
            game_close = True
        elif y1 >= dis_height or y1 < 0:
            game_close = True
 
        
        x1 += x1_change
        y1 += y1_change
        dis.blit(image_fond, (0,0))
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_liste.append(snake_Head)
        if len(snake_liste) > taille_snake:
            del snake_liste[0]
 
        for x in snake_liste[:-1]:
            if x == snake_Head:
                game_close = True
 
        le_snake(snake_block, snake_liste)
        Ton_score(taille_snake - 1)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            taille_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
gameLoop()