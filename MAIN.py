import pygame
import json
import urllib
import subprocess
from naoqi import ALProxy
#managerProxy = ALProxy("ALBehaviourManager","155.245.20.83", 9559)

pygame.init()
 
# Set the screen size
size = [1, 1]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Nao Robot")

#Loop until you click close button
done = False

#speed of updates
clock = pygame.time.Clock()

# Initialize the joystick module
pygame.joystick.init()

    


#############################################################################################################################################################################################################################################
#############################################################################################################################################################################################################################################
#MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP MAIN LOOP 
joystick = pygame.joystick.Joystick(0)#assign joystick to the connected controller
joystick.init()#intialise the controller
# Get the name of the controller
name = joystick.get_name()

while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Quit the program
            
        

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        for i in range( axes ):
            axis = joystick.get_axis( i )
        if joystick.get_axis(2)>0.7:
            print('LT')
        if joystick.get_axis(2)<-0.7:
            print('RT')

    ##LEFT JOYSTICK
        if joystick.get_axis(1)>0.9:
            #print('Left stick Down.')
            exec(open('walk backwards.py').read())
        if joystick.get_axis(1)<-0.9:
            #print('Left stick Up.')
            exec(open('walk forwards.py').read())
        if joystick.get_axis(0)>0.9:
            #print('Left stick Right.')
            exec(open('walkright.py').read())
        if joystick.get_axis(0)<-0.9:
            #print('Left stick Left.')
            exec(open('walkleft.py').read())
        if joystick.get_axis(1)<0.85 and joystick.get_axis(1)>0.5 and joystick.get_axis(0)<0.85 and joystick.get_axis(0)>0.5:
            #print('Left stick Right+Down')
            exec(open('backwardright.py').read())
        if joystick.get_axis(1)<0.85 and joystick.get_axis(1)>0.5 and joystick.get_axis(0)>-0.85 and joystick.get_axis(0)<-0.5:
            #print('Left stick Left+Down')
            exec(open('backwardleft.py').read())
        if joystick.get_axis(1)>-0.85 and joystick.get_axis(1)<-0.5 and joystick.get_axis(0)<0.85 and joystick.get_axis(0)>0.5:
            #print('Left stick Right+Up')
            exec(open('forwardright.py').read())
        if joystick.get_axis(1)>-0.85 and joystick.get_axis(1)<-0.5 and joystick.get_axis(0)>-0.85 and joystick.get_axis(0)<-0.5:
            #print('Left stick Left+Up')
            exec(open('forwardleft.py').read())

    ##RIGHT JOYSTICK
        if joystick.get_axis(3)>0.9:
            print('Right stick Down.')
        if joystick.get_axis(3)<-0.9:
            print('Right stick Up.')
        if joystick.get_axis(4)>0.9:
            print('Right stick Right.')
        if joystick.get_axis(4)<-0.9:
            print('Right stick Left.')
        if joystick.get_axis(3)<0.85 and joystick.get_axis(3)>0.5 and joystick.get_axis(4)<0.85 and joystick.get_axis(4)>0.5:
            print('Right stick Right+Down')
        if joystick.get_axis(3)<0.85 and joystick.get_axis(3)>0.5 and joystick.get_axis(4)>-0.85 and joystick.get_axis(4)<-0.5:
            print('Right stick Left+Down')
        if joystick.get_axis(3)>-0.85 and joystick.get_axis(3)<-0.5 and joystick.get_axis(4)<0.85 and joystick.get_axis(4)>0.5:
            print('Right stick Right+Up')
        if joystick.get_axis(3)>-0.85 and joystick.get_axis(3)<-0.5 and joystick.get_axis(4)>-0.85 and joystick.get_axis(4)<-0.5:
            print('Right stick Left+Up')
            
                
        buttons = joystick.get_numbuttons()

        for i in range( buttons ):
            button = joystick.get_button( i )
            if button==1:
                if i==0:
                    subprocess.call(['E:\\Choregraphe\Monitor 2.1.4.lnk'], shell=True)
                if i==1:
                    managerProxy.post.runBehavior(wave)
                if i==2:
                    managerProxy.post.runBehavior(heyyou)
                if i==3:
                    exec(open('ocr.py').read())
                if i==4:
                    print('LB')
                if i==5:
                    print('RB')
                if i==6:
                    managerProxy.post.runBehavior(sit)
                if i==7:
                    managerProxy.post.runBehavior(leds)
                if i==8:
                    print('L')
                if i==9:
                    print('R')
                    

            
        # Hat switch. (D-pad)
        hats = joystick.get_numhats()


        for i in range( hats ):
            hat = joystick.get_hat( i )
            if hat[0]==1:
                if hat[1]==1:
                    print('Right+Up')
                elif hat[1]==-1:
                    print('Right+Down')
                elif hat[1]==0:
                    print('Right')
            if hat[0]==-1:
                if hat[1]==1:
                    print('Left+Up')
                elif hat[1]==-1:
                    print('Left+Down')
                elif hat[1]==0:
                    print('Left')
            if hat[0]==0:
                if hat[1]==1:
                    print('Up')
                elif hat[1]==-1:
                    print('Down')



    # Limit to 60 frames per second
    clock.tick(10)
    
pygame.quit ()#quit
