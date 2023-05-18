import pygame
import random

pygame.init()

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Các cài đặt màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Piano Game')

# Khởi tạo đồng hồ
clock = pygame.time.Clock()

# Khởi tạo font chữ
font = pygame.font.Font(None, 36)

# Danh sách các phím
keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Danh sách các bài hát
songs = [['C', 'D', 'E', 'C', 'E', 'F', 'G', 'C', 'D', 'E', 'C', 'E', 'F', 'G'],
         ['G', 'F', 'E', 'D', 'C', 'D', 'E', 'F', 'G', 'G', 'F', 'E', 'D', 'C'],
         ['C', 'C', 'G', 'G', 'A', 'A', 'G', 'F', 'F', 'E', 'E', 'D', 'D', 'C']]

# Chế độ chọn bài hát
song_index = 0

# Biến điểm số
score = 0

# Biến đếm số lần nhấn sai hoặc bỏ qua
misses = 0

# Hàm kiểm tra xem phím có đúng với phím trong bài hát không
def check_key(key):
    global misses, song_index, score
    if key == songs[song_index][0]:
        songs[song_index].pop(0)
        score += 10
        if len(songs[song_index]) == 0:
            song_index = (song_index + 1) % len(songs)
    else:
        misses += 1
        if misses >= 3:
            game_over()

# Hàm kết thúc trò chơi
def game_over():
    global score
    screen.fill(WHITE)
    text = font.render('Game over! Score: ' + str(score), True, BLACK)
    screen.blit(text, [screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2])
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    quit()

# Vòng lặp chính
done = False
while not done:
    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_a:
                check_key('C')
            elif event.key == pygame.K_s:
                check_key('D')
            elif event.key == pygame.K_d:
                check_key('E' )
            elif event.key == pygame.K_f:
                check_key('F')
            elif event.key == pygame.K_g:
                check_key('G')
            elif event.key == pygame.K_h:
                check_key('A')
            elif event.key == pygame.K_j:
                check_key('B')
            elif event.key == pygame.K_SPACE:
                song_index = (song_index + 1) % len(songs)

                # Cập nhật màn hình
screen.fill(WHITE)

                # Vẽ các cột phím
pygame.draw.rect(screen, BLACK, [0, 0, 100, screen_height])
pygame.draw.rect(screen, BLACK, [screen_width - 100, 0, 100, screen_height])
pygame.draw.rect(screen, BLACK, [screen_width / 2 - 50, 0, 100, screen_height])

                # Vẽ các phím
key_width = 100
key_height = 50
key_padding = 10
for i in range(7):
    pygame.draw.rect(screen, BLACK,
    [key_padding + i * (key_width + key_padding), 350, key_width, key_height])
    text = font.render(keys[i], True, WHITE)
    screen.blit(text, [key_padding + i * (key_width + key_padding) + key_width / 2 - text.get_width() / 2,
    350 + key_height / 2 - text.get_height() / 2])

                # Hiển thị bài hát đang chơi
text = font.render('Song: ' + str(song_index + 1), True, BLACK)
screen.blit(text, [10, 10])

                # Hiển thị điểm số
text = font.render('Score: ' + str(score), True, BLACK)
screen.blit(text, [screen_width - 10 - text.get_width(), 10])

                # Hiển thị số lần nhấn sai hoặc bỏ qua
text = font.render('Misses: ' + str(misses), True, BLACK)
screen.blit(text, [screen_width / 2 - text.get_width() / 2, 10])

                # Nếu bài hát đã kết thúc thì hiển thị thông báo
if song_index == 0 and len(songs[song_index]) == 0:
    text = font.render('You won! Final score: ' + str(score), True, GREEN)
screen.blit(text, [screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2])
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
quit()

pygame.display.flip()
clock.tick(60)

