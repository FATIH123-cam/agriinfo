
import pygame


pygame.init()

SCREEN_WIDTH = 800
SCREEN_LENGTH = 800

screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
pygame.display.set_caption("Main menu")

# game variables
game_paused = False

# define font
font = pygame.font.SysFont("arialblack",40)

# define colours
TEXT_COLOR = (255,255,255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

# game run
run = True
while run:

    screen.fill((52,78,91))

    # check jf game is paused
    if game_paused == True :
        pass
    # display menu
    else:
        draw_text("press SPACE to pause", font, TEXT_COLOR, 160, 250)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()
pygame.quit()
