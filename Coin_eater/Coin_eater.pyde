# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle

x1=100
x2=20
y1=0
y2=20
steps=0

def setup():
    global v
    size(640, 360)
    v = Vehicle(width / 2, height / 2)
    
    global sf, steps, r1, r2
    #size(200, 200)
    background(255) # white
    r1= int(random(5,155))
    r2 = int(r1/10) * 10
    print("This is the random number", r1)
    print("This is the random number", r2)


def draw():
    background(51)
    
    global x1,y1,x2,y2, steps
    fill(39,79,188)
    rect(r2,r2,x2,y2)

    fill(155)
    stroke(1)
    rect(x1, y1, x2, y2)
    noStroke()
    rect(0,0,5, height-25)
    rect(0,height-25,width, 5)
    rect(width-5, 0, 5, height-25)
    rect(0,0,width, 5)
    # score header
    text("SCORE", 10, height-5) 
    # steps counter
    text(steps, 60, height-5)

    mouse = PVector(mouseX, mouseY)
    fruit = PVector(400, 300)
    fruit2 = PVector(100, 100)

    # Draw an ellipse at the mouse position
    fill(127)
    stroke(200)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)

    # Call the appropriate steering behaviors for our agents
    #v.arrive(mouse)
    v.arrive(fruit)
    v.update()
    v.display()
    
    #delay(50000)
    #v.arrive(fruit2)
    #v.update()
    #v.display()
