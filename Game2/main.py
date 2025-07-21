import pygame


WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Shooter game')



BG_IMAGE = pygame.image.load('assets/space.png')
BG = pygame.transform.scale(BG_IMAGE,(WIDTH,HEIGHT))

YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load('assets/spaceship_yellow.png'),90)
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load('assets/spaceship_red.png'),-90)

SPACESHIP_SIZE = 35
SPACESHIP_VELOCITY = 6


player1 = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_SIZE,SPACESHIP_SIZE))
player2 = pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_SIZE,SPACESHIP_SIZE))


def draw(yellow,red):
    WIN.blit(BG, (0,0))

    WIN.blit(player1,(yellow.x,yellow.y))
    WIN.blit(player2,(red.x,red.y))
    pygame.display.update()





def get_key_pressed(keys,yellow,red,player:str):
    if player == "yellow":
        #Yellow spaceship movement and boundries
        if keys[pygame.K_w] and yellow.y >=0:
            yellow.y-=SPACESHIP_VELOCITY
        if keys[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_SIZE:
            yellow.y+=SPACESHIP_VELOCITY
        if keys[pygame.K_a] and yellow.x>=0:
            yellow.x-=SPACESHIP_VELOCITY
        if keys[pygame.K_d] and yellow.x <= WIDTH/2 -SPACESHIP_SIZE:
            yellow.x+=SPACESHIP_VELOCITY
    
    elif player == "red":
        #Red spaceship movement and boundries
        if keys[pygame.K_UP] and red.y >=0:
            red.y -= SPACESHIP_VELOCITY
        if keys[pygame.K_DOWN] and red.y <= HEIGHT - SPACESHIP_SIZE:
            red.y += SPACESHIP_VELOCITY
        if keys[pygame.K_LEFT] and red.x >= WIDTH/2:
            red.x -= SPACESHIP_VELOCITY
        if keys[pygame.K_RIGHT] and red.x <= WIDTH - SPACESHIP_SIZE:
            red.x += SPACESHIP_VELOCITY








def main():

    yellow = pygame.Rect(10,HEIGHT/2 - SPACESHIP_SIZE,
                         SPACESHIP_SIZE,SPACESHIP_SIZE)
    red = pygame.Rect(WIDTH - SPACESHIP_SIZE - 10,
                      HEIGHT/2 - SPACESHIP_SIZE,
                      SPACESHIP_SIZE,SPACESHIP_SIZE)
    clock = pygame.time.Clock()
    run = True
    

    while run:


        clock.tick(90)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        keys = pygame.key.get_pressed()

        get_key_pressed(keys,yellow,red,"yellow")
        get_key_pressed(keys,yellow,red,"red")

        # #Yellow spaceship movement and boundries
        # if keys[pygame.K_w] and yellow.y >=0:
        #     yellow.y-=SPACESHIP_VELOCITY
        # if keys[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_SIZE:
        #     yellow.y+=SPACESHIP_VELOCITY
        # if keys[pygame.K_a] and yellow.x>=0:
        #     yellow.x-=SPACESHIP_VELOCITY
        # if keys[pygame.K_d] and yellow.x <= WIDTH/2 -SPACESHIP_SIZE:
        #     yellow.x+=SPACESHIP_VELOCITY


        # #Red spaceship movement and boundries
        # if keys[pygame.K_UP] and red.y >=0:
        #     red.y -= SPACESHIP_VELOCITY
        # if keys[pygame.K_DOWN] and red.y <= HEIGHT - SPACESHIP_SIZE:
        #     red.y += SPACESHIP_VELOCITY
        # if keys[pygame.K_LEFT] and red.x >= WIDTH/2:
        #     red.x -= SPACESHIP_VELOCITY
        # if keys[pygame.K_RIGHT] and red.x <= WIDTH - SPACESHIP_SIZE:
        #     red.x += SPACESHIP_VELOCITY
        




        draw(yellow,red)
        

    pygame.quit()



if __name__ == "__main__":
    main()









