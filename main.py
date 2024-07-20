import pygame

pygame.init()

screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

black=(0,0,0)
white=(255,255,255)

padel_width=10
padel_height=100
padel_1 = pygame.Rect(40, screen_height // 2 - padel_height // 2, padel_width, padel_height)
padel_2 = pygame.Rect(screen_width - 40, screen_height // 2 - padel_height // 2, padel_width, padel_height)

ball_radius = 15
ball_position = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
ball_speed=[5, 5]

font_size= 36
font=pygame.font.Font(None, font_size)
padel_1_score=0
padel_2_score=0

def draw_padel():
    pygame.draw.rect(screen, white, padel_1)
    pygame.draw.rect(screen, white, padel_2)

def move_padel():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w] and padel_1.top>0:
        padel_1.y -=10
    if keys[pygame.K_s] and padel_1.bottom<screen_height:
        padel_1.y +=10
    if keys[pygame.K_UP] and padel_2.top>0:
        padel_2.y -=10
    if keys[pygame.K_DOWN] and padel_2.bottom<screen_height:
        padel_2.y +=10

def draw_ball():
    pygame.draw.ellipse(screen, white, ball_position)

def move_ball():
    ball_position.x +=ball_speed[0]
    ball_position.y -=ball_speed[1]

    if ball_position.top <=0 or ball_position.bottom>=screen_height:
        ball_speed[1]=-ball_speed[1]
    if ball_position.colliderect(padel_1) or ball_position.colliderect(padel_2):
        ball_speed[0] =-ball_speed[0]
    if ball_position.left <=0 or ball_position.right>=screen_width:
        ball_speed[0]=-ball_speed[0]
def score():
    text=font.render(f"{padel_1_score} : {padel_2_score}", True, white)
    return text

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill(black)
    draw_padel()
    move_padel()
    draw_ball()
    move_ball()
    text=score()
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 10))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
