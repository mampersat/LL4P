import sys, pygame, time, random
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

def add_car():
    car = {
        'speed': random.random() * 100, 
        'position':0, 
        'rect': car_rect, 
        'lane': random.random() * 2,
        'born' : time.time(),
        }

    cars.append(car)

add_car()
add_car()
add_car()
add_car()

start = time.time()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(red)

    for car in cars:

        # seconds since this car was born
        elapsed = time.time() - car['born']

        # calculate position based on elapsed time    
        car['position'] = car['speed'] * elapsed
        
        if car['position'] > height +200:
            car['born'] = time.time()


        car['rect'].left = 10 + 100 * car['lane'] 
        car['rect'].bottom = car['position']
        
        screen.blit(car_img, car['rect'])

    pygame.display.flip()
