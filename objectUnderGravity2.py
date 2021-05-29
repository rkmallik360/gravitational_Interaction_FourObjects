#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 19:51:24 2018

@author: radhakrishnamallik
"""

############################For installation of pygame in mac####
# python3 -m pip install -U pygame --user
#######################   For installation of Pygame in windows
#py -m pip install -U pygame --user
##################################


import pygame
import pygame.math
import random
vec = pygame.math.Vector2
# Define some colors

BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60

# Set the width and height of the screen [width, height]

WIDTH = 1500
DEPTH = 950
size = (WIDTH, DEPTH)
screen = pygame.display.set_mode(size)

# time and distance scale factor
DaySec = 24*60*60 # Sec
DayNo = 300 # Day Time Scale factor 1 sec = n day
TotalSec = DayNo*DaySec
DSF = 10E8 # m Scale factor for length


# assign data to planets
        
obj_height = 200
obj_height1 = 250
obj_height2 = 300
obj_dia = 10
planet_dia = 30
massPlanet = 1.9891E30  # in kg
vel_obj = vec(20000,-5000) # m/sec
vel_obj1 = vec(15000,-5000) # m/sec
vel_obj2 = vec(10000,-5000) # m/sec
G = 6.67E-11 # Converting time from sec to "DayNo" Day 

# Initial Calculation
Time = DayNo*DaySec/FPS
TimeCount = 5000
timeStep = Time/TimeCount
pos_obj = vec(WIDTH/3, DEPTH/2-obj_height)*DSF
pos_obj1 = vec(WIDTH/3, DEPTH/2-obj_height1)*DSF
pos_obj2 = vec(WIDTH/3, DEPTH/2-obj_height2)*DSF
pos_planet = vec(WIDTH/2, DEPTH/2)*DSF


# Setting the window title

pygame.display.set_caption("Object around the Planet")

#####################################PYGAME ENGINE#########################
pygame.init()

# Loop until the user clicks the close button.

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # -------game logic ......
      
      
    # -------screen clearing code...
      
    screen.fill(BLACK)
      
    # -------Drawing code....   
#   pygame.draw.circle(screen, BLUE,pos,40)

        
    for i in range(0,TimeCount,1):
        pos_wrtPlanet = (pos_planet - pos_obj)
        pos_wrtPlanet1 = (pos_planet - pos_obj1)
        pos_wrtPlanet2 = (pos_planet - pos_obj2)
        r = vec.length(pos_wrtPlanet)
        r1 = vec.length(pos_wrtPlanet1)
        r2 = vec.length(pos_wrtPlanet2)
        acc_obj = (G*massPlanet/(r**3))*pos_wrtPlanet
        acc_obj1 = (G*massPlanet/(r1**3))*pos_wrtPlanet1
        acc_obj2 = (G*massPlanet/(r2**3))*pos_wrtPlanet2
        pos_obj += vel_obj*timeStep+0.5*acc_obj*timeStep**2
        pos_obj1 += vel_obj1*timeStep+0.5*acc_obj1*timeStep**2
        pos_obj2 += vel_obj2*timeStep+0.5*acc_obj2*timeStep**2
        vel_obj += acc_obj*timeStep
        vel_obj1 += acc_obj1*timeStep
        vel_obj2 += acc_obj2*timeStep
    obj = pygame.draw.circle(screen, RED, [int(pos_obj.x/DSF), int(pos_obj.y/DSF)], obj_dia)
    obj1 = pygame.draw.circle(screen, RED, [int(pos_obj1.x/DSF), int(pos_obj1.y/DSF)], obj_dia)
    obj2 = pygame.draw.circle(screen, RED, [int(pos_obj2.x/DSF), int(pos_obj2.y/DSF)], obj_dia)
    PLANET1 = pygame.draw.circle(screen,GREEN, [int(pos_planet.x/DSF),int(pos_planet.y/DSF)],planet_dia)
            
    # -------Update the screen with what have beed drawn...
    
    pygame.display.flip()
    
    # -------define frame per second 
    
    clock.tick(FPS)
    
# Close the window and quit
pygame.quit()      
        