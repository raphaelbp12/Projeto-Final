class Circuit(object):
    def __init__(self, circuitWeight, col):
        self.points = []
        self.pointsWithTheta = []
        self.circuitWeight = circuitWeight
        self.col = col
        
    def circle(self, x, y, radius, steps, interval):
        #interval = the amount that X increment
        theta = 0
        
        for i in range(steps):
            self.points.append([int(x+radius*cos(theta)), int(y+radius*sin(theta))])
            theta = theta + radians(interval)
        #print self.points
        
    def distance(self, pointA, pointB):
        ret = sqrt(pow(pointA[0] - pointB[0], 2)+pow(pointA[1] - pointB[1], 2))  
        #print [pointA, pointB, ret]
        return ret
    
    def lissajous(self, x, y, kx, ky, a, b, steps, interval):
        #interval = the amount that X increment
        theta = 0
        
        for i in range(steps):
            self.points.append([int(x+a*cos(kx*theta)), int(y+b*sin(ky*theta))])
            theta = theta + radians(interval)
        #print self.points
        
    def getTheta(self):
        for i in range(len(self.points)):
            #print i
            if i < (len(self.points)-1):
                mod = self.distance(self.points[i],self.points[i+1])
                if mod != 0:
                    theta = atan2((self.points[i+1][1]-self.points[i][1]),(self.points[i+1][0]-self.points[i][0]))
                    #print [self.points[i],self.points[i+1], degrees(theta)]
                else:
                    theta = 0
                self.pointsWithTheta.append(self.points[i]+[theta])
        #print self.pointsWithTheta        
                            
    def display(self, circDraw):
        circDraw.beginDraw()
        circDraw.noFill()
        circDraw.strokeWeight(self.circuitWeight)
        circDraw.stroke(self.col)
        circDraw.beginShape();
        circDraw.curveVertex(self.points[0][0], self.points[0][1])
        for point in self.points:
            circDraw.curveVertex(point[0], point[1])
        circDraw.curveVertex(self.points[-1][0], self.points[-1][1])
        circDraw.endShape()
        circDraw.endDraw()