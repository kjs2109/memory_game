import pygame


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


def displat_game_screen():
    pass


pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memory Game')

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

# 게임 시작 여부
start = False

running = True
while running:
    # mouse_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)
    if start:
        display_game_screen()
    else:
        display_start_screen()  # 시작 화면 표시

    # 화면 업데이트
    pygame.display.update()

pygame.quit()
