import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('my game v1.0')



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

running = True
while running:
    for event in pygame.event.get(): # 이벤트 감지
        if event.type == pygame.QUIT:
            running = False
    
         # 4. 키보드 이벤트 처리 하기
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인 후
            if event.key == pygame.K_LEFT : # 캐릭터를 왼쪽으로 좌표이동
                to_x -=5 # 4.2
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 좌표이동
                to_x +=5 # 4.2
            elif event.key == pygame.K_UP: # 캐릭터를 위로 좌표이동
                to_y -=5 # 4.2
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로 좌표이동
                to_y +=5 # 4.2

        if event.type == pygame.KEYUP: # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                to_y = 0
    
    # 4.3  이동좌표를 캐릭터에 적용하기
    character_x_pos += to_x
    character_y_pos += to_y

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

    screen.blit(background, (0,0)) # 배경 그리기
    
    # 3.2 캐릭터 그리기
    screen.blit(character,(character_x_pos, character_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료 
pygame.quit()