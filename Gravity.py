from Tkinter import *
from math import *
import time, random
root = Tk()
canvas = Canvas(root, width = 700, height = 700)
canvas.pack()


class Particle ():
    def __init__(self, mass, colour, positionX, positionY, velX, velY, r, accX, accY):
        self.mass = mass
        self.colour = colour
        self.positionX = positionX
        self.positionY = positionY
        self.radius = r
        self.velX  = velX
        self.velY = velY
        self.accX = accX
        self.accY = accY
    def draw(self):
        canvas.create_oval((self.positionX - self.radius), (self.positionY - self.radius), (self.positionX+self.radius), (self.positionY+self.radius), fill = self.colour)
    def getAcceleration(self,x,y):
        dx = self.positionX - x
        dy = self.positionY - y

        rads = atan2(-dy,dx)
        rads %= 2*pi
        r = sqrt(((dx)**2) + ((dy)**2))
        self.accX = -40000*(cos(rads))/(r**2)
        self.accY = 40000*(sin(rads))/(r**2)
       
    def getX(self):
        return self.positionX
    def getY(self):
        return self.positionY
        
    def move(self):
        self.velX += self.accX
        self.velY += self.accY
        self.positionX += self.velX
        self.positionY += self.velY
        
        if (self.positionY>=700 or self.positionY <= 0):
            self.velY *= -0.5
        if (self.positionX >=700 or self.positionX <= 0):
            self.velX *= -0.5
        
        
            

def main():
    particles = []
    for i in range(0, 25):
        x = random.randint(0,700)
        y = random.randint(0,700)
        v = random.randint(-10,10)
        vy = random.randint(-10,10)
        particle = Particle(5, "purple", x, y,v,vy,5,0,0)
        particles.append(particle)
        blob = Particle(1, "dark green",350,350,0,0,5,0,0)
    
    while True:
        
        time.sleep(0.03)        
        canvas.delete("all")
        blob.move()
        blob.draw()
        for i in range (0, len(particles)):
            
            particles[i].getAcceleration(blob.getX(),blob.getY())
            particles[i].move()
            particles[i].draw()
            
        canvas.update()
        
    
    mainloop()
    
    
main()




