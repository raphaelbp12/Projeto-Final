from sensors import Sensors

class Car(object):
    def __init__(self,x = 0,y = 0, theta = 0):
        self.x = x
        self.y = y
        self.theta = radians(theta)
        self.velLin = 0
        self.velAng = 0
        self.distFront = 0
        self.distRight = 0
        self.distLeft = 0
        self.sensors = Sensors()
        
    def sense(self, wallsPoints, maxDist):
        retPoints = []
        for p in self.sensors.calcDistanceToWall(self.theta, wallsPoints, maxDist, self):
            retPoints.append(p)
        if len(retPoints) == 3:
            self.distFront = retPoints[0][3]
            self.distRight = retPoints[1][3]
            self.distLeft = retPoints[2][3]
        return retPoints
        
        
    def move(self, velLin, velAng):
        self.velLin = velLin
        self.velAng = velAng
        self.theta = self.theta + velAng
        self.x = self.x + velLin*cos(self.theta)
        self.y = self.y + velLin*sin(self.theta)
        #print "x = "+str(self.x)+" y = "+str(self.y)+" theta = "+ str(self.theta) +" velLin = "+str(velLin)+" velAng = "+str(velAng)
        
    def display(self):
        stroke(255,0,0)
        velLin = self.velLin
        if velLin < 30:
            velLin = 30
        line(self.x, self.y, self.x+velLin*cos(self.theta), self.y+velLin*sin(self.theta))
        fill(255)
        ellipse(self.x,self.y,10,10)