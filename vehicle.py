class Car:
    tracks=[]
    def __init__(self,i,xi,yi,max_value):
        self.i=i
        self.x=xi
        self.y=yi
        self.tracks=[]
        self.completed=False
        self.state='0'
        self.count=0
        self.max_value=max_value
        
    def getTracks(self):
        return self.tracks


    def getState(self):
        return self.state


    def getX(self): 
        return self.x

    def getY(self):
        return self.y

    def updateCoords(self, xn, yn):
        self.count = 0
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn

    def setComplete(self):
        self.completed = True

    def timeOut(self):
        return self.completed

    def moving(self,mid_start):
        if len(self.tracks)>=2:
            if self.state=='0':
                if self.tracks[-1][1]>mid_start and self.tracks[-2][1]<=mid_start:
                    self.state = '1'
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def increment_value(self):
        self.count+=1
        if self.count>self.max_value:
            self.completed=True
        return  True