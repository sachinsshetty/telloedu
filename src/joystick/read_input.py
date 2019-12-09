## Source : http://www.pygame.org/docs/ref/joystick.html

import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printJS(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    if(joystick_count == 1):

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        name = joystick.get_name()
        textPrint.printJS(screen, "Joystick name: {}".format(name) )
        textPrint.indent()

        # Get the name from the OS for the controller/joystick

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.

        ## Raise / Lower Drone

        if(joystick.get_axis( 5 ) > 0.9):
            textPrint.printJS(screen, "Raise :")
        textPrint.unindent()

        if(joystick.get_axis( 2 ) > 0.9):
            textPrint.printJS(screen, "Lower :")
        textPrint.unindent()


        ## Move Drone

        if(joystick.get_axis( 4 ) < -0.9):
            textPrint.printJS(screen, "Move Forward :")
        textPrint.unindent()

        if(joystick.get_axis( 4 ) > 0.9):
            textPrint.printJS(screen, "Move Reverse :")
        textPrint.unindent()

        if(joystick.get_axis( 3 ) < -0.9):
            textPrint.printJS(screen, "Move Right:")
        textPrint.unindent()

        if(joystick.get_axis( 3 ) > 0.9):
            textPrint.printJS(screen, "Move Left :")
        textPrint.unindent()

        ## Turn Drone

        if(joystick.get_axis( 0 ) < -0.9):
            textPrint.printJS(screen, "Camera Left:")
        textPrint.unindent()

        if(joystick.get_axis( 0 ) > 0.9):
            textPrint.printJS(screen, "Camera Right:")
        textPrint.unindent()

        ## Start / Stop Drone

        if(joystick.get_button(7)== 1):
            textPrint.printJS(screen, "Start : Take Off pressed" )
            textPrint.indent()

        if(joystick.get_button(6)== 1):
            textPrint.printJS(screen, "Back : Land pressed" )
            textPrint.indent()

        textPrint.unindent()


    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
