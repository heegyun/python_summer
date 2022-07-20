import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption('my game v1.0')

# 2. 배경 이미지 불러오기
background = pygame.image.load('background.png')

# 3. 캐릭터(스프라이트) 불러오기
character = pygame.image.load('charater.png')

# 3.1 캐릭터는 움직임도 있어야 하므로 몇가지 배경과 다른  속성들이 필요함
character_size = character.get_rect().size # 이미지 크기 구함
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_width   # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

running = True
while running:
    for event in pygame.event.get(): # 이벤트 감지
        if event.type == pygame.QUIT:
            running = False
    

    screen.blit(background, (0,0)) # 배경 그리기

    # 3.2 캐릭터 그리기
    screen.blit(character,(character_x_pos, character_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료 
pygame.quit()