import pygame as game

def GAMEOVER() :
    screen.blit(gameover, ((screen_width-gameover_width)/2,(screen_height-gameover_height)/2))
    game.display.update()
    game.time.delay(2000)

game.init()

screen_width = 480
screen_height = 640

move = 0.2

screen = game.display.set_mode((screen_width,screen_height))

game.display.set_caption("Nado Game")


backGround = game.image.load("C:/Users/U107-10/Pictures/background.png")

#----- 캐릭터
character = game.image.load("C:/Users/U107-10/Pictures/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height
character_rect = character.get_rect()
to_x = 0
to_y = 0
#-----

#----- 장애물
enemy = game.image.load("C:/Users/U107-10/Pictures/grass.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = screen_height/2 - enemy_height/2
enemy_rect = enemy.get_rect()
#-----
#-----폰트 정의
    #타이머
game_timer_font = game.font.Font(None, 40)
    #게임오버
game_over_font = game.font.Font(None, 100)
gameover = game_over_font.render("GAME OVER",True,(0,0,0))
gameover_size = gameover.get_rect().size
gameover_width = gameover_size[0]
gameover_height = gameover_size[1]
#-----

#-----게임 시간
total_time = 10
start_ticks = game.time.get_ticks()
#-----
clock = game.time.Clock()


running = True

while running :

    dt = clock.tick(100)
    #-----버튼 command
    for event in game.event.get() :
        if event.type == game.QUIT :
            running = False

        if event.type == game.KEYDOWN :
            if event.key == game.K_LEFT :
                to_x -= move
            elif event.key == game.K_RIGHT :
                to_x += move
            elif event.key == game.K_UP :
                to_y -= move
            elif event.key == game.K_DOWN :
                to_y += move
            else :
                pass
            
        if event.type == game.KEYUP :
            if event.key == game.K_LEFT :
                to_x += move
            elif event.key == game.K_RIGHT :
                to_x -= move
            elif event.key == game.K_UP :
                to_y += move
            elif event.key == game.K_DOWN :
                to_y -= move
    #-----
    #-----타이머
    elapsed_time = (game.time.get_ticks() - start_ticks)/1000
    timer = game_timer_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    if (total_time-elapsed_time) < 0 :
        GAMEOVER()
        break
    #-----
    #-----좌표 이동
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt

    if character_x_pos < 0 :
        character_x_pos = 0
    if character_x_pos > (screen_width - character_width) :
        character_x_pos = (screen_width - character_width)
    if character_y_pos < 0 :
        character_y_pos = 0
    if character_y_pos > (screen_height - character_height) :
        character_y_pos = (screen_height - character_height)
    #-----
    #-----화면 그리기
    screen.blit(backGround, (0,0))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(timer, (10,10))
    
    game.display.update()
    #-----
    #-----충돌 처리
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect) :
        GAMEOVER()
        break
    #-----


game.quit()
