from turtle import Screen
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption('my game v1.0')


running = True
while running:
    for event in pygame.event.get(): # 이벤트 감지
        if event.type == pygame.QUIT:
            running = False

# pygame 종료 
pygame.quit()