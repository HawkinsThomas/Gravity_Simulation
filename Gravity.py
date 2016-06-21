from Tkinter import *
from math import *
import time, random
root = Tk()
canvas = Canvas(root, width = 1000, height = 600, background ='black')
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
        self.accX = -1100*(cos(rads))/(r**2)
        self.accY = 1100*(sin(rads))/(r**2)
       
    def getX(self):
        return self.positionX
    def getY(self):
        return self.positionY
        
    def move(self):
        self.velX += self.accX
        self.velY += self.accY
        self.positionX += self.velX
        self.positionY += self.velY
        
        if (self.positionY>=1080 or self.positionY <= 0):
            self.velY *= -0.7
        if (self.positionX >=1920 or self.positionX <= 0):
            self.velX *= -0.7
        
        
            

def main():
    colours = ["gray", "light gray", "dark gray", "white", "light yellow", "light blue", "beige"]
    particles = []
    for i in range(0, 40):
        #x = random.randint(0,1920)
        x = 590 + random.randint(0,200)*0.1
        y = 300
        v = random.randint(2,5) * 0.3
        vy = random.randint(900,1000)* -0.003
        particle = Particle(5, colours[i%len(colours)], x, y,v,vy,2,0,0)
        particles.append(particle)
        blob = Particle(1, "orange",500,300,0,0,10,0,0)
    
    while True:
        
        time.sleep(0.02)        
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




