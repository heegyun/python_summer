import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption('my game v1.0')

# 배경 이미지 불러오기
background = pygame.image.load('background.png')

running = True
while running:
    for event in pygame.event.get(): # 이벤트 감지
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0,0)) #배경 그리기

    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료 
pygame.quit()