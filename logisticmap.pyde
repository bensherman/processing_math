
w = 900
h = 900
rate = 0
x = .5

def setup():
    size(w,h)
    background(13, 67, 69)
    stroke(26, 134, 138)
    strokeWeight(1.5)

    
def logisticmap(x, r):
    print "new lm: ", x, r
    while True:
        x = r * x * (1 - x)
        yield x

def draw():
    global rate
    global stroke_color

    lm = logisticmap(.5, rate)
    y = lm.next()

    for i in range(100):
        x = y
        y = lm.next()
        point(x * w, h - (y * h))

            
    rate += .005
    print "rate: ", rate
    if x < 0:
        noLoop()
