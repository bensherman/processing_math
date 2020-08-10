import math 

width = 1000
height = 500
chunksize = width / 100
points = width / chunksize


    
# global, modified by kepresses
rate = 2.99
starting_population = .6


def setup():
    size(width, height)
    # color
    stroke(26, 134, 138)

def logistic(r, x):
    return r * x * (1 - x)

def draw():
    global rate
    global starting_population
    
    background(13, 67, 69)

    
    if starting_population > 1:
        starting_population = 1
    if starting_population < 0:
        starting_population = 0

    # osciuliscope blue
    # background(13, 67, 69)
        
    textSize(chunksize)
    text("rate: {}".format(rate), chunksize, chunksize)
    text("starting_population: {}".format(starting_population), chunksize, chunksize *2)
    
    population = starting_population
    old_xpos = 0
    old_ypos = height - (height * starting_population)
    
    for i in range(points):
        xpos = old_xpos + chunksize
        ypos = height - (height * population)
        
        line(old_xpos, old_ypos, xpos, ypos)
        
        old_xpos = xpos
        old_ypos = ypos
        
        population = logistic(rate, population)        
        
        
        
    if keyPressed:
        if key == 's':
            rate -= .001
            if rate < 0:
                rate = 0
        if key == 'w':
            rate += .001
        
        if key == 'a':
            starting_population -= .001
        
        if key == 'd':
            starting_population += .001
            if starting_population < 0:
                starting_population = 0        
    
def keyPressed():
  global rate
    
    

    
