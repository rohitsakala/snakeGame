try:
    import pygame
    import sys
    import os
    import random
    import high_score_page
    import main_page
except ImportError as err:
    print "Couldn't load module. %s" % (err)
    sys.exit(2)


def main():

    pygame.init()

    # Initialize Screen
    window_Info = pygame.display.Info()
    screen = pygame.display.set_mode(
        (window_Info.current_w, window_Info.current_h))
    pygame.display.set_caption('Snake Game')

    # Background Image
    background_image, background_image_rect = load_image(
        'snake_background.png')

    screen.blit(background_image, (0, 0))

    start_button = pygame.image.load("images/start_button.jpg")
    start_button_rect = screen.blit(start_button, (100, 100))

    high_score_button = pygame.image.load("images/start_button.jpg")
    high_score_button_rect = screen.blit(high_score_button, (100, 500))

    middle_snake, middle_snake_rect = load_image('snake_first_middle.jpg')
    screen.blit(middle_snake, (700, 200))

    # Text
    font = pygame.font.SysFont("comicsansms", 55)

    snake_head = font.render("Snake Game!!!",1,(0,0,0))
    screen.blit(snake_head,(500,10))

    font = pygame.font.SysFont("comicsansms", 35)

    info_head = font.render("Info", 1, (0, 0, 0))
    screen.blit(info_head, (1000, 100))

    font = pygame.font.SysFont("comicsansms", 25)

    for i in xrange(3):
        num = str(i + 1)
        num_d = font.render(num, 1, (0, 0, 0))
        screen.blit(num_d, (970, 100 + ((i + 1) * 70)))

    num_d = font.render("4", 1, (0, 0, 0))
    screen.blit(num_d, (970, 420))

    point_1 = font.render("Press arrow keys to control the snake!",1,(0,0,0))
    screen.blit(point_1,(1020,170))

    point_2 = font.render("For each insect you catch you score 5 points and for a spider 10 points!",1,(0,0,0))
    screen.blit(point_2,(1020,240))

    point_3 = font.render("The game will quit if you go in the backward direction or ",1,(0,0,0))
    screen.blit(point_3,(1020,310))

    point_3_1 = font.render("if your snake touches the borders!!!",1,(0,0,0))
    screen.blit(point_3_1,(1020,350))

    point_4 = font.render("Developed By SVK Rohit, IIIT Hyderabad!!!!",1,(0,0,0))
    screen.blit(point_4,(1020,420))

    while True:

        mos_x, mos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button_rect.collidepoint((mos_x, mos_y)):
                    main_page.main()
                elif high_score_button_rect.collidepoint((mos_x, mos_y)):
                    high_score_page.main()

        pygame.display.update()


def load_image(name):
    """ Load image and return image object"""

    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print 'Cannot load image:', fullname
        raise SystemExit(message)
    return image, image.get_rect()


if __name__ == "__main__":
    main()
