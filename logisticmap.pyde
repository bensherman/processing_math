
width = 500
height = 500

def setup():
    size(width, height)
    background(13, 67, 69)
    stroke(26, 134, 138)
    strokeWeight(100)

def logistic(r, x):
    return r * x * (1 - x)

def draw():
    rate = 2.0
    x = .5
    
    for _ in range(10):
        x = logistic(rate, x)
        print x
    
    
    noLoop()
