import pygame, random

screen = pygame.display.set_mode((1200, 500)) #экран и его размер

draw_on = False #запуск процесса рисования
last_pos = (0, 0) #координаты
color = (255, 128, 0) #цвет
radius = 30 #размер ручки

def roundline(screen, color, start, end, radius=1): #функция рисования
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy) #нахождение координат на которых будет рисовать ручка
        pygame.draw.circle(screen, color, (x, y), radius)

try:
    while True:
        e = pygame.event.wait() # е это переменная отвечающая за события
        if e.type == pygame.QUIT: #выход
            raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button==1: #для левой кнопки мыши
                color = (random.randrange(256), random.randrange(256), random.randrange(256))
                pygame.draw.circle(screen, color, e.pos, radius)
                draw_on = True #включен процесс рисования
            if e.button==3: #для правой кнопки мыши
                color = (0,0,0)
                pygame.draw.circle(screen, color, e.pos, radius)
                draw_on = True
        if e.type == pygame.MOUSEBUTTONUP: #не нажаты кнопки на мыши
            draw_on = False #выключение процесса рисования
        if e.type == pygame.MOUSEMOTION: #в случае движения мышки
            if draw_on: #и если процесс рисования вкл
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos
        pygame.display.flip() #обновление экрана
except StopIteration:
    pass

pygame.quit() #выход

