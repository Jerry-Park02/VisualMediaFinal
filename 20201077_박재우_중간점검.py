import pygame
import math
import time
import os

pygame.init()

width = 1200
height = 675

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

main = True
ingame = True

keys = [0,0,0,0]
keyset = [0,0,0,0]

maxframe = 60
fps = 0

gst = time.time()

Time = time.time() - gst


ty = 0
tst = Time

t1 = []
t2 = []
t3 = []
t4 = []

def sum_note(n):
    if n==1:
        ty = 0
        tst = Time + 2
        t1.append([ty,tst])
    if n==2:
        ty = 0
        tst = Time + 2
        t2.append([ty,tst])
    if n==3:
        ty = 0
        tst = Time + 2
        t3.append([ty,tst])   
    if n==4:
        ty = 0
        tst = Time + 2
        t4.append([ty,tst])

speed = 2

while main:
    while ingame:

        Time = time.time() - gst
        fps = clock.get_fps()
        if fps ==0:
            fps = maxframe

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keyset[0] = 1
                    sum_note(1)
                if event.key == pygame.K_f:
                    keyset[1] = 1
                    sum_note(2)
                if event.key == pygame.K_j:
                    keyset[2] = 1
                    sum_note(3)
                if event.key == pygame.K_k:
                    keyset[3] = 1
                    sum_note(4)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0
        
        screen.fill((0,0,0))

        keys[0] += (keys[0] - keys[0]) / (2 * (maxframe / fps))
        keys[1] += (keys[1] - keys[1]) / (2 * (maxframe / fps))
        keys[2] += (keys[2] - keys[2]) / (2 * (maxframe / fps))
        keys[3] += (keys[3] - keys[3]) / (2 * (maxframe / fps))
        
        pygame.draw.rect(screen, (0,0,0), (width/2 - width/8, -int(width/100), width/4, height + int(width/50)))
        pygame.draw.rect(screen, (255,255,255), (width/2 - width/8, -int(width/100), width/4, height + int(width/50)), int(width/100))

        for i in range(7):
            i+= 1
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i),200 - ((200/7)*i)), (width/2 - width/8 + width/32 - (width/32)* keys[0], (height/12)*9 - (height/30)*keys[0] *i, width/16 * keys[0],(height/35)/ i))
        for i in range(7):
            i+= 1 
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i),200 - ((200/7)*i)), (width/2 - width/16 + width/32 - (width/32)* keys[1], (height/12)*9 - (height/30)*keys[1] *i, width/16 * keys[1],(height/35)/ i))
        for i in range(7):
            i+= 1
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i),200 - ((200/7)*i)), (width/2 + width/32 - (width/32)*keys[2], (height/12)*9 - (height/30)*keys[2] *i, width/16 * keys[2],(height/35)/ i))
        for i in range(7):
            i+= 1 
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i),200 - ((200/7)*i)), (width/2 + width/16 + width/32 - (width/32)*keys[3], (height/12)*9 - (height/30)*keys[3] *i, width/16 * keys[3],(height/35)/ i))
        
    
#==================
        for tile_data in t1:
            tile_data[0] = (height/12) * 9 + (Time - tile_data[1]) * 350 * speed * (height /900)
            pygame.draw.rect(screen, (255,255,255),(width/2 - width/8, tile_data[0] - height/100, width/16, height / 50))
            if tile_data[0] > height - (height/9):
                t1.remove(tile_data)

        for tile_data in t2:
            tile_data[0] = (height/12) * 9 + (Time - tile_data[1]) * 350 * speed * (height /900)
            pygame.draw.rect(screen, (255,255,255),(width/2 - width/16, tile_data[0] - height/100, width/16, height / 50))
            if tile_data[0] > height - (height/9):
                t2.remove(tile_data)

        for tile_data in t3:
            tile_data[0] = (height/12) * 9 + (Time - tile_data[1]) * 350 * speed * (height /900)
            pygame.draw.rect(screen, (255,255,255),(width/2, tile_data[0] - height/100, width/16, height / 50))
            if tile_data[0] > height - (height/9):
                t3.remove(tile_data)

        for tile_data in t4:
            tile_data[0] = (height/12) * 9 + (Time - tile_data[1]) * 350 * speed * (height /900)
            pygame.draw.rect(screen, (255,255,255),(width/2 + width/16 , tile_data[0] - height/100, width/16, height / 50))
            if tile_data[0] > height - (height/9):
                t4.remove(tile_data)

        
        pygame.draw.rect(screen, (0,0,0), (width/2 - width/8, (height/12) * 9, width/4, height/2))
        pygame.draw.rect(screen, (255,255,255), (width/2 - width/8, (height/12) * 9, width/4, height/2), int(height/100))

        pygame.display.flip()