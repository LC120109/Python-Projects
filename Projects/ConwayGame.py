#Conway's Game of Life
#Source: NeuralNine on Youtube

import time
import pygame
import numpy as np

Color_Bg = (10, 10, 10)
Color_Grid = (40, 40, 40)
Color_Die_Next = (170, 170, 170)
Color_Alive_Next = (255, 255, 255)

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = Color_Bg if cells[row, col] == 0 else Color_Alive_Next

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = Color_Die_Next
                
            elif 2 <= alive <=3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = Color_Alive_Next

        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = Color_Alive_Next
        
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    cells = np.zeros((60, 80))
    screen.fill(Color_Grid)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
                
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(Color_Grid)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == "__main__":
    main()