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
    backround.fill(pygame.Color("green"))
#Assign
    clock = pygame.time.Clock()
    keepGoing = True
#Set up main loop
    while keepGoing:
        clock.tic(30)
#event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
# Refresh display
        screen.blit(backround, (0, 0))
        pygame.display.flip()
#build a box
        box = pygame.surface ((25, 25))
        box=box.convert()
        box.fill ((255, 0, 0))
#set box variables
        box_x = 0
        box_y = 200
# modify box values
        box_x +=5
#check boundaries
        if box_x> screen.get_width():
            box_x=0
#refresh screeen
        scren.blit(backround, (0, 0,))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
        
#load an image
        
        
#set image variables


        
    pygame.quit()
    
        
    
    
    
    