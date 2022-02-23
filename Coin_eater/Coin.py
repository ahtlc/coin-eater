class Coin():

    def __init__(self, w, h):
        x=random(w)
        y=random(h)
        self.position = PVector(x, y)
        self.r = 10
        
    def update(self, w, h, coins):
        x=random(w)
        y=random(h)
        self.position = PVector(x, y)
        self.display
        # coin counter
        coins = coins + 1
        return coins
        
    def display(self, x, y, coins):
        # Draw an circle representing the coin
        fill(255, 210, 0)
        stroke(255, 255, 0)
        strokeWeight(4)
        ellipse(x, y, 30, 30)
        # Draw the amount of coins
        text(coins, 170, 60)
