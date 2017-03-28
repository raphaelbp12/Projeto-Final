class Car(object):
    def __init__(self,x = 0,y = 0, theta = 0):
        self.x = x
        self.y = y
        self.theta = radians(theta)
        self.velLin = 0
        self.velAng = 0
        self.distanceFront = 0
        
    def pickColor(self, x, y):
        loadPixels()
        pixel = pixels[int(y)*width+int(x)]
        r = red(pixel)
        g = green(pixel)
        b = blue(pixel)
        return color(r,g,b)
        
    def isOnCircuit(self, x, y): 
        return self.pickColor(x,y) != color(0,0,0)
    
    def distance(self, pointA, pointB):
        return sqrt(pow(pointA[0] - pointB[0], 2)+pow(pointA[1] - pointB[1], 2))      
        
    def calcDistance(self, points):
        calcD = 800
        for p in points:
            newD = self.distance(p,[self.x, self.y])
            if newD < calcD:
                calcD = newD
        return calcD
    
    def determinant(self, pointA, pointB):
        return pointA[0]*pointB[1]-pointA[1]*pointB[0]
    
    def calcIntercept(self, theta, points, distMax):
        distPoints = []
        for p in points:
            coefAngVet = tan(p[2])
            coefLinVet = p[1] -  coefAngVet*p[0]
            a = tan(theta)
            b = self.y - a*self.x
            det = self.determinant([a,b],[coefAngVet, coefLinVet])
            if det < 0:
                det = det * -1.0
            if det > exp(-5):
                if coefAngVet != 0:
                    xVet = (coefLinVet - b)/(a - coefAngVet)
                    yVet = a * xVet + b
                    distVet = self.distance([xVet, yVet],[p[0], p[1]])
                    if distVet < distMax:
                        distPoints.append([distVet, p, [xVet, yVet]])
            #print "x1 = " + str(self.x) + " y1 = " + str(self.y) + " a1 = " + str(a) + " b1 = " + str(b) + " theta1 = " + str(degrees(theta))
            #print "x2 = " + str(p[0]) + " y2 = " + str(p[1]) + " a2 = " + str(coefAngVet) + " b2 = " + str(coefLinVet) + " theta2 = " + str(degrees(p[2]))
            #print "xVet = " + str(xVet) + " yVet = " + str(yVet)
            #print "det = " + str(det) + " distVet = " + str(distVet)
            #break
        return distPoints
                    
                
        
    def calcDistanceTheta(self, col, theta):
        projTheta = self.theta + radians(theta)
        projX = self.x
        projY = self.y
        ret = 0
        loadPixels()
        
        while True:
            if projX > 0 and projY > 0 and projX < width and projY < width:
                if self.pickColor(projX, projY) != col:
                    ret = self.distance([self.x, self.y], [projX, projY])
                    break
                else:
                    projX = projX + 5*cos(projTheta)
                    projY = projY + 5*sin(projTheta)
            else:
                ret = -1
                break
        return ret
        
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
        ellipse(self.x,self.y,20,20)