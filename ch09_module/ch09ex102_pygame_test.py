import pygame

# pygame 모듈 초기화 - 초기화시 성공 실패 개수를 튜플로 반환합니다.
(successes, failurese) = pygame.init()
print(f'{successes} Succeses and {failurese} Failurese...')

# 스크린 만들기 - set_mode()에 튜플로  창의 크기 지정
screenSize = width, height = 400, 300
screen = pygame.display.set_mode(screenSize)

# 창의 타이틀 지정 - set_caption()으로 캡션 지정
pygame.display.set_caption('Hello PyGame')

# 게임 프레임 준비
clock = pygame.time.Clock()
# clock.tick(FPS)로 화면전환 속도 조절.
FPS = 60

# 튜플로 색상 변수를 만든다.
WHITE = 250,250,250
BLACK = 0,0,0


# Surface(빈 종이) 표면 만들기
# 이 표면을 조각 하기 위한 Rect 객체가 필요하다.
rect = pygame.Rect((0,0), (32,32))
surf = pygame.Surface((32,32))
surf.fill(WHITE)

# 게임 루프(중요하다)
# 이벤트를 전달 받는다.
# type이 QUIT이면 while 반복문 탈출
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-2,0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(2,0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0,-2)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0,2)

    screen.fill(BLACK)
    screen.blit(surf, rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()