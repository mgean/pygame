# Example file showing a circle moving on screen
import pygame
import random
from rectangle import Rectangle
from circle import Circle


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.SysFont("Arial", 36)
text_content = ""


paddle_width = 40
paddle_height = 200
ball_radius = 30
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# paddle1_pos = pygame.Vector2(0, screen.get_height() / 2 - paddle_height / 2)
# paddle2_pos = pygame.Vector2(screen.get_width() - 40, screen.get_height() / 2 - paddle_height / 2)

paddle1 = Rectangle(0, screen.get_height() / 2, paddle_width, paddle_height, 1280, 720, 0)
paddle2 = Rectangle(screen.get_width() - 40, screen.get_height() / 2, paddle_width, paddle_height, 1280, 720, 0)
ball = Circle(ball_pos.x, ball_pos.y, ball_radius)

x_direction = "BALL_RIGHT"
y_direction = "BALL_UP"
# move_direction = random.choice(["BALL_UP", "BALL_DOWN", "BALL_LEFT", "BALL_RIGHT"])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "white", pygame.Vector2(ball.x, ball.y), ball.radius)
    pygame.draw.rect(screen, "white", pygame.Rect(paddle1.x, paddle1.y, paddle1.width, paddle1.height), width=0)
    pygame.draw.rect(screen, "white", pygame.Rect(paddle2.x, paddle2.y, paddle2.width, paddle2.height), width=0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        # move_direction = "UP"
        if paddle1.y > 0:
            paddle1.y -= 300 * dt
    if keys[pygame.K_s]:
        # move_direction = "DOWN"
        if paddle1.y < screen.get_height() - paddle1.height:
            paddle1.y += 300 * dt
    if keys[pygame.K_UP]:
        # move_direction = "UP"
        if paddle2.y > 0:
            paddle2.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        # move_direction = "DOWN"
        if paddle2.y < screen.get_height() - paddle2.height:
            paddle2.y += 300 * dt

    if y_direction == "BALL_UP":
        if ball.y > 0 + ball.radius:
            ball.y -= 300 * dt
        else:
            y_direction = "BALL_DOWN"
    if y_direction == "BALL_DOWN":
        if ball.y < screen.get_height() - ball.radius:
            ball.y += 300 * dt
        else:
            y_direction = "BALL_UP"
    if x_direction == "BALL_LEFT":
        if ball.x > 0 + ball.radius:
            ball.x -= 300 * dt
        else:
            x_direction = "BALL_RIGHT"
    if x_direction == "BALL_RIGHT":
        if ball.x < screen.get_width() - ball.radius:
            ball.x += 300 * dt
        else:
            x_direction = "BALL_LEFT"
            
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()