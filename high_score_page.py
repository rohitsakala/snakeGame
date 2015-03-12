try:
    import pygame
    import sys
    import os
    import random
    import main_page
    import first_page
    import pickle
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

    screen.blit(background_image, (0,0))

    back_button=pygame.image.load("images/start_button.jpg")
    back_button_rect = screen.blit(back_button,(500,100))

    while True:

        score_list = []
        with open('high_score.pkl', 'rb') as input:
            score_list = pickle.load(input)
        
        font = pygame.font.SysFont("comicsansms", 35)

        high_head = font.render("High Score",1,(0,0,0))
        screen.blit(high_head,(150,20)) 

        font = pygame.font.SysFont("comicsansms", 35)

        for i in xrange(len(score_list) - 1):
            num = str(i+1)
            num_d = font.render(num,1,(0,0,0))
            score_int = str(score_list[i])
            score=font.render(score_int,1,(0,0,0))
            screen.blit(num_d,(150,10+((i+1)*70)))
            screen.blit(score,(200,10+((i+1)*70)))

    	mos_x,mos_y=pygame.mouse.get_pos()    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            	if back_button_rect.collidepoint((mos_x,mos_y)):
            		first_page.main()

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
