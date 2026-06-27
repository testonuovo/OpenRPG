import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ChronoQuest")

clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((25, 25, 25))

    pygame.display.flip()

pygame.quit()