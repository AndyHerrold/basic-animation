#andy herrold basic animation
#import and initialize
import pygame

def main():
    pygame.init()
    
#Create Display
    screen = pygame.display.set_mode((640, 480))#not sure on effect of modifying these values
    pygame.display.set_caption("Hello!")
    
#Create backround entity
    backround = pygame.Surface(screen.get_size())
    backround = backround.convert()
    backround.fill((0, 255, 0))
