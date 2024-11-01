#andy herrold basic animation
#import and initialize
import pygame

def main():
    pygame.init()
    
#Create Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Taxi!")
    backround = pygame.Surface(screen.get_size())
    backround.fill ("green")
    screen.blit (backround, (0, 0))
#load an image
    self.image = pygame.image.load("taxi.png")
    self.image.convert_alpha()
#Try different sclales
    self.image = pygame.transform.scale(self.image, (100, 100))
#create corresponding rect
    self.rect = self.image.get_rect()
#make adjustments if needed
    self.rect.centerx = 320
    self.rect.centery = 240
#create movement
    self.dx = 5
    self.dy = 3
#set update method
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
#check bounds
        if self.rect.right > screen.get_width():
            self.rect.left = 0
        if self.rect.bottom > screen.get_height():
            self.rect.top = 0
#set taxi variables
    taxi_x = 0
    taxi_y = 200
# instantiate taxi
    taxi = Taxi()
    allSprites = pygame.sprite.Group(taxi)
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
# clear and redraw
    allSprites.clear (screen, backround)
    allSprites.update()
    allSprites.draw(screen)
    pygane.display.flip()
# modify image values
    taxi_x +=5
#check boundaries
    if taxi_x> screen.get_width():
        taxi_x=0

# Refresh display
        screen.blit(backround, (0, 0))
        screen.blit(taxi, (taxi_x, taxi_y))
        pygame.display.flip()
    
#refresh screeen
        scren.blit(backround, (0, 0,))
        screen.blit(taxi, (taxi_x, taxi_y))
        pygame.display.flip()
        
    
        


if __name__ == "__main__":
    main()
    pygame.quit()
    
        
    
    
    
    

