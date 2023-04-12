import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Catching Game")

background_color = (255, 255, 255)
font_color = (0, 0, 0)
font_size = 32
fruit_types = ["apple", "banana", "orange"]
fruit_images = {fruit: pygame.image.load(f"{fruit}.png") for fruit in fruit_types}
fruit_speed = 5

player_image = pygame.image.load("player.png").convert_alpha()
player_rect = player_image.get_rect(midbottom=(WIDTH//2, HEIGHT - 20))
player_speed = 7

fruit_size = (50, 50)
fruits = []

score = 0
score_font = pygame.font.Font(None, font_size)

clock = pygame.time.Clock()

def get_fruit():
    fruit_type = random.choice(fruit_types)
    fruit_image = fruit_images.get(fruit_type)
    fruit_x = random.randint(0, WIDTH - fruit_size[0])
    fruit_y = 0 - fruit_size[1]
    fruit_rect = fruit_image.get_rect(topleft=(fruit_x, fruit_y))
    fruit_speed = random.randint(3, 7)
    fruit_data = {"rect": fruit_rect, "image": fruit_image, "speed": fruit_speed, "type": fruit_type}
    fruits.append(fruit_data)

def update_fruits():
    for fruit in fruits:
        fruit["rect"].move_ip(0, fruit["speed"])
        if fruit["rect"].top > HEIGHT:
            fruits.remove(fruit)

def draw_fruits():
    for fruit in fruits:
        screen.blit(fruit["image"], fruit["rect"])

def detect_collisions():
    global score
    for fruit in fruits:
        if fruit["rect"].colliderect(player_rect):
            fruits.remove(fruit)
            score += 1

def display_score():
    score_text = score_font.render(f"Score: {score}", True, font_color)
    screen.blit(score_text, (10, 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.move_ip(player_speed, 0)

    if random.randint(0, 30) == 0:
        get_fruit()

    update_fruits()

    detect_collisions()

    screen.fill(background_color)

    draw_fruits()

    screen.blit(player_image, player_rect)

    display_score()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
