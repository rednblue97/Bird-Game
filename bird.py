import pygame
from settings import import_sprite


class Bird(pygame.sprite.Sprite):
    def __init(self, pos, size):
        super().__init__()

        self.frame_index = 0
        self.animation_delay = 3
        self.jump_move = -9

        #bird being animated

        self.bird_img = import_sprite("assets/redbird-upflap.png")
        self.image = self.bird_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.direction = pygame.math.Vector(0,0)
        self.score = 0

    #flying animation
        
    def _animate(self):
        sprites = self.bird_img
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0

    #make the bird fly higher
            
    def _jump(self):
        self.direction.y = self.jump_move

    def update(self, is_jump):
        if is_jump:
            self._jump()
        self._animate()

