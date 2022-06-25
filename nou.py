from pygame import *
import sys


#создание оана
win_width = 800
win_down = 600
window = display.set_mode((win_width,win_down))
display.set_caption('динозаврик')
background = transform.scale(image.load('fon.jpg'), (win_width, win_down))
point = 0
class GameSpraite(sprite.Sprite):
    def __init__(self, playre_imege, playre_x, playre_y,size_x,size_y, playre_speed,paver_gamp,isgamp):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(playre_imege),(size_x,size_y))
        self.speed = playre_speed
        self.rect = self.image.get_rect()
        self.rect.x = playre_x
        self.rect.y = playre_y
        self.paver = paver_gamp
        self.isgamp = isgamp

    # отрисовываем
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
# класс игрока
class Plair(GameSpraite):
    def update(self):
        keys= key.get_pressed()
        if keys[K_UP]:
            self.isgamp = True
        if not(self.isgamp):
            if keys[K_UP]:
                self.isgamp = True
        else:
            if self.paver >= -14:

                if self.paver <= 0:
                    self.rect.y += self.paver**2 / 4
                else:
                    self.rect.y -= self.paver**2 / 4
                self.paver-=2

            else:
                self.isgamp = False
                self.paver = 14
    def new(self,ret):
        self.image = transform.scale(image.load(ret),(self.size_x+35,self.size_y))
        finush = True
    def new2(self,ret):
        self.image = transform.scale(image.load(ret),(self.size_x,self.size_y))
        finush = True
class Enemi(GameSpraite):
    def upleut(self):
        self.rect.x-=self.speed
        if self.rect.x < -50:
            self.rect.x = win_width -20
            global point
            point += 1
            if reform == True:
                global p1
                p1 += 1
class bonys(GameSpraite):
    def upleut(self):
        self.rect.x-=self.speed
        if self.rect.x < -100:
            self.rect.x = win_width -20

class train(GameSpraite):
    def upleut(self):
        self.rect.x-=self.speed
        if self.rect.x < -200:
            self.rect.x = win_width -20
font.init()
font1 = font.Font(None,36)
text = font1.render("Счет: "+str(point),1,(0,0,0))

sprait_slaim = "slame.png"
sprait_slaim_fail = "slame_fail.png"

hiro = Plair(sprait_slaim,50,400,50,50,10,14,False)
enim = Enemi("enemi.png",700,380,70,70,25,16,False)
bony = bonys("bonys.png",1000,380,50,50,25,16,False)
x_tra = 0
trais=sprite.Group()
for i in range(1,12):
    trai = train("1_blok.png",x_tra,450,100,200,25,16,False)
    x_tra += 100
    trais.add(trai)


finush = False
game = True
clock=time.Clock()
FPS = 20
p = 10
p1 = 0
reform = False
# логика игры
while game:
    for e in event.get():
        if e.type==QUIT:
        	game = False

    if finush != True:
        window.blit(background,(0,0))
        text = font1.render("Счет: "+str(point),1,(0,0,0))
        window.blit(text,(10,20))
        hiro.update()
        hiro.reset()
        enim.upleut()
        enim.reset()
        if point >= 8:
            if point % 8 == 0:
                bony.upleut()
                bony.reset()
        for i in trais:
            i.upleut()
            i.reset()
        if point == p:
            p += 10
            FPS += 1
        if sprite.collide_rect(hiro,bony):
            reform = True
            hiro.new(sprait_slaim_fail)
        if p1== 8:
            hiro.new2(sprait_slaim)
            p1 = 0

            # finush = True


    # за цикливание
    display.update()
    clock.tick(FPS)
