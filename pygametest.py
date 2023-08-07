import pygame

def main():
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Test Program")

    screen = pygame.display.set_mode((240,180))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = false

if __name__ == "__main__":
    main()