# khai bao thu vien
import copy
from board import bang
import pygame
import math
import time
import random
import os
pygame.init() #khởi tạo chương trình
pygame.mixer.init()
# man hinh
WIDTH = 900
HEIGHT = 950
pygame.display.set_caption('EROPAC')
bg = pygame.transform.scale(pygame.image.load(f'assets/backgrounds/bien.jpg'),(WIDTH, HEIGHT)) #chỉnh sửa kích thước ảnh
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60 #tốc độ khung hình trên giây
font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(bang) # thay đổi đối tượng sao chép không thay đổi đối tượng ban đầu
color = 'blue'
PI = math.pi
# add ảnh nhân vật
player1= pygame.transform.scale(pygame.image.load(f'assets/robot/HỮU CƠ.png'), (60, 60))
player2=pygame.transform.scale(pygame.image.load(f'assets/robot/TÁI CHẾ.png'), (60, 60))
player3=pygame.transform.scale(pygame.image.load(f'assets/robot/VÔ CƠ.png'), (60, 60))
player =player1
player_x = 450 # set up vị trí ban đầu của nv
player_y = 663
direction = 0 # hướng ban đầu
# R, L, U, D
turns_allowed = [False, False, False, False]
direction_command = 0
player_speed = 2
score = 0
moving = True
startup_counter = 0
game_over = False
game_won = False
start_ticks= False
#add âm thanh
sound_play=pygame.mixer.Sound('assets/Music/nhacnen.mp3')
sound_play.set_volume(0.2)
sound_end = pygame.mixer.Sound('assets/Music/thua.mp3')
sound_end.set_volume(0.1)
sound_win = pygame.mixer.Sound('assets/Music/win.mp3')
sound_win.set_volume(0.1)
sound_count=pygame.mixer.Sound('assets/Music/demnguoc.mp3')
sound_count.set_volume(0.2)
def draw_misc():
    score_text = font.render(f'Score: {score}', True, 'white') #in điểm số lên màn hình
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2-40))
    if game_over:
        sound_play.stop()
        sound_count.stop()
        pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('CHICKEN! Space bar to restart!', True, 'red')
        screen.blit(gameover_text, (100, 300))
        sound_end.play()
       
    if game_won:
        sound_play.stop()
        sound_count.stop()
        pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(screen, 'firebrick', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('Maginificent, outstanding, wonderful! Space bar to restart!', True, 'green')
        screen.blit(gameover_text, (100, 300))
        sound_win.play()


def check_collisions(scor): # tính điểm, ăn
    num1 = (HEIGHT - 50) // 32
    num2 = (WIDTH // 30)
    if 0 < player_x < 870:
        if level[center_y // num1][center_x // num2] == 1: # ăn chấm nhỏ
            level[center_y // num1][center_x // num2] = 0 # mất
            scor += 10
        if player==player3:
            if level[center_y // num1][center_x // num2] == 2: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
            if level[center_y // num1][center_x // num2] == 9: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
        if player==player2: 
            if level[center_y // num1][center_x // num2] == 10: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
            if level[center_y // num1][center_x // num2] == 11: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
            if level[center_y // num1][center_x // num2] == 12: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
            if level[center_y // num1][center_x // num2] == 13: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
        if player==player1:
            if level[center_y // num1][center_x // num2] == 14: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
            if level[center_y // num1][center_x // num2] == 15: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
            if level[center_y // num1][center_x // num2] == 16: # ăn chấm to
                level[center_y // num1][center_x // num2] = 0
                scor += 20
    return scor
file1 =[f for f in os.listdir('assets/rac/RÁC VÔ CƠ')]
file2 =[f for f in os.listdir('assets/rac/RÁC TÁI CHẾ')]
file3 =[f for f in os.listdir('assets/rac/RÁC HỮU CƠ')]
image1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC VÔ CƠ', random.choice(file1))),(40,40))
image2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC VÔ CƠ', random.choice(file1))),(40,40))
image3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC TÁI CHẾ', random.choice(file2))),(40,40))
image4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC TÁI CHẾ', random.choice(file2))),(40,40))
image5 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC TÁI CHẾ', random.choice(file2))),(40,40))
image6 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC TÁI CHẾ', random.choice(file2))),(40,40))
image7 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC HỮU CƠ', random.choice(file3))),(40,40))
image8 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC HỮU CƠ', random.choice(file3))),(40,40))
image9 = pygame.transform.scale(pygame.image.load(os.path.join('assets/rac/RÁC HỮU CƠ', random.choice(file3))),(40,40))
# hàm tạo bản đồ
def draw_board():
    num1 =((HEIGHT- 50)//32)
    num2 =(WIDTH //30)
    for i in range (len(level)):
        for j in range (len(level[i])):
            if level[i][j]==1:
                pygame.draw.circle(screen, 'white',(j*num2 +(0.5*num2), i* num1+(0.5*num1)), 4)
            # add rác dô nè
            if level[i][j]==2:
                screen.blit(image1,(j*num2 +(0.5*num2)-15, i* num1+(0.5*num1) -15))
            if level[i][j]==9:
                screen.blit(image2,(j*num2 +(0.5*num2) -15, i* num1+(0.5*num1)))
            if level[i][j]==10:
                screen.blit(image3,(j*num2 +(0.5*num2)-15, i* num1+(0.5*num1) -15))
            if level[i][j]==11:
                screen.blit(image4,(j*num2 +(0.5*num2) -10, i* num1+(0.5*num1)-15))
            if level[i][j]==12:
                screen.blit(image5,(j*num2 +(0.5*num2) +20, i* num1+(0.5*num1)-10))
            if level[i][j]==13:
                screen.blit(image6,(j*num2 +(0.5*num2) -10, i* num1+(0.5*num1)-20))
            if level[i][j]==14:
                screen.blit(image7,(j*num2 +(0.5*num2)-10, i* num1+(0.5*num1)-20))
            if level[i][j]==15:
                screen.blit(image8,(j*num2 +(0.5*num2)-15, i* num1+(0.5*num1)))
            if level[i][j]==16:
                screen.blit(image9,(j*num2 +(0.5*num2)-10, i* num1+(0.5*num1)-20))
            if level[i][j]==3:
                pygame.draw.line(screen, color,(j*num2 +(0.5*num2), i* num1),(j*num2 +(0.5*num2), i* num1 + num1),3)
            if level[i][j]==4:
                pygame.draw.line(screen, color,(j*num2, i* num1 +(0.5*num1)),(j*num2 + num2, i* num1 +(0.5*num1)),3)
            if level[i][j]==5:
                pygame.draw.arc(screen, color, [(j*num2 -(num2*0.4)) -2, (i* num1+ (0.5*num1)), num2, num1], 0, PI/2, 3)
            if level[i][j]==6:
                pygame.draw.arc(screen, color,[(j* num2 +(num2*0.5)), (i* num1 +(0.5 *num1)), num2, num1], PI/2, PI, 3)
            if level[i][j]==7:
                pygame.draw.arc(screen, color, [(j*num2+ (num2*0.5)), (i* num1 -(0.4*num1)), num2, num1], PI, 3*PI/2,3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j* num2- (num2 *0.4))- 2, (i* num1 -(0.4 *num1)), num2, num1], 3*PI/2, 2*PI, 3)
            if level[i][j] == 9:
                pygame.draw.line (screen, 'white', (j *num2, 1*num1+ (0.5*num1)), (j *num2 +num2, 1*num1 +(0.5*num1)), 3)

def draw_player():
      # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
      # kiểm tra hướng của nv và chuyển hướng
    for direction in range (0,4):
        screen.blit(player,(player_x, player_y))


def check_position(centerx, centery): # kiểm tra vị trí và di chuyển
    # 0-Right, 1-Left, 2- Up, 3- Down
    turns = [False, False, False, False]
    num1 = (HEIGHT - 50) // 32 # chiều cao của mỗi ô
    num2 = (WIDTH // 30) # chiều rộng của mỗi ô
    num3 = 15 # độ lệch nhỏ để kiểm tra vị trí chính xác hơn
    p= [2, 9, 10, 11, 12, 13, 14, 15, 16]
    if centerx //30 < 29: #đảm bảo không ra khỏi bản đ
        if direction == 0:      
            if level[centery// num1] [(centerx - num3)// num2] < 3 or level[centery// num1] [(centerx - num3)// num2] in p :
                turns[1] = True
        if direction == 1:
            if level [centery//num1] [(centerx -num3)// num2] < 3 or level[centery// num1] [(centerx - num3)// num2] in p:
                turns[0] = True
        if direction == 2:
            if level [(centery+ num3)// num1] [centerx// num2] < 3 or level [(centery+ num3)// num1] [centerx// num2] in p:  
                turns[3] = True
        if direction == 3:
            if level [(centery- num3)// num1] [centerx // num2] < 3 or level [(centery - num3)// num1] [centerx// num2] in p:
                turns [2] = True
        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3) // num1][centerx // num2] < 3 or level [(centery+ num3)// num1] [centerx// num2] in p:
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 3 or level [(centery- num3)// num1] [centerx// num2] in p:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num2) // num2] < 3 or level[centery // num1][(centerx - num2) // num2] in p:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 3 or level[centery // num1][(centerx + num2) // num2] in p:
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num1) // num1][centerx // num2] < 3 or level[(centery + num1) // num1][centerx // num2] in p:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 3 or level[(centery - num1) // num1][centerx // num2] in p:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num3) // num2] < 3 or level[centery// num1] [(centerx - num3)// num2] in p:
                    turns[1] = True
                if level[centery // num1][(centerx + num3) // num2] < 3 or level[centery// num1] [(centerx + num3)// num2] in p:
                    turns[0] = True
    else:
        turns[0]= True
        turns[1]= True
    return turns
def move_player(play_x, play_y):
    # r, l, u, d
    if direction == 0 and turns_allowed[0]:
        play_x += player_speed
    elif direction == 1 and turns_allowed[1]:
        play_x -= player_speed
    if direction == 2 and turns_allowed[2]:
        play_y -= player_speed
    elif direction == 3 and turns_allowed[3]:
        play_y += player_speed
    return play_x, play_y


run = True
while run:
    sound_play.play(-1)
    timer.tick(fps) # giới hạn số khung hình mỗi giây
    screen.blit(bg,(0,0))
    if startup_counter < 180 and not game_over and not game_won: # chờ 3s mới move
        moving = False
        startup_counter += 1
    else:
        moving = True
    
    if moving: # thiết lập đếm ngược
        if start_ticks == False:
            start_ticks = pygame.time.get_ticks() # bắt đầu tính thời gian
        countdown_time= 60
        seconds_left = countdown_time - (pygame.time.get_ticks() - start_ticks) // 1000 # chuyển mil giây sang giây
        if seconds_left ==10:
            sound_play.stop()
            sound_count.play(1)
        if seconds_left <= 0:
            seconds_left =0
            if seconds_left == 0:
                moving=False
                game_over=True
        text = font.render(f'Time:{seconds_left}', True, 'red')
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2)) # căn ở chính giữa
    draw_board()
    center_x = player_x + 22
    center_y = player_y + 22

    draw_misc()
    game_won = True
    for i in range(len(level)):
        for j in level[i]:
            if j in [ 2, 9, 10, 11, 12, 13, 14, 15, 16]:
                game_won = False
                break
            else:
                game_won=True
        if not game_won:
            break
            
    draw_player()
    turns_allowed = check_position(center_x, center_y)
    if moving:
        player_x, player_y = move_player(player_x, player_y)
    score = check_collisions(score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
        if event.type == pygame.KEYDOWN:                        
            if event.key == pygame.K_RIGHT:# set up nút bấm tương ứng với hướng đi
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
            if event.key == pygame.K_a:# chuyển đổi nhân vật
                player= player1
            if event.key == pygame.K_s:
                player= player2
            if event.key == pygame.K_d:
                player= player3
            if event.key == pygame.K_SPACE and ( game_over or game_won): # set up lại từ đầu
                start_ticks = pygame.time.get_ticks() + startup_counter//60*1000
                seconds_left = countdown_time - (pygame.time.get_ticks()-start_ticks) // 1000
                game_over = False
                game_won = False
                startup_counter = 0
                player_x = 450
                player_y = 663
                direction = 0
                direction_command = 0
                score = 0
                level = copy.deepcopy(bang)
                sound_end.stop()
                sound_win.stop()
                sound_play.play(-1)
                player =player1
           
        if event.type == pygame.KEYUP: # bỏ giữ phím mà vẫn giữ nguyên hướng đang di chuyển
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction
       
    for i in range (4):
        if direction_command == i and turns_allowed[i]:
            direction = i
    if player_x > 900: # khi nv qua khỏi lề bên phải thì nó xuất hiện bên trái
        player_x = -47
    elif player_x < -50: # ngược lại
        player_x = 897
    pygame.display.flip()  # cập nhật toàn bộ màn hình
pygame.quit()
