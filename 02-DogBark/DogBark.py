import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # DONE 1: Create an image with the 2dogs.JPG image
    dog_image = pygame.image.load("2dogs.JPG")
    # DONE 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    # DONE 4: Create a font object with a size 28 font.
    font_obect_1 = pygame.font.SysFont("verdana", 28)
    font_object_2 = pygame.font.SysFont("verdana", 20)

    # fonts = pygame.font.get_fonts()
    # for font in sorted(fonts):
    #    print(font)
    
    # DONE 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption_1 = font_obect_1.render("Two Dogs", True, BLACK)
    caption_2 = font_object_2.render("funny text", True, WHITE)
    # Prepare the music
    # DONE 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # DONE 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # DONE 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dog_image, (0, 0))
        # Draw the text onto the screen
        # DONE 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption_1, (screen.get_width() / 2 - caption_1.get_width() / 2,
                                screen.get_height() - caption_1.get_height() - 1))
        # DONE 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        screen.blit(caption_2, (100, 20))
        # Update the screen
        pygame.display.update()


main()
