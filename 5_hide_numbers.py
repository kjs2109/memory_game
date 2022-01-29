import pygame
from random import *

# 레벨에 맞게 설정


def setup(level):
    # 레벨에 따라 숫자가 보여지는 시간
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)

    # 게임 레벨에 따른 문제 개수
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    # 실제 화면에 grid 형태로 숫자를 랜덤 배치
    shuffle_grid(number_count)


def shuffle_grid(number_count):
    columns = 9
    rows = 5

    cell_size = 130  # 각 Grid cell 별로 가로, 세로 크기
    button_size = 110  # Grid clee 내에 실제로 그려질 버튼 크기
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for column in range(columns)] for row in range(rows)]

    number = 1
    while number <= number_count:
        col_idx = randrange(columns)
        row_idx = randrange(rows)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + col_idx*cell_size + cell_size/2
            center_y = screen_top_margin + row_idx*cell_size + cell_size/2

            # 숫자 버튼 만들기
            # 버튼 객체 생성 -> collidepoint 사용 가능
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)  # 조심

            number_buttons.append(button)
    print(grid)

    # 시작 화면 보여주기


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 게임 화면 보여주기


def display_game_screen():
    global display_time, hidden

    if not hidden:
        elapsed_time = (pygame.time.get_ticks() -
                        start_ticks) / 1000  # ms -> sec
        if elapsed_time >= display_time:
            hidden = True

    for index, rect in enumerate(number_buttons, start=1):

        if hidden:  # 숫자가 보이지 않음
            pygame.draw.rect(screen, GRAY, rect)
        else:
            # 실제 숫자 보여주기
            cell_text = game_font.render(str(index), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)


def check_buttons(pos):  # 버튼 클릭 이벤트 발생시 실행된다. 크게 게임 진핸중과 시작전의 상황으로 나눠서 처리한다.
    global start, start_ticks
    if start:  # 게임이 시작 했으면
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()


def check_number_buttons(pos):
    global hidden

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print('correct')
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print('worng')
            break


pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memory Game')

# 게임 폰트
game_font = pygame.font.Font(None, 120)  # 폰트 정의

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
GRAY = (50, 50, 50)

number_buttons = []  # 플레이어가 눌러야 하는 버튼들

display_time = None  # 숫자를 보여주는 시간
start_ticks = None  # 시간 계산, 현재의 시간정보를 저장

# 게임 시작 여부
start = False

# hidden이 False일 경우 숫자가 보이다.
hidden = False

# 게임 시작 전에 게임 설정 함수 수행
setup(1)

running = True
while running:
    click_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    if start:
        display_game_screen()  # 게임 화면 표시
    else:
        display_start_screen()  # 시작 화면 표시

    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()

pygame.quit()
