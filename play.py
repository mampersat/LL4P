import sys, pygame
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

car = {
    'speed': 50,
    'position': 0,
    'rect': car_rect,
}

cars.append( car)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(red)

    for car in cars:
        print(car)
        
        car['position'] += 1 # car['speed'] 
        car['rect'].left = 10
        car['rect'].top = car['position']
        screen.blit(car_img, car['rect'])

    pygame.display.flip()
