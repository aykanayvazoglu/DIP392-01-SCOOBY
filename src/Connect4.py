from pathlib import Path
from sys import exit
import pygame
import numpy as np

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Connect 4')
clock = pygame.time.Clock()

column_1 = pygame.Rect(292,0, 95, 720)
column_2 = pygame.Rect(392,0, 95, 720)
column_3 = pygame.Rect(492,0, 95, 720)
column_4 = pygame.Rect(592, 0, 95, 720)
column_5 = pygame.Rect(692,0, 95, 720)
column_6 = pygame.Rect(792,0, 95, 720)
column_7 = pygame.Rect(892,0, 95, 720)

asset_folder = Path('assets/')
background_surf = pygame.image.load(asset_folder / "bg.jpg").convert()

board_surf = pygame.image.load(asset_folder / "connect4Board.png").convert()
board_rect = board_surf.get_rect(midbottom=(640,720))

redtoken_surf = pygame.image.load(asset_folder / "redtoken.png")

bluetoken_surf = pygame.image.load(asset_folder / "bluetoken.png")

floor_rect = pygame.Rect(0, 709, 1280,11)

game_board = np.zeros((6, 7))
col1_pressed = 0
col2_pressed = 0
col3_pressed = 0
col4_pressed = 0
col5_pressed = 0
col6_pressed = 0
col7_pressed = 0
turn = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    turn = turn %2
    pygame.draw.rect(screen, (255,255,255), floor_rect)   
    pygame.draw.rect(screen, (0,0,0), column_1)
    pygame.draw.rect(screen, (0,0,0), column_2)
    pygame.draw.rect(screen, (0,0,0), column_3)
    pygame.draw.rect(screen, (0,0,0), column_4)
    pygame.draw.rect(screen, (0,0,0), column_5)
    pygame.draw.rect(screen, (0,0,0), column_6)
    pygame.draw.rect(screen, (0,0,0), column_7)     
    screen.blit(background_surf, (0,0))
    screen.blit(board_surf, board_rect)

    if(turn == 0):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        if column_1.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (300, 20))
            if mouse_buttons[0]:
                #game_board[col1_pressed][0]
                col1_pressed+=1
                screen.blit(redtoken_surf, (300, floor_rect.top - 80))
                print(col1_pressed)
        elif  column_2.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (392, 20))
            if mouse_buttons[0]:
                #game_board[col2_pressed][1]
                col2_pressed+=1
        elif  column_3.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (492, 20))
            if mouse_buttons[0]:
                #game_board[col3_pressed][2]
                col3_pressed+=1
        elif  column_4.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (592, 20))
            if mouse_buttons[0]:
                #game_board[col4_pressed][3]
                col4_pressed+=1
        elif  column_5.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (692, 20))
            if mouse_buttons[0]:
                #game_board[col5_pressed][4]
                col5_pressed+=1
        elif  column_6.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (792, 20))
            if mouse_buttons[0]:
                #game_board[col6_pressed][5]
                col6_pressed+=1
        elif  column_7.collidepoint(mouse_pos):
            screen.blit(redtoken_surf, (892, 20))
            if mouse_buttons[0]:
                #game_board[col7_pressed][0]
                col7_pressed+=1

        for col in range(7):
            for row in range(6):
                x_coord = 300 + col * 100
                y_coord = (floor_rect.top - 80) - 100*row
                #screen.blit(redtoken_surf, (x_coord, y_coord))
    pygame.display.update()
    clock.tick(60)
