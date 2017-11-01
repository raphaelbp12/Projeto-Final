from car import Car
from circuit import Circuit
from sensors import Sensors


def setup():
    global car, circuit, circuitDraw
    car = Car(600,400, 90)
    circuitDraw = createGraphics(800, 800)
    circuit = Circuit(80, color(0,0,100))
    circuit.circle(400, 400, 200, 70, 10)
    #circuit.lissajous(400, 400, 1, 2, 200, 200, 70, 10)
    circuit.display(circuitDraw)
    circuit.getTheta()
    size(800, 800)
    frameRate(1000)

def draw():
    background(0)
    noFill()
    stroke(255, 102, 0)
    image(circuitDraw, 0, 0)
    car.move(1,0.0051)
    textSize(16)
    text("Frame rate: " + str(int(frameRate)), 10, 20)
    text("x: " + str(int(car.x)), 10, 40)
    text("y: " + str(int(car.y)), 10, 60)
    text("theta: " + str((float(car.theta)/2/3.14*360)%360), 10, 80)
    text("dist Front: " + str(int(car.distFront)), 10, 100)
    text("dist Right: " + str(int(car.distRight)), 10, 120)
    text("dist Left: " + str(int(car.distLeft)), 10, 140)
    for p in car.sense(circuit.walls, 41):
        stroke(0,255,0)
        fill(0,255,0)
        ellipse(p[2][0],p[2][1],6,6)
    fill(255)
    car.display()