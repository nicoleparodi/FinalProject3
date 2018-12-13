add_library('minim')
import os
path = os.getcwd()
player = Minim(this)

class Creature():
    def __init__(self,x,y,r,g,img,w,h,F):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.vx=0
        self.vy=0
        self.w=w
        self.h=h
        self.F=F
        self.f=0
        self.img = img
        self.dir = 1

    

    def update(self):

        self.x += self.vx
        self.y += self.vy

   
    def display(self):
        self.update()
        
    #     if self.vx != 0:
    #         self.f = (self.f+0.3)%self.F

    #     if self.dir > 0:
    #         image(self.img,200,100,self.w,self.h)
    #     elif self.dir < 0:
    #         image(self.img,200,100,self.w,self.h,self.x,0,0,self.y) 

class Bird(Creature):
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN: False}
        
        self.Score = 0
        self.Lives = 3

    def update(self):
        if self.keyHandler[LEFT] == True:
      
            self.vx = -25
            self.dir = -1
            
        elif self.keyHandler[RIGHT] == True:
            self.vx = 20
            self.dir = 1
    
            
        elif self.keyHandler[UP] == True:
            self.vy = -20
   
            
        elif self.keyHandler[DOWN] == True:
            self.vy = 20
   
          #FIX THIS
        if  self.x in range(1025):
            self.x += self.vx 
        else: 
             pass   
            
        if self.y in range(550)
            self.y += self.vy
        else:
            pass



    # for b in g.basketballs:
    #         if self.distance(s) < self.r + s.r:
    #             g.basketballs.remove(b)
    #             del b
            
    #             self.Score += 1

    # for p in g.poolballs:
    #         if self.distance(s) < self.r + s.r:
    #             g.poolballs.remove(p)
    #             del p
            
    #             self.BallCnt += 1
                
    # for e in g.booklist:
    #         if self.distance(e) < self.r + e.r:
    #             # there is a collision with e
    #                 g.booklist.remove(e)
    #                 del e
    #                 self.Lives -= 1
                    
                
           # if self.Lives == 0: 
                    #g.__init__(1025,550,200)

    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
    
    def display (self):
        self.update()
        image(self.img,self.x,self.y)
        
        
class Book(Creature):#book is an enemie
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        
        self.x = random(g.w,g.w+20)
        self.y = random(g.h,g.h+20)
        
        self.vx = 
        self.vy = 
   



    def update(self):
        





class Ball():
    def __init__(self):
        self.x = x
        self.y = y
        self.r = r
    
        self.b = "no" #this will indicate whether the ball will bounce or not 


    def update(self):

   



class BB(Ball): #basketball
    def __init__(self):
        Ball.__init__(x,y,r,img,g,b)


    

class PB(Ball): #pool ball
    def __init__(self):
        Ball.__init__(x,y,r,img,g,b)


    def update(self):
        pass

    def display(self):
        pass


class Game():
    def __init__(self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.state = "menu"
        self.time = 0
        self.counter = 0
        
        self.birdimg = loadImage(path+"/images/blueparrot.png")
        self.bird = Bird(50,100,4,100,self.birdimg,16,12,2)


        self.booklist = [] # will add 2 different books to list
        # for b in range(3):
        #     self.booklist.append(Book(,,,,))
        # for c in range(3):
        #     self.booklist.append(Book2(,,,))

        self.basketballs = []
        # for i in range (3):
        #     self.basketballs.append(BB(,,,,))

        self.poolballs = []
        # for j in range (5):
        #     self.poolballs.append(PB) #- need to chose random ball either here or in class

    def display(self):
        print(self.time % 300)
        if 0 <= self.time % 300 <= 100:
            #display one image
            self.img = loadImage(path+"/images/BCKGROUND1.png")
            image(self.img,0,0,self.w, self.h)
        elif 101 <= self.time % 300 <= 200:
            #display one image 
            self.img = loadImage(path+"/images/BCKGROUND2.png")
            image(self.img,0,0,self.w, self.h)
        elif 201 <= self.time % 300 <= 300:
            #display one image 
            self.img = loadImage(path+"/images/BCKGROUND3.png")
            image(self.img,0,0,self.w, self.h)
    
   
            
        #scores
        fill(225)
        rect(0, 0, 180,50)
        textSize(24)
        fill(0)
        text("Score: " + str(self.bird.Score), 30, 35)
        
           #lives
        fill(225)   
        rect(400, 0, 150,50)
        textSize(24)
        fill(0)
        text("Lives: " + str(self.bird.Lives), 425, 35)
        
        
        #time
        fill(225)
        rect(800, 0, 150,50)
        textSize(24)
        fill(0)
        text("Time: " + str(self.time), 815, 35)
        
     
            

        for i in self.basketballs:
            i.display()
            pass

        for j in self.poolballs:
            j.display()
            pass

        for b in self.booklist:
            pass
            #randomize which ones are picked to be displayed
                
        self.bird.display()
                 
    def update(self):
        self.time += 1

#time aspect

g = Game(1025,550,200)
         
def setup():
    size(g.w,g.h)
    background(0)

def draw():
    g.update()
    if g.state == 'menu':
        g.display()
        # background(0)
        textSize(30)
        fill(255)
        # code for the choices 
        
    elif g.state == 'play':
        pass

    #box for the time
    #box for the books collected 


    #pass

def mouseClicked():
    #YASIRS CODE: if g.state == "menu" and g.w//2.5 < mouseX < g.w//2.5 + 220 and g.h//3 < mouseY < g.h//3+50:
        #g.state="play"
    #need coordinates if clicked in box of play then will play
    # if g.state == 'menu' and and : # between ands are rectangle
    #     g.state = "play" #reassigning the state to play

    pass

def keyPressed():
    if keyCode == LEFT:
        g.bird.keyHandler[LEFT]=True
    elif keyCode == RIGHT:
        g.bird.keyHandler[RIGHT]=True
    elif keyCode == UP:
        g.bird.keyHandler[UP]=True
    elif keyCode == DOWN:
        g.bird.keyHandler[DOWN]= True

def keyReleased():
    if keyCode == LEFT:
        g.bird.keyHandler[LEFT]=False
    elif keyCode == RIGHT:
        g.bird.keyHandler[RIGHT]=False
    elif keyCode == UP:
        g.bird.keyHandler[UP]=False
    elif keyCode == DOWN:
        g.bird.keyHandler[DOWN]= False
