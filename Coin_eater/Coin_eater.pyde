from Vehicle import Vehicle
from Coin import Coin

coins = 0

def setup():
    global v, c, coins
    size(1280, 720)
    v = Vehicle(width / 2, height / 2)
    c = Coin(width, height)

def draw():
    global v, c, coins
    
    background(51)
    
    # score header
    textSize(32)
    fill(255, 255, 255)
    text("COINS", 50, 60)
    
    coin = c.position
    
    c.display(coin.x, coin.y, coins)
    coins = v.arrive(c, coin, coins)
    v.update()
    v.display()
