import pygame
import board
import spritesheet as ss
import algortihms
import time

# Get the sprites from spritesheet
sprite_sheet = ss.SpriteSheet(pygame.image.load("assets.png"))
empty = sprite_sheet.get_sprite(0, 16, 16, 2)
open = sprite_sheet.get_sprite(1, 16, 16, 2)
closed = sprite_sheet.get_sprite(2, 16, 16, 2)
key = sprite_sheet.get_sprite(3, 16, 16, 2)
wall = sprite_sheet.get_sprite(4, 16, 16, 2)

# Draw And Update The Window
def draw(window, board):
    for r in range(board.size[0]):
        for c in range(board.size[1]):
            # Drawing Grid
            if board.board[r][c].key:
                window.blit(key, (c * 32, r * 32))
            elif board.board[r][c].wall:
                window.blit(wall, (c * 32, r * 32))
            elif board.board[r][c].open:
                window.blit(open, (c * 32, r * 32))
            elif board.board[r][c].open == False:
                window.blit(closed, (c * 32, r * 32))
            else:
                window.blit(empty, (c * 32, r * 32))
    pygame.display.update() # Update Window

# Mainloop
def mainloop(width, height, row, col, s_loc, t_loc):
    b = board.Board(row, col, s_loc, t_loc)

    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PathFinding")

    # Event Handler
    running = True
    solve = False
    djik = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit The Game
                running = False
            if pygame.mouse.get_pressed()[0] and not solve:
                # Detect Row And Column
                crow = pygame.mouse.get_pos()[1] // 32
                ccol = pygame.mouse.get_pos()[0] // 32
                if not b.board[crow][ccol].key:
                    b.click(crow, ccol)
            if event.type == pygame.KEYDOWN and not solve:
                if event.key == pygame.K_d:
                    d = algortihms.Djikstra(b, s_loc, t_loc)
                    djik = True
                    solve = True
        
        if solve:
            if djik:
                # Loop For The Djikstra
                if d.solve():
                    print("Djikstra Algorithm")
                    print(f"Length: {b.board[t_loc[0]][t_loc[1]].g}")
                    draw(window, b)
                    time.sleep(5)
                    running = False
            time.sleep(0.2)
        draw(window, b)
    pygame.quit()
    
mainloop(320, 320, 10, 10, (3, 1), (6, 9))