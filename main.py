import pygame
import random
import time

pygame.init()

class TicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Pygame Tic Tac Toe')
        icon = pygame.image.load('media/image/game.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.myfont = pygame.font.Font('media/font/RobotoMono-VariableFont_wght.ttf', 40)
        self.fields_group = pygame.sprite.Group()
        self.create_fields()
        self.current_player = 'cros'

    def create_fields(self):
        for y in range(1, 4):
            for x in range(1, 4):
                field = Field('media/image/field.png', (100*x, 100*y), (x, y))
                self.fields_group.add(field)

    def check_board(self):
        all_win_positions = [
            {(1, 1), (1, 2), (1, 3)},
            {(2, 1), (2, 2), (2, 3)},
            {(3, 1), (3, 2), (3, 3)},
            {(1, 1), (2, 1), (3, 1)},
            {(1, 2), (2, 2), (3, 2)},
            {(1, 3), (2, 3), (3, 3)},
            {(1, 1), (2, 2), (3, 3)},
            {(3, 1), (2, 2), (1, 3)},
        ]
        cros_positions = [field.cordinate for field in self.fields_group if field.type == 1]
        circle_positions = [field.cordinate for field in self.fields_group if field.type == 2]
        for win_position in all_win_positions:
            if win_position <= set(cros_positions) and set(cros_positions):
                self.display_winner_message('cros wins!', 'Blue')
                self.reset_game()
            elif win_position <= set(circle_positions) and set(circle_positions):
                self.display_winner_message('circle wins!', 'Red')
                self.reset_game()

    def display_winner_message(self, message, color):
        text_surface = self.myfont.render(message, True, color)
        self.screen.blit(text_surface, (10, 10))
        pygame.display.update()
        time.sleep(2)

    def reset_game(self):
        self.fields_group.empty()
        self.create_fields()

    def run(self):
        running = True
        while running:
            self.screen.fill("Green")
            self.fields_group.draw(self.screen)
            self.clock.tick(60)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for field in self.fields_group:
                        if field.rect.collidepoint(event.pos):
                            if field.full:
                                if self.current_player == 'cros':
                                    field.image = pygame.image.load('media/image/cros.png')
                                    field.type = 1
                                    self.fields_group.draw(self.screen, field)
                                    self.current_player = 'circle'
                                else:
                                    field.image = pygame.image.load('media/image/circle.png')
                                    field.type = 2
                                    self.fields_group.draw(self.screen,field)
                                    self.current_player = 'cros'
                                field.full = False
                                self.check_board()

class Field(pygame.sprite.Sprite):
    def __init__(self, image, position, cordinate):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=position)
        self.cordinate = cordinate
        self.type = 0  # 1 - cros, 2 - circle
        self.full = True

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
