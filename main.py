import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

padel_width = 10
padel_height = 100
padel_1 = pygame.Rect(40, screen_height // 2 - padel_height // 2, padel_width, padel_height)
padel_2 = pygame.Rect(screen_width - 40 - padel_width, screen_height // 2 - padel_height // 2, padel_width, padel_height)

ball_radius = 15
ball_position = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
ball_speed = [5, 5]

font_size = 36
font = pygame.font.Font(None, font_size)
padel_1_score = 0
padel_2_score = 0

def draw_padel():
    pygame.draw.rect(screen, white, padel_1)
    pygame.draw.rect(screen, white, padel_2)

def move_padel():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and padel_1.top > 0:
        padel_1.y -= 10
    if keys[pygame.K_s] and padel_1.bottom < screen_height:
        padel_1.y += 10
    if keys[pygame.K_UP] and padel_2.top > 0:
        padel_2.y -= 10
    if keys[pygame.K_DOWN] and padel_2.bottom < screen_height:
        padel_2.y += 10

def draw_ball():
    pygame.draw.ellipse(screen, white, ball_position)

def move_ball():
    global ball_position, ball_speed, padel_1_score, padel_2_score

    ball_position.x += ball_speed[0]
    ball_position.y += ball_speed[1]

    if ball_position.top <= 0 or ball_position.bottom >= screen_height:
        ball_speed[1] = -ball_speed[1]
    if ball_position.colliderect(padel_1) or ball_position.colliderect(padel_2):
        ball_speed[0] = -ball_speed[0]

    if ball_position.left <= 0:
        padel_2_score += 1
        if padel_2_score >= 5:
            end_game()
        else:
            reset_ball()
    elif ball_position.right >= screen_width:
        padel_1_score += 1
        if padel_1_score >= 5:
            end_game()
        else:
            reset_ball()

def reset_ball():
    global ball_position, ball_speed
    ball_position = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
    ball_speed = [5, 5]

def draw_scores():
    text = font.render(f"{padel_1_score} : {padel_2_score}", True, white)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 10))

def end_game():
    screen.fill(black)
    text = font.render("GAME OVER!", True, red)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    reset_game()

def reset_game():
    global padel_1_score, padel_2_score, padel_1, padel_2, ball_position, ball_speed
    padel_1_score = 0
    padel_2_score = 0
    padel_1 = pygame.Rect(40, screen_height // 2 - padel_height // 2, padel_width, padel_height)
    padel_2 = pygame.Rect(screen_width - 40 - padel_width, screen_height // 2 - padel_height // 2, padel_width, padel_height)
    ball_position = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
    ball_speed = [5, 5]

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        move_padel()
        move_ball()
        screen.fill(black)
        draw_padel()
        draw_ball()
        draw_scores()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

        if padel_1_score >= 5 or padel_2_score >= 5:
            end_game()
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r] and game_over:
        reset_game()
        game_over = False
    elif keys[pygame.K_q]:
        running = False

pygame.quit()
