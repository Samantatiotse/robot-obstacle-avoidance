import math
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

robot_x = 250
robot_y = 250

robot_angle = 45
robot_speed = 2
angle_radians = math.radians(robot_angle)
vx= robot_speed * math.cos(angle_radians)
vy= robot_speed * math.sin(angle_radians)

obstacles1 = pygame.Rect(200, 150, 100, 70)
obstacles2 = pygame.Rect(400, 150, 40, 30)
obstacles3 = pygame.Rect(600, 400, 100, 120)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if robot_x > 800-15 or robot_x < 0:
            vx = -vx
    if robot_y > 600-15 or robot_y < 0:
            vy = -vy

    screen.fill((255, 255, 255))


    robot_x += vx
    robot_rect = pygame.Rect(robot_x - 15, robot_y - 15, 30, 30)
    for obstacle in [obstacles1, obstacles2, obstacles3]:
        if robot_rect.colliderect(obstacle):
           robot_x -= vx   
           vx = -vx       
           break

    robot_y += vy
    robot_rect = pygame.Rect(robot_x - 15, robot_y - 15, 30, 30)
    for obstacle in [obstacles1, obstacles2, obstacles3]:
        if robot_rect.colliderect(obstacle):
          robot_y -= vy
          vy = -vy
          break
    
    for obstacle in [obstacles1, obstacles2, obstacles3]:
        pygame.draw.rect(screen, (78, 64, 80), obstacle)
    
    pygame.draw.circle(screen, (80, 200, 255), (int(robot_x), int(robot_y)), 15)
    
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()