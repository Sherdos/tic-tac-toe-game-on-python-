import pygame, random



pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Py game')
icon = pygame.image.load('media/image/game.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

square = pygame.Surface((50,170))
square.fill('Blue')

myfont = pygame.font.Font('media/font/RobotoMono-VariableFont_wght.ttf',40)
text_surface = myfont.render('Hello world',True,'Red')


# field = pygame.image.load('media/image/field.png')
# field_rect = field.get_rect(topleft=(10, 100)) 


running = True

order = True

class Field(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=position)
        
fields_group = pygame.sprite.Group()

for y in range(1,4):
    for x in range(1,4):
        field = Field('media/image/field.png', (100*x, 100*y))
        fields_group.add(field)

while running:
    
    screen.fill("Green")
    fields_group.draw(screen)
    
    clock.tick(60)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for field in fields_group:
                if field.rect.collidepoint(event.pos):
                    if order:
                        field.image = pygame.image.load('media/image/circle.png')
                        order = False
                    else:
                        field.image = pygame.image.load('media/image/cros.png')
                        order = True