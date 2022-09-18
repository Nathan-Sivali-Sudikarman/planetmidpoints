import pygame
from sys import exit
import time
from copy import deepcopy
import math
import matplotlib.pyplot as plt
import random

pygame.init()

max_width = 1300
max_height = 700
centre = [max_width/2,max_height/2]

clock = pygame.time.Clock()
clock.tick(50)


screen = pygame.display.set_mode((max_width, max_height))
displayfont = pygame.font.Font(None,23)
titlefont = pygame.font.Font(None,35)
        

freq = 3


def calcradius(freq):
    return pow(freq,2/3)
while True:

    #freq = float(input("What should the ratio of the frequency between the planets be?"))
    screen = pygame.display.set_mode((max_width, max_height))
    


    theta = 0
    line_segment = False #boolean to draw line segment
    midpoint = False #flag to draw midpoints or not
    midpoints = [] #list of midpoints
    scale_radius = calcradius(freq)
    on_reset = False #a flag to tell the program whetehr or not the values of r and freq are chanigng
    angles = []
    distances = [] #list containing distances and theta values
    since_on = 0 #see: under key press M
    instructions_bool = False #toggles window for displaying instructions
    displayratio = True #boolean that affects whetehr or not we display ratio
 
    while True:


        
        screen.fill((0,0,0)) #fill the screen black

        ####################
        ###quit condition###
        ####################

        planet1 = (centre[0]+ 30*math.cos(freq*theta), centre[1] + 30*math.sin(freq*theta))
        
        planet2 = (centre[0]+30*scale_radius*math.cos(theta),centre[1]+30*scale_radius*math.sin(theta))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_l:
                    
                    line_segment = not line_segment #flip line_segment bool value

                if event.key == pygame.K_m:

                    since_on = 0 #measures the angle (in radians) since midpoint was turned on so that we dont have to draw unnecessary circles

                    midpoints = [] #reset midpoint values

                    midpoint = not midpoint #flip midpoint bool value
                    


                if event.key == pygame.K_a: #add 1 to the frequency value

                    since_on = 0 #reset since on
                    midpoints = [] #reset midpoints
                    
                    freq += 1
                    scale_radius = calcradius(freq)

                    on_reset = True

                if event.key == pygame.K_r and freq != 1: #minus 1 to the frequency value

                    since_on = 0
                    midpoints = []
                    freq -= 1
                    scale_radius = calcradius(freq)

                    on_reset = True

                if event.key == pygame.K_i:
                    instructions_bool = not instructions_bool
                    

                
                if event.key == pygame.K_f:
                    displayratio = not displayratio

                    

        if not on_reset: #if not changing freq and r values
            if line_segment:
                pygame.draw.line(screen,(127.5,127.5,127.5),planet1,planet2)

                
            if not instructions_bool:

                instructions = displayfont.render("Press I for instructions", True, (125.5,125.5,125.5))
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (100,20)
                screen.blit(instructions,instructionsrect)



            else:
                instructiontitle = titlefont.render("Instructions:", True, (0,255,0))
                instructiontitlerect = instructiontitle.get_rect()
                instructiontitlerect.center = (100,20)
                screen.blit(instructiontitle,instructiontitlerect)

                instructions = displayfont.render(f"- Press L to turn on line segments", True, (255,255,255))
                
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (140,45)
                screen.blit(instructions,instructionsrect)

                
                instructions = displayfont.render(f"- Press M to draw out the midpoints", True, (255,255,255))
                
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (145,65)
                screen.blit(instructions,instructionsrect)


                instructions = displayfont.render(f"- Press A to add 1 more to the frequency ratio", True, (255,255,255))
                
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (181,85)
                screen.blit(instructions,instructionsrect)

                
                instructions = displayfont.render(f"- Press R to remove 1 from the frequency ratio", True, (255,255,255))
                
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (184,105)
                screen.blit(instructions,instructionsrect)

                
                instructions = displayfont.render(f"- Press I to toggle instructions", True, (255,255,255))
                
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (128,125)
                screen.blit(instructions,instructionsrect)

                
                instructions = displayfont.render(f"- Press F to toggle displaying frequency ratio", True, (255,255,255))
                
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (182,145)
                screen.blit(instructions,instructionsrect)
            ############
            ###orbits###
            ############

            pygame.draw.circle(screen, (255,255,255), centre, 30*scale_radius, 1)
            
            pygame.draw.circle(screen, (255,255,255), centre, 30, 1)
            
            pygame.draw.circle(screen, (255,0,0), centre, 10)


            #############
            ###planets###
            #############


            pygame.draw.circle(screen,(255,255,0),planet1,3)


            pygame.draw.circle(screen, (0,255,255), planet2, 3)

            distance = math.sqrt(((planet1[0]-planet2[0])**2 + (planet1[1]-planet2[1])**2))


            angles.append(theta)
            distances.append(distance)

            if midpoint:

                if since_on < 2*math.pi:
                    midpoints.append(((planet1[0]+planet2[0])/2,(planet1[1]+planet2[1])/2))

                for mid in midpoints:
                    pygame.draw.circle(screen,(255,0,255),mid,1)

            if displayratio:
                instructions = titlefont.render(f"Current freq ratio: {freq}", True, (0,0,255))
                instructionsrect = instructions.get_rect()
                instructionsrect.center = (max_width//2,20)
                screen.blit(instructions,instructionsrect)
            

            theta += 0.005
            since_on += 0.005

            pygame.display.update()

        
        if on_reset:
            on_reset = False #flip at the end

