# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

from Coin import Coin

class Vehicle():

    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -2)
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 8
        self.maxforce = 0.2

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def arrive(self, c, target, coins):
        
        # A vector pointing from the location to the target
        desired = target - self.position
        d = desired.mag()

        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
            if(d < 30):
                coins = c.update(1280, 720, coins)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)
        return coins

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(255, 255, 255)
        stroke(0, 0, 0)
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
