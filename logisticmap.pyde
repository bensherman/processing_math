import math 

width = 1000
height = 500
chunksize = width / 100
points = width / chunksize


    
# global, modified by kepresses
rate = 2.99
starting_p = .6


def setup():
    size(width, height)
    # color
    stroke(26, 134, 138)

def logistic(r, x):
    return r * x * (1 - x)

def draw():
    global rate
    global starting_p
    
    background(13, 67, 69)

    
    if starting_p > 1:
        starting_p = 1
    if starting_p < 0:
        starting_p = 0

    # osciuliscope blue
    # background(13, 67, 69)
        
    textSize(chunksize)
    text("rate: {}".format(rate), chunksize, chunksize)
    text("starting_p: {}".format(starting_p), chunksize, chunksize *2)
    
    p = starting_p
    old_xpos = 0
    old_ypos = height - (height * starting_p)
    
    for i in range(points):
        xpos = old_xpos + chunksize
        ypos = height - (height * p)
        
        line(old_xpos, old_ypos, xpos, ypos)
        
        old_xpos = xpos
        old_ypos = ypos
        
        p = logistic(rate, p)        
            
        
    if keyPressed:
        if key == 's':
            rate -= .01
            if rate < 0:
                rate = 0
        if key == 'w':
            rate += .01
        
        if key == 'a':
            starting_p -= .005
            if starting_p < 0:
                starting_p = 0
        
        if key == 'd':
            starting_p += .005
            if starting_p > 1:
                starting_p = 1       

    

    
