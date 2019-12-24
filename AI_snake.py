import pygame
import random
import A_algo_duplicate
pygame.init()

pygame.mixer.init()
# creating window

screen_width = 900
screen_height = 960
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake game")
carImg = pygame.image.load('apple.png')
overImg = pygame.image.load('tenor.gif')
welcm = pygame.image.load('welcome_page.png')
green = (1, 50, 32)


# Game specific variables
start_on = True


def start_game():
    pygame.mixer.music.load('media.io_background.wav')
    pygame.mixer.music.play(20)
    exit_game = False
    game_over = False
    snake_x = 5
    snake_y = 5
    snake_width = 20
    FPS = 20
    snake_mv = 'r'
    food_pos = (random.randint(1, 43), random.randint(1, 43))
    head = [[4, 5], [snake_x, snake_y]]
    snake_len = 1
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Snake Chan", 29)
    font2 = pygame.font.SysFont("Snake Chan", 45)
    return exit_game, game_over, snake_x, snake_y, snake_width, FPS, snake_mv, food_pos, head, snake_len, clock, font, font2

exit_game, game_over, snake_x, snake_y, snake_width, FPS, snake_mv, food_pos, head, snake_len, clock, font, font2 = start_game()
def plot_snake(gameWindow, head, snake_width):
    for i in head:
        pygame.draw.rect(gameWindow, green, [i[0] * 20, i[1] * 20, snake_width, snake_width])
    # pygame.draw.circle(gameWindow, green, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2], snake_width//2 + 1)
    # if snake_len//3 < snake_width//2:
    #     for i in range(0, len(head)//3):
    #         pygame.draw.circle(gameWindow, green, [head[i][0] + snake_width//2, head[i][1] + snake_width//2], snake_width//2 + i - snake_len//3)
    #     for i in head[len(head)//3:-1]:
    #         pygame.draw.circle(gameWindow, green, [i[0] + snake_width//2, i[1] + snake_width//2], snake_width//2)
    # else:
    #     for i in range(0, snake_width//2):
    #         pygame.draw.circle(gameWindow, green, [head[i][0] + snake_width//2, head[i][1] + snake_width//2], snake_width//2 - snake_width//2 + i)
    #     for i in head[snake_width//2:-1]:
    #         pygame.draw.circle(gameWindow, green, [i[0] + snake_width//2, i[1] + snake_width//2], snake_width//2)
    if head[-1][0] == head[-2][0]:
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] * 20 + snake_width//2 + 4, head[-1][1] * 20 + snake_width//2], 4)
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] * 20 + snake_width//2 - 4, head[-1][1] * 20 + snake_width//2], 4)
    else:
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] * 20 + snake_width//2, head[-1][1] * 20 + snake_width//2 - 4], 4)
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] * 20 + snake_width//2, head[-1][1] * 20 + snake_width//2 + 4], 4)

def put_text(text, color, x, y, font):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])

with open("high_score.txt", "r") as f:
    high_score = int(f.read())
sound1 = pygame.mixer.Sound('bite.wav')
while not exit_game:
    while start_on:
        gameWindow.blit(welcm, (20, 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_on = False


    command, end_game = A_algo_duplicate.main_func(head, food_pos)
    for i in command[::-1]:
        snake_x = i[0]
        snake_y = i[1]
        if snake_x == food_pos[0] and snake_y == food_pos[1]:
            snake_len += 1
            # print(head)
            # print("eaten", food_pos)
            sound1.play()
            head.append([snake_x, snake_y])
            food_pos = (random.randint(1, 43), random.randint(1, 43))
            while food_pos in head:
                food_pos = (random.randint(1, 43), random.randint(1, 43))
            # print("next", food_pos)
            continue
        else:
            # if len(head) > snake_len:
            head.append([snake_x, snake_y])
            del head[0]
        gameWindow.fill((255, 255, 255))
        if (snake_len - 1) * 5 > high_score:
            high_score = (snake_len - 1) * 5
        if head[-1][0] >= 45 or head[-1][0] <= 0 or head[-1][1] >= 45 or head[-1][1] <= 0 or (head[-1] in head[:-1] and len(head) != 1) or end_game == True:
            # print(head)
            # x = input()
            print(food_pos)
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
            game_over = True
            while game_over == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            exit_game, game_over, snake_x, snake_y, snake_width, FPS, snake_mv, food_pos, head, snake_len, clock, font, font2 = start_game()
                            gameWindow.fill((255, 255, 255))
                            put_text('score : ' + str((snake_len - 1) * 5), green, 10, 910, font)
                            put_text('highest score : ' + str(high_score), green, 450, 910, font)
                            pygame.draw.line(gameWindow, (0, 0, 0), (0, 900), (900, 900), 5)
                            gameWindow.blit(carImg, (food_pos[0]*20, food_pos[1] * 20))
                            plot_snake(gameWindow, head, snake_width)
                            pygame.display.update()
                            clock.tick(FPS)
                            game_over = False
                            continue
                        else:
                            pygame.quit()
                            exit()
                pygame.display.update()
                clock.tick(FPS)
                gameWindow.blit(overImg, (340, 180))
                put_text('Game over', green, 300, 400, font2)
                put_text('press ENTER to restart or any other key', green, 20, 500, font)
            # break
        put_text('score : ' + str((snake_len - 1) * 5), green, 10, 910, font)
        put_text('highest score : ' + str(high_score), green, 450, 910, font)
        with open("high_score.txt", "w") as f:
            f.write(str(high_score))
        pygame.draw.line(gameWindow, (0, 0, 0), (0, 900), (900, 900), 5)
        gameWindow.blit(carImg, (food_pos[0]*20, food_pos[1] * 20))
        plot_snake(gameWindow, head, snake_width)
        pygame.display.update()
        clock.tick(FPS)
pygame.quit()
exit()
