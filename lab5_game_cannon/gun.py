import math
from random import choice, randint, random
import tkinter
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600




class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.left_to_live = 5
        self.color = BLACK
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть,
        обновляет значения self.x и self.y с учетом скоростей
        self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        global balls
        g = 30/FPS
        self.vy -= g
        hitwall = (self.x<self.r) or (800-self.x<self.r)
        if hitwall:
            self.vx = -self.vx
        hitfloor = (self.y>600-self.r)
        if not hitfloor:
            pass
        else:
            self.vy += g
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        self.vx *=0.97	# замедление мяча
        self.vy *=0.97
        self.left_to_live -= 1 / FPS
        if self.left_to_live <= 0:
            balls.pop(0)

    
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью,
        описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели.
            В противном случае возвращает False.
        """
        hit = (obj.x-self.x)**2+(obj.y-self.y)**2<(obj.r+self.r)**2
        if hit:
            return hit


class Rocket(Ball):
    def __init__(self,screen,x,y):
        super().__init__(screen,x,y)
        self.r = 3

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        rocket_beyond = (self.x >= 800) or (self.x <= 0) or(self.y >= 600) or (self.y <= 0)
        if rocket_beyond:
            balls.pop(0)

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.length = 30
        self.width = 8
        self.color = GREY
        self.x1 = 30
        self.y1 = 530
        self.shell = 'ball'

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от
        положения мыши.
        """
        global balls, bullet
        bullet += 1
        if self.shell == 'ball':
            new_shell = Ball(self.screen, self.x1, self.y1) #мяч создается в пушке
            self.an = math.atan2((event.pos[1] - new_shell.y),
                                 (event.pos[0] - new_shell.x))
            new_shell.vx = self.f2_power * math.cos(self.an)
            new_shell.vy = - self.f2_power * math.sin(self.an)
        elif self.shell == 'rocket':
            new_shell = Rocket(self.screen, self.x1, self.y1)  # мяч создается в пушке
            self.an = math.atan2((event.pos[1] - new_shell.y),
                                 (event.pos[0] - new_shell.x))
            new_shell.vx = self.f2_power * math.cos(self.an)/3
            new_shell.vy = - self.f2_power * math.sin(self.an)/3
        balls.append(new_shell)
        self.f2_on = 0
        self.f2_power = 10
        self.length = 30

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1]-self.y1),
                                    (event.pos[0]-self.x1))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def change_shell(self):
        if self.shell == 'ball':
            self.shell = 'rocket'
        elif self.shell == 'rocket':
            self.shell = 'ball'

    def draw(self):
        self.draw_muzzle()
        self.draw_cart()
        
    def draw_muzzle(self):
        """Направление пушки зависит от положения мыши, прямоугольник ABCD, толщиной width"""
        S = (self.x1,self.y1)
        A = (self.x1+self.width/2*math.cos(self.an-math.pi/2),
                self.y1+self.width/2*math.sin(self.an-math.pi/2))
        B = (self.x1+self.width/2*math.cos(self.an+math.pi/2),
                self.y1+self.width/2*math.sin(self.an+math.pi/2))
        C = (B[0]+self.length/2*math.cos(self.an),
                B[1]+self.length/2*math.sin(self.an))
        D = (A[0]+self.length/2*math.cos(self.an),
                A[1]+self.length/2*math.sin(self.an))
        pygame.draw.polygon(self.screen, self.color, [A,B,C,D])
        pygame.draw.aalines(self.screen, self.color, True, [A,B,C,D])

    def draw_cart(self):
        pass

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.length += 1/3
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        self.type = 0
        self.x = randint(50, 750)
        self.y = randint(50, 500)
        self.r = 40
        self.color = RED
        self.points = 0
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global game_round
        self.points += points
        game_round.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        
    def move(self):
        pass


class Airplane_Target(Target):
    def __init__(self):
        super().__init__()
        self.type = 1
        self.x = 50
        self.y = randint(50, 400)
        self.r = 20
        self.color = GREEN
        self.points = 0
        self.live = 1
        self.vx = 2
        self.tan = (random() - 0.5) / 4

    def move(self):
        global targets
        self.x += self.vx
        self.y += self.vx * self.tan
        if self.x >= 800:
            targets.remove(self)
            targets.append(Airplane_Target())


class Balloon_Target(Target):
    def __init__(self):
        super().__init__()
        self.type = 2
        self.r = 35
        self.y = randint(100, 450)
        self.vy = 2
        self.time = 0

    def move(self):
        self.time += 1/FPS
        self.y += math.sin(self.time/2*math.pi)


class Game_round:
    def __init__(self, number=1, points=0):
        self.number = number
        self.targets_on_screen = 3
        self.targets_in_round = self.number+3
        self.phase = 0
        self.points = points
    
    def hello(self,screen):
        screen.fill(WHITE)
        font1 = pygame.font.Font(None, 36)
        hello = 'Раунд '+str(self.number)
        text1 = font1.render(hello, True, RED)
        screen.blit(text1, (WIDTH/2-30, HEIGHT/2-18))
        pygame.display.update()
        
    def goodbye(self,screen):
        global balls, targets
        screen.fill(WHITE)
        font1 = pygame.font.Font(None, 36)
        goodbye = 'Раунд '+str(self.number)+' закончен'
        result = 'Ваши очки: '+str(self.points)
        text1 = font1.render(goodbye, True, RED)
        text2 = font1.render(result, True, RED)
        screen.blit(text1, (WIDTH/2-60, HEIGHT/2-18))
        screen.blit(text2, (WIDTH/2-60, HEIGHT/2+18))
        pygame.display.update()
        balls.clear()
        targets.clear()
    
    def start(self,screen):
        global gun, targets
        gun = Gun(screen)
        for i in range(self.targets_on_screen):
            t = choice([Airplane_Target(),Balloon_Target()])
            targets.append(t)
        
    def draw(self, screen):
        screen.fill(WHITE)
        gun.draw()
        for t in targets:
            t.draw()
        for b in balls:
            b.draw()
        pygame.display.update()
        
    def update(self):
        global targets,balls
        gun.power_up()
        for t in targets:
            t.move()
        for b in balls:
            b.move()
            for t in targets:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    self.targets_in_round -= 1
                    targets.remove(t)
                    if self.targets_in_round == 0:
                        self.phase = 2
                    else:
                        targets.append(Airplane_Target())
                    balls.pop(0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []
game_rounds = []

clock = pygame.time.Clock()
game_round = Game_round()
finished = False

while not finished:
    clock.tick(FPS)
    
    if game_round.phase == 0:
        game_round.hello(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONUP:
                game_round.phase = 1
                game_round.start(screen)
    
    if game_round.phase == 1:
        game_round.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                gun.fire2_end(event)
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)
            elif event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
                gun.change_shell()
        game_round.update()
        
    if game_round.phase == 2:
        game_round.goodbye(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONUP:
                game_round = Game_round(game_round.number+1,game_round.points)

pygame.quit()
