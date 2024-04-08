from field import Field
import pygame

pygame.init()

class TicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Pygame Tic Tac Toe')
        icon = pygame.image.load('media/image/game.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.myfont = pygame.font.Font('media/font/RobotoMono-VariableFont_wght.ttf', 40)
        self.fields_group = pygame.sprite.Group()
        self.create_fields()
        self.current_player = 'cross'
        self.running = True

    def create_fields(self):
        # Создание полей для игры (3х3)
        for y in range(1, 4):
            for x in range(1, 4):
                field = Field('media/image/field.png', (100*x, 100*y), (x, y))
                self.fields_group.add(field)

    def check_board(self):
        # Проверка поля игры
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
        cross_positions = [field.cordinate for field in self.fields_group if field.type == 1]
        nought_positions = [field.cordinate for field in self.fields_group if field.type == 2]
        for win_position in all_win_positions:
            if win_position <= set(cross_positions) and set(cross_positions):
                self.display_winner_message('cross wins!', 'Blue')
                self.reset_game()
            elif win_position <= set(nought_positions) and set(nought_positions):
                self.display_winner_message('nought wins!', 'Red')
                self.reset_game()

    def display_winner_message(self, message, color):
        # Поздравительный текст победителя
        text_surface = self.myfont.render(message, True, color)
        self.screen.blit(text_surface, (10, 10))
        pygame.display.update()
        pygame.time.wait(2000)

    def reset_game(self):
        # перезапуск игры
        self.fields_group.empty()
        self.create_fields()
        self.current_player = 'cross'
        
    def check_event(self):
        # Проверка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.click_on_field(event)
                    
    
    def click_on_field(self, event):
        # Действие при клике на поле
        for field in self.fields_group:
            if field.rect.collidepoint(event.pos):
                self.full_field(field)
                if self.is_board_full():
                    self.fields_group.draw(self.screen)
                    self.display_winner_message('Draw', 'Orange')
                    pygame.time.wait(2000)
                    self.reset_game()
                
    def is_board_full(self):
        for field in self.fields_group:
            if field.full:
                return False  # If any field is empty, return False
        return True  # If all fields are occupied, return True
    
    def full_field(self, field):
        # действие при свободном поле
        if field.full:
            self.mark_field(field)
            field.full = False
            self.check_board()
        
    def mark_field(self, field):
        # отметка поля крести или нолик
        if self.current_player == 'cross':
            self.change_field(field, 'cross.png', 1, 'nouht')
        else:
            self.change_field(field, 'nought.png', 2, 'cross')
    
    def change_field(self,field,image,type_of_field,next_player):
        # Изменение поля 
        field.image = pygame.image.load(f'media/image/{image}')
        field.type = type_of_field
        self.fields_group.draw(self.screen, field)
        self.current_player = next_player
        pygame.display.flip()
        
        
    def run(self):
        # запуск игры
        while self.running:
            self.screen.fill((47,54,153))
            self.fields_group.draw(self.screen)
            self.clock.tick(60)
            pygame.display.update() 
            self.check_event()
            
    

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
