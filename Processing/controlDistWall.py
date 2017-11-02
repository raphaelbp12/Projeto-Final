class ControlDistWall(object):
    def __init__(self, KpAng, KpLin, circuitWeight):
        self.KpAng = KpAng
        self.KpLin = KpLin
        self.circuitWeight = circuitWeight
        
    def controlAngVel(self, rightDist, leftDist):
        AngVelRight = 0
        AngVelLeft = 0
        
        if(rightDist <= self.circuitWeight/2):
            AngVelRight = self.KpAng*((self.circuitWeight/2) - rightDist)
        
        if(leftDist <= self.circuitWeight/2):
            AngVelLeft = self.KpAng*((self.circuitWeight/2) - leftDist)
        ret =  AngVelLeft - AngVelRight
        #print("rightDist = " + str(rightDist) + " leftDist = " + str(leftDist))
        #print("AngVelRight = " + str(AngVelRight) + " AngVelLeft = " + str(AngVelLeft))
        return ret
    
    def controlLinVel(self, frontDist):
        ret = self.KpLin * frontDist
        #print("lin = " + str(ret))
        return ret
        