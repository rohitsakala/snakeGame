#!/usr/bin/python

try:
    import pygame
    import sys
    import os
    import random
    import pickle
    import first_page
    import score_page
except ImportError as err:
    print "Couldn't load module. %s" % (err)
    sys.exit(2)

    # To do photoshop of head_close and body part


class Snake_Head_Open():

    """A snake class which is responsible for the movements
       of the snake and its length"""

    def __init__(self, x, y):
        self.image, self.rect = load_image(
            'snake_head_open_left.png')
        self.rect[0] = x
        self.rect[1] = y
        self.score = 0
        self.direction = "left"
        self.no_of_insects = 0
        self.no_of_spiders = 0

class Snake_Tail():

    """A snake class which is responsible for the movements
       of the snake and its lenght"""

    def __init__(self, x, y):
        self.image, self.rect = load_image(
            'snake_tail_left.png')
        self.rect[0] = x
        self.rect[1] = y       

class Snake_Part():

    """A snake class which is responsible for the movements
       of the snake and its lenght"""

    def __init__(self, x, y):
        self.image, self.rect = load_image(
            'snake_body.png')
        self.rect[0] = x
        self.rect[1] = y
        
class Insect(pygame.sprite.Sprite):

    """A ball class which is food to the snake"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('snake_head_open_left.png')
        self.rect[0] = x
        self.rect[1] = y
        self.score = 5


class Spider(pygame.sprite.Sprite):

    """A spider class which is food to the snake"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('snake_head_open_left.png')
        self.rect[0] = x
        self.rect[1] = y
        self.score = 10

def main():

    # Initialize Screen
    pygame.init()
    window_Info = pygame.display.Info()
    screen = pygame.display.set_mode(
        (window_Info.current_w, window_Info.current_h))
    pygame.display.set_caption('Snake Game')

    # Background Image
    background_image, background_image_rect = load_image(
        'snake_background.png')

    # For positioning snake
    x = 800
    y = 600 

    # Initialize Snake
    global snake_head_open
    global snake_part
    snake_part = []
    global snake_tail
    global insect
    global snake_part_length
    snake_part_length = 3

    snake_head_open = Snake_Head_Open(x, y)
    for i in xrange(3):
        snake_part.append(Snake_Part(x + 32 + (32 * i), y))
    snake_tail = Snake_Tail(x + (32 * 4), y)

    #For positioning insect
    x1 = random.randint(132, window_Info.current_w - 132)
    y1 = random.randint(132, window_Info.current_h - 132)

    #Initialize insect
    insect = Insect(x1, y1)

    #Initialize spider
    x2 = 0
    y2 = 0
    spider = Spider(x2, y2) 
    flag = 0

    # Blit everything to the screen
    screen.blit(background_image, (0, 0))
    pygame.display.update()

    # Initialise clock
    clock = pygame.time.Clock()
    timer = 0

    # Event Loop
    while True:
        timer = timer + 1
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('high_score.pkl', 'rb') as input:
                    score_list = pickle.load(input)
                if len(score_list) > 10:
                    score_list[9] = snake_head_open.score
                else:
                    score_list.append(snake_head_open.score)
                score_list.sort(reverse=True)
                with open('high_score.pkl', 'wb') as output:
                    pickle.dump(score_list, output, pickle.HIGHEST_PROTOCOL)
                score_page.main(snake_head_open.score)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_head_open.direction = "up"
                elif event.key == pygame.K_DOWN:
                    snake_head_open.direction = "down"
                elif event.key == pygame.K_LEFT:
                    snake_head_open.direction = "left" 
                elif event.key == pygame.K_RIGHT:
                    snake_head_open.direction = "right"

        screen.blit(background_image, snake_head_open.rect, snake_head_open.rect)
        for i in xrange(snake_part_length):
            screen.blit(background_image, snake_part[i].rect, snake_part[i].rect)
        screen.blit(background_image, snake_tail.rect, snake_tail.rect)
        screen.blit(background_image, insect.rect, insect.rect)
        screen.blit(background_image, spider.rect, spider.rect)

        #Draw Borders
        pygame.draw.line(screen, (0,0,0), (100, 100), (window_Info.current_w - 100, 100), 4)
        pygame.draw.line(screen, (0,0,0), (100, 100), (100,window_Info.current_h - 100), 4)
        pygame.draw.line(screen, (0,0,0), (100, window_Info.current_h - 100), (window_Info.current_w - 100, window_Info.current_h - 100), 4)
        pygame.draw.line(screen, (0,0,0), (window_Info.current_w - 100, 100), (window_Info.current_w - 100, window_Info.current_h - 100), 4)

        #List of rects of snake
        snake_rect_list = []
        snake_rect_list.append(snake_head_open.rect)
        snake_rect_list.append(snake_tail.rect)
        for i in xrange(snake_part_length):
            snake_rect_list.append(snake_part[i].rect)
        snake_rect_list.append(snake_tail.rect)

        #Collision between spider and the snake
        if snake_head_open.no_of_insects != 0 and snake_head_open.no_of_insects % 5 == 0 and flag == 0:
            flag = 1
            timer = 0
            x2 = random.randint(132, window_Info.current_w - 132)
            y2 = random.randint(132, window_Info.current_h - 132)
            spider.rect[0] = x2
            spider.rect[1] = y2
            while spider.rect.collidelist(snake_rect_list) != -1 and spider.rect.colliderect(insect.rect) == True:
                x2 = random.randint(132, window_Info.current_w - 132)
                y2 = random.randint(132, window_Info.current_h - 132)
                spider.rect[0] = x2
                spider.rect[1] = y2
            
        if flag == 1:
            if timer < 200:
                screen.blit(spider.image , spider.rect)
                if snake_head_open.rect.colliderect(spider.rect):
                    snake_head_open.score = snake_head_open.score + spider.score
                    snake_head_open.no_of_spiders =  snake_head_open.no_of_spiders + 1
                    timer = 300
        else:
            flag = 0

        #Collision between the snake and wall
        if snake_head_open.rect[0] > (window_Info.current_w - 132) or snake_head_open.rect[1] > (window_Info.current_h - 132) or snake_head_open.rect[0] < 100 or snake_head_open.rect[1] < 100:
            with open('high_score.pkl', 'rb') as input:
                score_list = pickle.load(input)
            if len(score_list) > 10:
                score_list[9] = snake_head_open.score
            else:
                score_list.append(snake_head_open.score)
            score_list.sort(reverse=True)
            with open('high_score.pkl', 'wb') as output:
                pickle.dump(score_list, output, pickle.HIGHEST_PROTOCOL)
            score_page.main(snake_head_open.score) 

        #Collision between snake and the insect
        if snake_head_open.rect.colliderect(insect.rect):
            snake_head_open.score = snake_head_open.score + insect.score
            snake_head_open.no_of_insects = snake_head_open.no_of_insects + 1
            snake_part.append(Snake_Part(snake_part[snake_part_length - 1].rect[0],snake_part[snake_part_length - 1].rect[1]))
            snake_part_length = snake_part_length + 1   
            x1 = random.randint(132, window_Info.current_w - 132)
            y1 = random.randint(132, window_Info.current_h - 132)
            insect.rect[0] = x1
            insect.rect[1] = y1
            while insect.rect.collidelist(snake_rect_list) != -1:
                x1 = random.randint(132, window_Info.current_w - 132)
                y1 = random.randint(132, window_Info.current_h - 132)
                insect.rect[0] = x1
                insect.rect[1] = y1
        else:
            snake_tail.rect[0] = snake_part[snake_part_length - 1].rect[0]
            snake_tail.rect[1] = snake_part[snake_part_length - 1].rect[1]
            

        #Movement of the rest of the snake
        for i in xrange(snake_part_length-1,0,-1):
            snake_part[i].rect[0] = snake_part[i - 1].rect[0]
            snake_part[i].rect[1] = snake_part[i - 1].rect[1]

        snake_part[0].rect[0] = snake_head_open.rect[0]
        snake_part[0].rect[1] = snake_head_open.rect[1]

        #Movement of the head of the snake
        if snake_head_open.direction == "left":
            snake_head_open.rect[0] = snake_head_open.rect[0] - 32
            fullname = os.path.join('images', 'snake_head_open_left.png')
            snake_head_open.image = pygame.image.load(fullname).convert()
        elif snake_head_open.direction == "right":
            snake_head_open.rect[0] = snake_head_open.rect[0] + 32
            fullname = os.path.join('images', 'snake_head_open_right.png')
            snake_head_open.image = pygame.image.load(fullname).convert()
        elif snake_head_open.direction == "up":
            snake_head_open.rect[1] = snake_head_open.rect[1] - 32
            fullname = os.path.join('images', 'snake_head_open_up.png')
            snake_head_open.image = pygame.image.load(fullname).convert()
        elif snake_head_open.direction == "down":
            snake_head_open.rect[1] = snake_head_open.rect[1] + 32
            fullname = os.path.join('images', 'snake_head_open_down.png')
            snake_head_open.image = pygame.image.load(fullname).convert()

        if snake_part[snake_part_length - 1].rect[1] - snake_tail.rect[1] > 0:
            fullname = os.path.join('images', 'snake_tail_down.png')
            snake_tail.image = pygame.image.load(fullname).convert() 
        elif snake_part[snake_part_length - 1].rect[1] - snake_tail.rect[1] < 0 :
            fullname = os.path.join('images', 'snake_tail_up.png')
            snake_tail.image = pygame.image.load(fullname).convert()
        elif snake_part[snake_part_length - 1].rect[0] - snake_tail.rect[0] > 0:
            fullname = os.path.join('images', 'snake_tail_right.png')
            snake_tail.image = pygame.image.load(fullname).convert()
        else:
            fullname = os.path.join('images', 'snake_tail_left.png')
            snake_tail.image = pygame.image.load(fullname).convert()    


        screen.fill(pygame.Color("white"), (290, 16, 60,26))

        #Show boarders for score
        pygame.draw.line(screen, (0,0,0), (290, 16), (350,16), 3)
        pygame.draw.line(screen, (0,0,0), (350, 16), (350,42), 3)
        pygame.draw.line(screen, (0,0,0), (350, 42), (290,42), 3)
        pygame.draw.line(screen, (0,0,0), (290, 42), (290,16), 3)

        #Show score on the top
        font = pygame.font.SysFont("comicsansms", 25)
        Score = font.render("Score :",1,(0,0,0))
        score_int = str(snake_head_open.score)
        score=font.render(score_int,1,(0,0,0))
        screen.blit(score,(300,10))
        screen.blit(Score,(200,10))

        snake_rect_list_ex_head = []
        snake_rect_list_ex_head.append(snake_tail.rect)
        for i in xrange(snake_part_length):
            snake_rect_list_ex_head.append(snake_part[i].rect)
        #Collision between snake_head and itself
        if snake_head_open.rect.collidelist(snake_rect_list_ex_head) != -1:
            first_page.main()

        screen.blit(snake_head_open.image ,snake_head_open.rect)
        for i in xrange(snake_part_length):
            screen.blit(snake_part[i].image ,snake_part[i].rect)
        screen.blit(snake_tail.image ,snake_tail.rect)
        screen.blit(insect.image ,insect.rect)
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
