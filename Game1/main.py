import pygame
import time
import random

# Constant variables -> WIDTH, HEIGHT
WIDTH, HEIGHT = 1000, 700

# Set the window and it's width and height
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
# Set the window title
pygame.display.set_caption("Space Dodge")

# Initialize pygame's font
pygame.font.init()

# Set the background variable
BG = pygame.transform.scale(pygame.image.load("Game1/bg.jpeg"),(WIDTH,HEIGHT))



# Initialize player stats -> player width, player height, player velocity
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_VELOCITY = 5



# Initialize star(projectiles) stats -> star width, star height, star velocity
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 3


# Add the font style and size
FONT = pygame.font.SysFont("comicsans", 30)

def draw(player,elapsed_time,stars):
    """
    Args: 
        player -> The player is the red rectangle at the beginning
        elapsed_time -> Time displayed at the top left corner. AKA score.
        stars -> Projectiles to stay away from
    Returns:
        None
    """

    # Display(blit) the background to the window
    WIN.blit(BG, (0,0))


    # Render the text
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    # display the rendered text to the coordinates(10,10)
    WIN.blit(time_text, (10,10))

    # Draw the player on the window
    pygame.draw.rect(WIN, "red", player)


    # Render the stars to descent to the bottom of the screen. In this case three projectiles at a time
    for star in stars:
        pygame.draw.rect(WIN,"white",star)

    # Update the display every time the draw function is called in the while loop
    pygame.display.update()



def main():
    run = True

    # Player as a red rectangle is rendered on the screen
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT ,PLAYER_WIDTH,PLAYER_HEIGHT)


    # Pygame clock initialized
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    hit = False


    stars = []

    # Main game loop
    while run:
        star_count += clock.tick(90)
        elapsed_time = time.time() - start_time
        

        # star_add_increment is 2000ms and if the star count crosses the increment 
        # it is time to generate the next three stars
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH,STAR_HEIGHT)
                stars.append(star)
        
            star_add_increment = max(200, star_add_increment - 50)
            #Reset the star count
            star_count = 0




        # For loop that makes sure the event continues until the user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        

        # Key binds and player bounds
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >=0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_d] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VELOCITY
        if keys[pygame.K_w] and player.y - PLAYER_VELOCITY >= HEIGHT - 250:
            player.y -= PLAYER_VELOCITY
        if keys[pygame.K_s] and player.y + PLAYER_HEIGHT +PLAYER_VELOCITY <= HEIGHT:
            player.y += PLAYER_VELOCITY


        # stars[:] -> creates a copy so the original can be modified
        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break


        # hit = True causes the game to be over and render "You Lost" text onto the middle of the screen
        if hit:
            lost_text = FONT.render("You Lost", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        # Call the draw function to display the player, time taken and the stars generated
        draw(player,elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()