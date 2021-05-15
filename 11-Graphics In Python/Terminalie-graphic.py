import pygame as pg
import threading
# initialize the display
pg.init()
screen = pg.display.set_mode((300, 300))
white = (255, 255, 255)
screen.fill(white)
pg.display.update()
# pg.event.pump()
def cont():
    while True:
        pg.event.pump()

# t1 = threading.Thread(name= 'th1', target= cont)
# t1.start()
# t1.join()

color = (0, 0, 0)
size = 1
while True:
    # pg.event.pump()
    command = input()
    commands = command.split()
    if command == 'end drawing':
        break
    
    elif command.startswith('change color'):
        color = tuple([int(item) for item in commands[2:]])

    elif command.startswith('change size'):
        size = int(commands[2])
        
    elif command.startswith('draw line'):
        pointa = tuple([int(item) for item in commands[2:4]])
        pointb = tuple([int(item) for item in commands[4:]])
        pg.draw.line(screen, color, pointa, pointb, size)

    elif command.startswith('draw circle'):
        center = tuple([int(item) for item in commands[2:4]])
        diameter = int(commands[-1])
        pg.draw.circle(screen, color, center, diameter, size)
        
    elif command.startswith('draw polygon'):
        points = [(int(commands[i-1]), int(commands[i])) for i in range(3, len(commands), 2)]
        pg.draw.polygon(screen, color, points, size)
    
    pg.display.update()
    # pg.event.pump() 

pg.image.save(screen, 'draw.png') 
pg.quit()




# import pygame
# from math import pi

# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# red = (255, 0, 0)
# blue = (0, 0, 255)
# green = (0, 255, 0)
# gray = (128, 128, 128)

# screen.fill(gray)

# pygame.draw.line(screen, red, (300, 300), (600, 400))
# pygame.draw.circle(screen, red, (200, 200), 20)
# pygame.draw.rect(screen, blue, (400, 400, 30, 80))
# pygame.draw.ellipse(screen, blue, (450, 450, 100, 50))
# pygame.draw.polygon(screen, green, [(700, 500), (600, 500), (550, 450), (650, 440)])
# pygame.draw.lines(screen, green, True, [(700, 200), (600, 200), (550, 150), (650, 140)])
# pygame.draw.lines(screen, green, False, [(700, 350), (600, 350), (550, 300), (650, 290)])
# pygame.draw.arc(screen, red,  (210, 75, 150, 125), 3*pi/2, 2*pi)

# pygame.display.update()

# while True:
#     pygame.event.pump()