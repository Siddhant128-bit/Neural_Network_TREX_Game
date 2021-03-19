import pygame
import random
pygame.init()
win=pygame.display.set_mode((500,200))
pygame.display.set_caption('AI_PATH_FINDER')
x1=10
y1=150
x2=30
y2=130
x3=15
y3=180
x4=28
y4=180
x5=0
y5=185
xog=600
yog=155
xoa=600
yoa=110
xgo=600
ygo=193
isduck=False
width_vary_ground=random.randrange(10,50)
width_vary_air=random.randrange(10,50)
vel=5
animation_count=0
run=True
jump_count=10
is_jump=False
score=0
with open('high_score.txt','r+')as f:
    h_score=f.readline()
h_score=int(h_score)
while run:
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('score: '+str(score), True, (0,0,0), (255,255,255))
    textRect = text.get_rect()
    text1 = font.render('Hscore: '+str(h_score), True, (0,0,0), (255,255,255))
    textRect1 = text1.get_rect()
    textRect1.center = (390,15)
    #exit the game!!!!!!!!!!!!!!!!!!!!
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump=True
        if keys[pygame.K_DOWN]:
            isduck=1
            if isduck==True:
                temp=155
                y2=temp

        else:
            isduck=0
            temp=130
            y2=temp

    else:
        print(jump_count)
        if jump_count>=-10:
            neg=1
            if jump_count<0:
                neg=-1

            y1-=(jump_count**2)*0.2*neg
            y2-=(jump_count**2)*0.2*neg
            y3-=(jump_count**2)*0.2*neg
            y4-=(jump_count**2)*0.2*neg
            jump_count-=1

        else:
            is_jump=False
            jump_count=10


    pygame.time.delay(20)
    win.fill((255,255,255))
    win.blit(text, textRect)
    win.blit(text1, textRect1)

    #get key pressed !!!!!!!!!!!!!!!!!!!!
    pygame.draw.rect(win,(0,0,0),(x1,y1,30,30))
    pygame.draw.rect(win,(0,0,0),(x2,y2,20,20))
    if animation_count%10==0:
        pygame.draw.rect(win,(0,0,0),(x3+1000,y3+1000,4,5))
        pygame.draw.rect(win,(0,0,0),(x4,y4,4,5))
    else:
        pygame.draw.rect(win,(0,0,0),(x3,y3,4,5))
        pygame.draw.rect(win,(0,0,0),(x4+1000,y4+1000,4,5))
    if (xog-xoa)<=100 or (xoa-xog)>=-100:
        xoa=xog+600

    pygame.draw.rect(win,(0,0,0),(x5,y5,600,5))
    pygame.draw.rect(win,(0,0,0),(xog,yog,width_vary_ground,30))
    pygame.draw.rect(win,(0,0,0),(xoa,yoa,width_vary_air,30))
    pygame.draw.rect(win,(0,0,0),(xgo,ygo,10,10))
    xog=xog-vel
    xgo=xgo-vel
    xoa=xoa-vel
    if xog<0:
        score=score+10
        xog=random.randrange(500,2000)
        xgo=random.randrange(500,600)
        width_vary_ground=random.randrange(10,50)
        binary=random.randint(1,2)
        if binary==1:
            vel=vel+(random.randint(1,10)/10)
        elif binary==2:
            vel=vel-(random.randint(1,6)/10)
    if xoa<0:
        score=score+10
        xoa=random.randrange(500,2000)
        print(yoa)
        yoa=random.randrange(90,110)
        width_vary_air=random.randrange(10,50)
        binary=random.randint(1,2)
        if binary==1:
            vel=vel+(random.randint(1,10)/10)
        elif binary==2:
            vel=vel-(random.randint(1,6)/10)

    if x2-xoa>=-200:
        print(y1-yoa)

    if (x1-xog>=-2 and y1-yog>=-2) or (x3-xog>=-2 and y4-yog>=-2) or (x2-xoa>=-2 and y2-yoa<=20 ):
        print('game over')
        if score>h_score:
            with open('high_score.txt','r+')as f:
                f.writelines(str(score))

        break
    pygame.display.update()
    animation_count+=5

pygame.quit()
