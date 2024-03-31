import pygame


class Pipe(pygame.sprite.Sprite): 
    def __init__(self, pos, width, height, flip):
        super().__init__()
        self.width = width
        img_path = 'assets/pipe-green.png'
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        if flip:
            flipped_image = pygame.transform.flip(self.image, False, True)
            self.image = flipped_image
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

        if self.rect.right < (-self.width):
            self.kill
