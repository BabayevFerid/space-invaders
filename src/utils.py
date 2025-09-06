import pygame

def load_image(path, scale=None):
    """
    Şəkli yükləyir, istəsən ölçüsünü dəyişir.
    """
    image = pygame.image.load(path).convert_alpha()
    if scale:
        image = pygame.transform.scale(image, scale)
    return image

def check_collision(rect1, rect2):
    """
    İki rect arasında toqquşma yoxlaması.
    """
    return rect1.colliderect(rect2)
