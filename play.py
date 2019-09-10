import sys, pygame, time
pygame.init()

size = width, height = 320, 800
speed = [1, 1]
black = 0, 0, 0
cars = []

screen = pygame.display.set_mode(size)
red = (255,0,0)
screen.fill(red)
pygame.display.update()


car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (100,200))
car_rect = car_img.get_rect()

cars.append( {'speed': 65, 'position':0, 'rect': car_rect, 'lane': 0})
cars.append( {'speed': 75, 'position':0, 'rect': car_rect, 'lane': 1})


start = time.time()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(red)

    # calculate seconds elapsed since starting
    elapsed = time.time() - start

    for car in cars:

        # calculate position based on elapsed time    
        car['position'] = car['speed'] * elapsed
        
        if car['position'] > height +200:
            car['position'] = 0

        car['rect'].left = 10 + 200 * car['lane'] 
        car['rect'].bottom = car['position']
        
        screen.blit(car_img, car['rect'])

    pygame.display.flip()
