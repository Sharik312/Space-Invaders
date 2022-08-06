import pygame, time, os # Importing necessary libraries
pygame.font.init() # initialising Pygame Font
pygame.init() # initialising Pygame


# Color Variables
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (30, 255, 65)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Basic Variables
SC_WIDTH, SC_LENGTH = 600, 650
SHIP_WIDTH, SHIP_LENGTH = 110, 80
SHIP = pygame.Rect(SC_WIDTH/2 - (SHIP_WIDTH/2), SC_LENGTH*0.7, SHIP_WIDTH, SHIP_LENGTH)
TEXT_FONT = pygame.font.SysFont("comicsans", 35)
FPS = 60
HEALTH = 10
VEL = 8

# Importing Assets
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (1152, 650))

SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", 'spaceship_red.png'))

SHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_LENGTH)), 180)

# Creating Window
WIN = pygame.display.set_mode((SC_WIDTH, SC_LENGTH))
pygame.display.set_caption("Space Invaders!")

# Function for Game Start
def game_start():
    game_start_text = TEXT_FONT.render("Press Any Key To Start", 1, WHITE)
    WIN.fill(BLACK) # Setting Background Color to Black
    
    WIN.blit(game_start_text, (SC_WIDTH/2 - (game_start_text.get_width()/2), SC_LENGTH*0.75))
    pygame.display.update() # Updating Screen


def ship_movement(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and SHIP.x - VEL > 0:
        SHIP.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and SHIP.x + SHIP.width + VEL < SC_WIDTH:
        SHIP.x += VEL
    if keys_pressed[pygame.K_DOWN] and SHIP.y - VEL + SHIP.height < SC_LENGTH-25:
        SHIP.y += VEL
    if keys_pressed[pygame.K_UP] and SHIP.y - VEL > SC_LENGTH/2 + (SHIP_LENGTH):
        SHIP.y -= VEL

# Function for drawing Game Screen
def draw_window():
    WIN.blit(SPACE, (0, 0))

    hp_text = TEXT_FONT.render("Health: " + str(HEALTH), 1, WHITE)

    WIN.blit(SHIP_IMAGE, (SHIP.x, SHIP.y))
    WIN.blit(hp_text, (10, 10))
    pygame.display.update()

# Main Function
def main():
    clock = pygame.time.Clock()
    game_started = False

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if game_started == False:
                game_start()
                if event.type == pygame.KEYDOWN:
                    game_started = True
                    draw_window()
                    continue
            
            

        
        if game_started == True:
            keys_pressed = pygame.key.get_pressed()
            ship_movement(keys_pressed)
            draw_window()

        













if __name__ == "__main__":
    main()