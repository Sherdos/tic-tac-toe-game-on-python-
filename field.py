import pygame


class Field(pygame.sprite.Sprite):
    def __init__(self, image, position, cordinate):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=position)
        self.cordinate = cordinate
        self.type = 0  # 1 - cros, 2 - nought
        self.full = True