import pygame
import random

pygame.init()
#-----똥
ddong = pygame.image.load("C:/Users/U107-10/Pictures/ddong.png")
ddong_width = ddong.get_rect().size[0]
ddong_height = ddong.get_rect().size[1]
ddong_pos = []
creat_bool = True
class DDong :
    def __init__(self,time) :
        self.check = True
        self.ddong_pos = []
        self.ddong_time = time
    
    def creat(self) :
        if (int(time_now)%self.ddong_time) == 0 and self.check :
            self.check = False
            self.ddong_pos.append([random.randrange(0,(screen_width-ddong_width+1)),0,random.uniform(0.1,0.3)])
        elif (int(time_now)%self.ddong_time) != 0 :
            self.check = True

    def down(self) :
        for i in self.ddong_pos :
            i[1] += i[2]*dt

    def delet(self) :
        for dd in self.ddong_pos :
            if dd[1] >= (560 - ddong_height) :
                del(self.ddong_pos[self.ddong_pos.index(dd)])      
#-----

enemy = ddong.get_rect()#충돌 처리용 변수

#-----스크린
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
#-----

pygame.display.set_caption("똥피하기")#타이틀

#-----배경
background = pygame.image.load("C:/Users/U107-10/Pictures/back.png")
#-----
#-----폰트
#타이머
timer_font = pygame.font.Font(None,40)
#게임오버
gameover_font = pygame.font.Font(None,100)
gameover = gameover_font.render("GAME OVER",True,(0,0,0))
#-----
#-----캐릭터
character = pygame.image.load("C:/Users/U107-10/Pictures/nom.png")
character_width = character.get_rect().size[0]
character_height = character.get_rect().size[1]
character_x_pos = ((screen_width - character_width)/2)
character_y_pos = (560 - character_height)
character_speed = 0.3
character_x_speed = 0
character_y_speed = 0
character_rect = character.get_rect()
#-----
#-----시간
tick = pygame.time.Clock()
start_time = pygame.time.get_ticks()
#-----
running = 1

while running :
    
    dt = tick.tick(100)
    for event in pygame.event.get() :
        #-----종료
        if event.type == pygame.QUIT :
            running = False
        #-----
        #-----이동키
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                character_x_speed += character_speed
            elif event.key == pygame.K_LEFT :
                character_x_speed -= character_speed
            elif event.key == pygame.K_SPACE :
                if character_y_pos >= (560 - character_height) :
                    character_y_speed = -0.7
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_RIGHT :
                character_x_speed -= character_speed
            elif event.key == pygame.K_LEFT :
                character_x_speed += character_speed
        #-----
    #-----이동
    #이동하기
    character_x_pos += character_x_speed*dt
    character_y_pos += character_y_speed*dt
    #좌우 이동 제한
    if character_x_pos > screen_width-character_width :
        character_x_pos = screen_width-character_width
    if character_x_pos < 0 :
        character_x_pos = 0
    #중력 가속도
    if character_y_pos < (560 - character_height) :
        character_y_speed += 0.02
    if character_y_pos > (560 - character_height) :
        character_y_pos = (560 - character_height)
        character_y_speed = 0
    #-----

    time_now = (pygame.time.get_ticks() - start_time)/1000 #시간경과
    #-----타이머
    timer = timer_font.render(str(int(time_now)),True,(0,0,0))
    #-----
    #-----똥 생성
    for ddcc in range(1,30,3) :
        if (int(time_now) == ddcc*3) and creat_bool :
            creat_bool = False
            ddong_pos.append(DDong(1+ddcc))
        if (int(time_now) == (ddcc+1)*3) and not(creat_bool) :
            creat_bool = True
            ddong_pos.append(DDong(2+ddcc))
    
    for ddc in ddong_pos :
        ddc.creat()
    #-----
    #-----똥 이동
    for dd in ddong_pos :
        dd.down()
    #-----
    #-----똥 제거
    for ddd in ddong_pos :
        ddd.delet()
    #-----
    #-----오브젝트 위치 할당
    #캐릭터
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    #-----
    #-----충돌처리
    for ddk in ddong_pos :
        for ddk1 in ddk.ddong_pos :
            enemy.left = ddk1[0]
            enemy.top = ddk1[1]

            if character_rect.colliderect(enemy) :
                screen.blit(gameover, (int((screen_width-gameover.get_rect().size[0])/2),int(screen_height-gameover.get_rect().size[1])/2))
                pygame.display.update()
                pygame.time.delay(3000)
                running = False
    #-----
    #-----화면 생성
    screen.blit(background, (0,0))#배경
    #똥
    for ddb in ddong_pos :
        for ddb1 in ddb.ddong_pos :
            screen.blit(ddong, (ddb1[0],ddb1[1]))

    screen.blit(timer, (10,10))#타이머
    screen.blit(character, (character_x_pos,character_y_pos))#캐릭터
    
    pygame.display.update()
    #-----
    
pygame.quit()
