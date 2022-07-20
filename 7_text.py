import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('my game v1.0')

# 5. 초당 프레임 수 (초당 프레임수가 높으면 좀 부드럽고, 낮으면 좀 거칠게(끊기는것)표현됨)
clock = pygame.time.Clock()


# 2. 배경 이미지 불러오기
background = pygame.image.load('background.png')

# 3. 캐릭터(스프라이트) 불러오기
character = pygame.image.load('charater.png')

# 3.1 캐릭터는 움직임도 있어야 하므로 몇가지 배경과 다른  속성들이 필요함
character_size = character.get_rect().size # 이미지 크기 구함
character_width = character_size[0]
character_height = character_size[1]

 # 위치는 화면 아래쪽 정 가운데에서 캐릭터가 위치하게 함
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 - 캐릭터 그림 가로의 절반사이즈
character_y_pos = screen_height - character_width   # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 - 캐릭터의 가로길이

# 4.1 이동할 좌표
to_x = 0
to_y = 0

# 5.3 이동 속도 
character_speed = 0.6

# 6. 적 enemy 캐릭터
enemy = pygame.image.load('enemy.png')

# 6.1 
enemy_size = enemy.get_rect().size # 이미지 크기 구함
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

# 6.2 정가운데 위치
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 - 캐릭터 그림 가로의 절반사이즈
enemy_y_pos = (screen_height/2)  -  (enemy_width / 2)  # 화면 세로의 절반 크기에 해당하는 곳에 위치 - 캐릭터 그림 가로의 절반사이즈

# 7. 폰트 정의
game_font = pygame.font.Font(None, 40)

# 7.1 총 시간 10초
total_time = 10

# 7.2 시작 시간
stat_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True
while running:
    # 5.1 fps 
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

# 5.2 예를 들어 캐릭터가 100만큼 이동을 해야함 (fps가 바뀌었다고 해서 속도가 달라지면 안된다. 이것 처리 하는 방법)
# 10fps: 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동할까? 10만큼 : 10 * 10 = 100
# 20fps: 1초 동안에 20번 동작 -> 1번에 몇 만큼 이동할까? 5만큼 : 5 * 20 = 100

    for event in pygame.event.get(): # 이벤트 감지
        if event.type == pygame.QUIT:
            running = False
    
         # 4. 키보드 이벤트 처리 하기
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인 후
            if event.key == pygame.K_LEFT : # 캐릭터를 왼쪽으로 좌표이동
                to_x -=character_speed #  5.3 이동 속도
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 좌표이동
                to_x +=character_speed # 5.3 이동 속도
            elif event.key == pygame.K_UP: # 캐릭터를 위로 좌표이동
                to_y -=character_speed # 5.3 이동 속도
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로 좌표이동
                to_y +=character_speed # 5.3 이동 속도

        if event.type == pygame.KEYUP: # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                to_y = 0
    
    # 5.4  속도 고정 시키기
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 4.4 캐릭터가 화면 내에 있도록 위치 조정하기
    # 가로 경계값 위치 값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 위치 값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 6.5 적과 충돌 처리 (충돌시 게임 종료)
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('충돌 했습니다!!')
        running = False


    screen.blit(background, (0,0)) # 배경 그리기
    
    # 3.2 캐릭터 그리기
    screen.blit(character,(character_x_pos, character_y_pos))

     # 6.3 적 그리기
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))


    # 7.3 타이머 작동
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - stat_ticks ) / 1000
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer, (10,10))

    # 시간이 0이하면 게임 종료
    if total_time-elapsed_time <= 0:
        print('타임 아웃')
        running = False


    pygame.display.update() # 게임 화면을 다시 그리기



# 잠시 대기
pygame.time.delay(2000)

# pygame 종료 
pygame.quit()