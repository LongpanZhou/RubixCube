import numpy as np
import pygame
import os
pygame.init()
Width, Height = 1440, 1080
spacing = 5

RGB = {
    'background': (189, 172, 161),
    0: (255, 255, 255),
    1: (0, 70, 173),
    2: (0, 155, 72),
    3: (255, 213, 0),
    4: (183, 18, 52),
    5: (255, 88, 0),
}

win = pygame.display.set_mode((Width, Height))
logo = pygame.image.load("rubix.png")
icon_size = (150,150)

rotations = [pygame.image.load(os.path.join("icons","reset.png")), pygame.image.load(os.path.join("icons","X.png")), pygame.image.load(os.path.join("icons","Y.png")),
             pygame.image.load(os.path.join("icons","Z.png"))]

images_1 = [pygame.image.load(os.path.join("icons","Up.png")), pygame.image.load(os.path.join("icons","Down.png")),
            pygame.image.load(os.path.join("icons","Front.png")), pygame.image.load(os.path.join("icons","Back.png")),
            pygame.image.load(os.path.join("icons","Right.png")), pygame.image.load(os.path.join("icons","Left.png"))]

images_2 = [pygame.image.load(os.path.join("icons","Up'.png")), pygame.image.load(os.path.join("icons","Down'.png")),
            pygame.image.load(os.path.join("icons","Front'.png")), pygame.image.load(os.path.join("icons","Back'.png")),
            pygame.image.load(os.path.join("icons","Right'.png")), pygame.image.load(os.path.join("icons","Left'.png"))]
clock = pygame.time.Clock()


class Rubix:
    facedict = {"U": 0, "D": 1, "F": 2, "B": 3, "R": 4, "L": 5}
    cube = np.array([np.tile(i, (3, 3)) for i in range(6)])

    def move(self, direction, prime):
        if prime == False:
            # save front face
            match self.facedict[direction]:
                case 0:
                    temp = np.copy(self.cube[2][0])
                    self.cube[2][0] = self.cube[4][0]
                    self.cube[4][0] = self.cube[3][0]
                    self.cube[3][0] = self.cube[5][0]
                    self.cube[5][0] = temp
                case 1:
                    temp = np.copy(self.cube[2][2])
                    self.cube[2][2] = self.cube[5][2]
                    self.cube[5][2] = self.cube[3][2]
                    self.cube[3][2] = self.cube[4][2]
                    self.cube[4][2] = temp
                case 2:
                    temp = np.copy(self.cube[0][2])
                    self.cube[0][2] = self.cube[5][:, [2]].flatten()
                    self.cube[5][:, [2]] = self.cube[1][0].reshape((3, 1))
                    self.cube[1][0] = self.cube[4][:, [0]].flatten()
                    self.cube[4][:, [0]] = temp.reshape((3, 1))
                case 3:
                    temp = np.copy(self.cube[0][0])
                    self.cube[0][0] = self.cube[4][:, [2]].flatten()
                    self.cube[4][:, [2]] = self.cube[1][2].reshape((3, 1))
                    self.cube[1][2] = self.cube[5][:, [0]].flatten()
                    self.cube[5][:, [0]] = temp.reshape((3, 1))
                case 4:
                    temp = np.copy(self.cube[2][:,[2]])
                    self.cube[2][:, [2]] = self.cube[1][:, [2]]
                    self.cube[1][:, [2]] = self.cube[3][:, [2]]
                    self.cube[3][:, [2]] = self.cube[0][:, [2]]
                    self.cube[0][:, [2]] = temp
                case 5:
                    temp = np.copy(self.cube[2][:,[0]])
                    self.cube[2][:, [0]] = self.cube[0][:, [0]]
                    self.cube[0][:, [0]] = self.cube[3][:, [0]]
                    self.cube[3][:, [0]] = self.cube[1][:, [0]]
                    self.cube[1][:, [0]] = temp
        else:
            match self.facedict[direction]:
                case 0:
                    temp = np.copy(self.cube[2][0])
                    self.cube[2][0] = self.cube[5][0]
                    self.cube[5][0] = self.cube[3][0]
                    self.cube[3][0] = self.cube[4][0]
                    self.cube[4][0] = temp
                case 1:
                    temp = np.copy(self.cube[2][2])
                    self.cube[2][2] = self.cube[4][2]
                    self.cube[4][2] = self.cube[3][2]
                    self.cube[3][2] = self.cube[5][2]
                    self.cube[5][2] = temp
                case 2:
                    temp = np.copy(self.cube[0][2])
                    self.cube[0][2] = self.cube[4][:, [0]].flatten()
                    self.cube[4][:, [0]] = self.cube[1][0].reshape((3, 1))
                    self.cube[1][0] = self.cube[5][:, [2]].flatten()
                    self.cube[5][:, [2]] = temp.reshape((3, 1))
                case 3:
                    temp = np.copy(self.cube[0][0])
                    self.cube[0][0] = self.cube[5][:, [0]].flatten()
                    self.cube[5][:, [0]] = self.cube[1][2].reshape((3, 1))
                    self.cube[1][2] = self.cube[4][:, [2]].flatten()
                    self.cube[4][:, [2]] = temp.reshape((3, 1))
                case 4:
                    temp = np.copy(self.cube[2][:,[2]])
                    self.cube[2][:, [2]] = self.cube[0][:, [2]]
                    self.cube[0][:, [2]] = self.cube[3][:, [2]]
                    self.cube[3][:, [2]] = self.cube[1][:, [2]]
                    self.cube[1][:, [2]] = temp
                case 5:
                    temp = np.copy(self.cube[2][:,[0]])
                    self.cube[2][:, [0]] = self.cube[1][:, [0]]
                    self.cube[1][:, [0]] = self.cube[3][:, [0]]
                    self.cube[3][:, [0]] = self.cube[0][:, [0]]
                    self.cube[0][:, [0]] = temp

    def turn(self, direction):
        #facedict = {"U": 0, "D": 1, "F": 2, "B": 3, "R": 4, "L": 5}
        match direction:
            case 'X':
                temp = np.copy(self.cube[2])
                self.cube[2] = self.cube[1]
                self.cube[1] = self.cube[3]
                self.cube[3] = self.cube[0]
                self.cube[0] = temp
            case 'Y':
                temp = np.copy(self.cube[2])
                self.cube[2] = self.cube[5]
                self.cube[5] = self.cube[3]
                self.cube[3] = self.cube[4]
                self.cube[4] = temp
            case 'Z':
                temp = np.copy(self.cube[0])
                self.cube[0] = self.cube[4]
                self.cube[4] = self.cube[1]
                self.cube[1] = self.cube[5]
                self.cube[5] = temp


def draw_grid(win, grid, x, y):
    for i in range(3):
        for j in range(3):
            n = grid[i][j]

            rect_y = y + i * 360 // 3 + spacing
            rect_x = x + j * 360 // 3 + spacing
            rect_w = 360 // 3 - 2 * spacing
            rect_h = 360 // 3 - 2 * spacing

            pygame.draw.rect(win, RGB[n], pygame.Rect(rect_x, rect_y, rect_w, rect_h), border_radius=8)


class button():
    def __init__(self, x, y, image, ids):
        self.img = image
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.id = ids

    def draw(self, win, cube):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.id == 0:
                    cube.cube = np.array([np.tile(i, (3, 3)) for i in range(6)])
                elif self.id == 1:
                    cube.turn(cube, 'X')
                elif self.id == 2:
                    cube.turn(cube, 'Y')
                elif self.id == 3:
                    cube.turn(cube, 'Z')
                elif self.id == 4:
                    cube.move(cube, 'U', False)
                elif self.id == 5:
                    cube.move(cube, 'D', False)
                elif self.id == 6:
                    cube.move(cube, 'F', False)
                elif self.id == 7:
                    cube.move(cube, 'B', False)
                elif self.id == 8:
                    cube.move(cube, 'R', False)
                elif self.id == 9:
                    cube.move(cube, 'L', False)
                elif self.id == 10:
                    cube.move(cube, 'U', True)
                elif self.id == 11:
                    cube.move(cube, 'D', True)
                elif self.id == 12:
                    cube.move(cube, 'F', True)
                elif self.id == 13:
                    cube.move(cube, 'B', True)
                elif self.id == 14:
                    cube.move(cube, 'R', True)
                elif self.id == 15:
                    cube.move(cube, 'L', True)
                pygame.time.wait(150)
        win.blit(self.img, (self.rect.x, self.rect.y))


def game_rubix():
    cube = Rubix
    running = True
    win.fill(RGB['background'])
    rotations_button = [button(0, 0, pygame.transform.scale(rotations[0], icon_size),0),
                        button(150, 150, pygame.transform.scale(rotations[1], icon_size), 1),
                        button(0, 150, pygame.transform.scale(rotations[2], icon_size), 2),
                        button(150, 0, pygame.transform.scale(rotations[3], icon_size), 3)]

    move_button = [button(720, 0, pygame.transform.scale(images_1[0], icon_size), 4),
                   button(960, 0, pygame.transform.scale(images_1[1], icon_size), 5),
                   button(1200, 0, pygame.transform.scale(images_1[2], icon_size), 6),
                   button(720, 720, pygame.transform.scale(images_1[3], icon_size), 7),
                   button(960, 720, pygame.transform.scale(images_1[4], icon_size), 8),
                   button(1200, 720, pygame.transform.scale(images_1[5], icon_size), 9)]

    move_prime_button = [button(720, 180, pygame.transform.scale(images_2[0], icon_size), 10),
                   button(960, 180, pygame.transform.scale(images_2[1], icon_size), 11),
                   button(1200, 180, pygame.transform.scale(images_2[2], icon_size), 12),
                   button(720, 900, pygame.transform.scale(images_2[3], icon_size), 13),
                   button(960, 900, pygame.transform.scale(images_2[4], icon_size), 14),
                   button(1200, 900, pygame.transform.scale(images_2[5], icon_size), 15)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_grid(win, cube.cube[0], 360, 0)
        draw_grid(win, cube.cube[1], 360, 720)
        draw_grid(win, cube.cube[2], 360, 360)
        draw_grid(win, cube.cube[3], 1080, 360)
        draw_grid(win, cube.cube[4], 720, 360)
        draw_grid(win, cube.cube[5], 0, 360)
        for i in rotations_button:
            i.draw(win,cube)
        for i in move_button:
            i.draw(win,cube)
        for i in move_prime_button:
            i.draw(win,cube)

        pygame.display.update()

game_rubix()
