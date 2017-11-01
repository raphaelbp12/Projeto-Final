class Sensors(object):
    def __init__(self):
        self.wallPoints = []
        
    def distance(self, pointA, pointB):
        return sqrt(pow(pointA[0] - pointB[0], 2)+pow(pointA[1] - pointB[1], 2))      
    
    def determinant(self, pointA, pointB):
        return pointA[0]*pointB[1]-pointA[1]*pointB[0]
    
    def sortByDist(self, item):
        return item[3]
    
    def isForward(self, theta, pointCar, pointA):
        theta = degrees(theta) % 360
        #print theta
        ret = False
        if theta < 90 and theta >= 0:
            if pointA[0] > pointCar[0] and pointA[1] >= pointCar[1]:
                ret = True 
        elif theta >= 90 and theta < 180:
            if pointA[0] <= pointCar[0] and pointA[1] > pointCar[1]:
                ret = True 
        elif theta >= 180 and theta < 270:
            if pointA[0] < pointCar[0] and pointA[1] <= pointCar[1]:
                ret = True 
        elif theta >= 270 and theta < 360:
            if pointA[0] >= pointCar[0] and pointA[1] < pointCar[1]:
                ret = True
        return ret
        
    def calcDistanceToWall(self, thetaInput, points, distMax, car):
        returnPoints = []
        
        for theta in [thetaInput, thetaInput + radians(90), thetaInput + radians(270)]:
            distPoints = []
            minDist = 800
            for twoWalls in points:
                for p in twoWalls:
                    coefAngVet = tan(p[2])
                    coefLinVet = p[1] -  coefAngVet*p[0]
                    a = tan(theta)
                    b = car.y - a*car.x
                    det = self.determinant([a,b],[coefAngVet, coefLinVet])
                    if det < 0:
                        det = det * -1.0
                    if det > exp(-5):
                        if coefAngVet != 0:
                            xVet = (coefLinVet - b)/(a - coefAngVet)
                            yVet = a * xVet + b
                            distVet = self.distance([xVet, yVet],[p[0], p[1]])
                            if distVet < distMax:
                                if self.isForward(theta, [car.x, car.y], [xVet, yVet]):
                                    distPoints.append([distVet, p, [xVet, yVet], self.distance([xVet, yVet], [car.x, car.y]), a, b])
                    #print "x1 = " + str(self.x) + " y1 = " + str(self.y) + " a1 = " + str(a) + " b1 = " + str(b) + " theta1 = " + str(degrees(theta))
                    #print "x2 = " + str(p[0]) + " y2 = " + str(p[1]) + " a2 = " + str(coefAngVet) + " b2 = " + str(coefLinVet) + " theta2 = " + str(degrees(p[2]))
                    #print "xVet = " + str(xVet) + " yVet = " + str(yVet)
                    #print "det = " + str(det) + " distVet = " + str(distVet)
                    #break
            distPoints.sort(key=self.sortByDist)
            if len(distPoints) > 0:
                returnPoints.append(distPoints[0])
        return returnPoints