import pygame
import asyncio

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Wczytanie obrazków
img1 = pygame.image.load("Ranatin-1.png")
img2 = pygame.image.load("Ranatin-2.png")
img3 = pygame.image.load("Ranatin-3.png")

async def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # Zdjêcia jedno pod drugim
        screen.blit(img1, (100, 50))
        screen.blit(img2, (100, 300))
        screen.blit(img3, (100, 550))

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

asyncio.run(main())