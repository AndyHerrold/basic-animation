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
#build a box
    box = pygame.surface ((25, 25))
    box=box.convert()
    box.fill ((255, 0, 0))
#set box variables
    box_x = 0
    box_y = 200
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
# modify box values
        box_x +=5
#check boundaries
        if box_x> screen.get_width():
            box_x=0

# Refresh display
        screen.blit(backround, (0, 0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
# modify box values
        box_x +=5
#refresh screeen
        scren.blit(backround, (0, 0,))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
        
#load an image
        
        
#set image variables


pygame.quit()
if __name__ == "__main__":
    main()
    
        
    
    
    
    