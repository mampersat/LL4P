import sys, pygame
pygame.init()

size = width, height = 320, 800
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
red = (255,0,0)
screen.fill(red)
pygame.display.update()


car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (100,200))
car_rect = car_img.get_rect()

car = {
    'speed': 50,
    'position': 0
}


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    car_rect = car_rect.move(speed)
    if car_rect.left < 0 or car_rect.right > width:
        speed[0] = -speed[0]
    if car_rect.top < 0 or car_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(red)
    screen.blit(car_img, car_rect)
    pygame.display.flip()