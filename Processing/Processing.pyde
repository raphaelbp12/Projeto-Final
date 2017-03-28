from car import Car
from circuit import Circuit


def setup():
    global car, circuit, circuitDraw
    car = Car(400,400, 120)
    circuitDraw = createGraphics(800, 800)
    circuit = Circuit(50, color(0,0,100))
    #circuit.circle(400, 400, 200, 400, 1)
    circuit.lissajous(400, 400, 1, 2, 200, 200, 70, 10)
    circuit.display(circuitDraw)
    circuit.getTheta()
    size(800, 800)
    frameRate(1000)

def draw():
    background(0)
    noFill()
    stroke(255, 102, 0)
    image(circuitDraw, 0, 0)
    car.move(1,0.03)
    if not car.isOnCircuit(car.x, car.y):
        textSize(25)
        #text("FORA DA PISTA", width/2, height/2)
    textSize(16)
    text("Frame rate: " + str(int(frameRate)), 10, 20)
    text("x: " + str(int(car.x)), 10, 40)
    text("y: " + str(int(car.y)), 10, 60)
    text("theta: " + str((float(car.theta)/2/3.14*360)%360), 10, 80)
    #text("dist Front: " + str(car.calcDistanceTheta(circuit.col, 0)), 10, 100)
    #text("dist Right: " + str(car.calcDistanceTheta(circuit.col, 90)), 10, 120)
    #text("dist Left: " + str(car.calcDistanceTheta(circuit.col, 270)), 10, 140)
    text("newD: " + str(car.calcDistance(circuit.points)), 10, 160)
    for p in car.calcIntercept(car.theta, circuit.pointsWithTheta, 90):
        stroke(0,255,0)
        fill(0,255,0)
        ellipse(p[1][0],p[1][1],6,6)
        line(p[1][0], p[1][1], p[1][0]+90*cos(p[1][2]), p[1][1]+90*sin(p[1][2]))
        stroke(255,0,0)
        fill(255,0,0)
        ellipse(p[2][0],p[2][1],6,6)
    fill(255)
    car.display()