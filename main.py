import pgzrun
from random import randint


TITLE = "Morbius: The Movie"

WIDTH = 500
HEIGHT = 500

message = ""



morbius = Actor('morbius')

def draw():
    #screen is another built in object
    screen.clear()
    screen.fill(color = (4, 0, 250))
    #place_morbius
    morbius.draw()
    screen.draw.text(message, center = (400, 10), fontsize = 30)

def place_morbius():
    morbius.x = randint(50,WIDTH-50)
    morbius.y = randint(50,WIDTH-50)

def on_mouse_down(pos):
    #print("Hello World!")
    global message
    if morbius.collidepoint(pos):
        message = "Let's Go"
        place_morbius()
    else:
        message = "No Go"


place_morbius()
pgzrun.go()