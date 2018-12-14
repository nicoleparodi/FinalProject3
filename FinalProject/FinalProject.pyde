add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)

class Creature():
    def __init__(self,x,y,r,gr,img,w,h,F):
        self.x=x
        self.y=y
        self.r=r
        self.gr=gr
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
        image(self.img,self.x,self.y)


        if self.dir > 0:
            image(self.img,200,100,self.w,self.h)
        elif self.dir < 0:
            image(self.img,200,100,self.w,self.h,self.x,0,0,self.y) 

class Bird(Creature):
    def __init__(self,x,y,r,gr,img,w,h,F):
        Creature.__init__(self,x,y,r,gr,img,w,h,F)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN: False}
        
        self.Score = 0
        self.Lives = 3

    def update(self):
        if self.keyHandler[LEFT] == True:
            self.vx = -30
            
        elif self.keyHandler[RIGHT] == True:
            self.vx = 30
        
        else:
            self.vx = 0
        
            
        if self.keyHandler[UP] == True:
            self.vy = -30
            
        elif self.keyHandler[DOWN] == True:
            self.vy = 30
        
        else:
            self.vy = 0
   
        if  self.x in range(1025):
            self.x += self.vx 
        else: 
             self.x = 50   
            
        if self.y in range(550):
            self.y += self.vy
        else:
            self.y = 50


        for b in g.basketballs:
                if self.distance(b) < self.r + b.r:
                    g.basketballs.remove(b)
                    del b
                
                    self.Score += 1
    
        for p in g.drinks:
                if self.distance(p) < self.r + p.r:
                    g.drinks.remove(p)
                    del p
                
                    self.Score += 1
                    
        for e in g.booklist:
                if self.distance(e) < self.r + e.r:
                    # there is a collision with e
                        g.booklist.remove(e)
                        del e
                        self.Lives -= 1
                        
                    
        if self.Lives == 0: 
            g.__init__(1025,550,200)

    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
    
    def display (self):
        self.update()
        image(self.img,self.x,self.y)        
        
class Book(Creature):#book is an enemie
    def __init__(self,r,img,w,h,F):
        
        self.offset = 20
        x = random.randint(-self.offset,g.w+self.offset)
        y = random.randint(-self.offset,g.h+self.offset)
        
        while x in range(g.w) and y in range(g.h):
            x = random.randint(-self.offset,g.w+self.offset)
            y = random.randint(-self.offset,g.h+self.offset)
            
        gr = 0
        
        Creature.__init__(self,x,y,r,gr,img,w,h,F)
        
        
        self.vx = random.randint(-50,10)
        self.vy = random.randint(-50,10)
   

        


class B_Ball(Creature):
     def __init__(self,r,img,w,h,F):
        
        self.offset = 20
        x = random.randint(-self.offset,g.w+self.offset)
        y = random.randint(-self.offset,g.h+self.offset)
        
        while x in range(g.w) and y in range(g.h):
            x = random.randint(-self.offset,g.w+self.offset)
            y = random.randint(-self.offset,g.h+self.offset)
            
        gr = 0
        
        Creature.__init__(self,x,y,r,gr,img,w,h,F)
        
        
        self.vx = random.randint(-10,10)
        self.vy = random.randint(-10,10)

    

    

class CapriSun(Creature): #pool ball
      def __init__(self,r,img,w,h,F):
        
        self.offset = 20
        x = random.randint(-self.offset,g.w+self.offset)
        y = random.randint(-self.offset,g.h+self.offset)
        
        while x in range(g.w) and y in range(g.h):
            x = random.randint(-self.offset,g.w+self.offset)
            y = random.randint(-self.offset,g.h+self.offset)
            
        gr = 0
        
        Creature.__init__(self,x,y,r,gr,img,w,h,F)
        
        
        self.vx = random.randint(-10,10)
        self.vy = random.randint(-10,10)

class Game():
    def __init__(self,w,h,gr):
        self.w=w
        self.h=h
        self.gr=gr
        self.state = "menu"
        self.time = 0
        self.counter = 0
        
        self.pause = False 
        
        self.birdimg = loadImage(path+"/images/bird2.png")
        self.bookimg = loadImage(path+"/images/book2.png")
        self.b_ballimg = loadImage(path+"/images/basketball.png")
        self.caprisunimg = loadImage(path+"/images/caprisun.png")
        
        
    def CreateGame(self):
        self.bird = Bird(50,100,4,100,self.birdimg,16,12,2)


        self.booklist = [] # will add 2 different books to list
        self.drinks = []  
        self.basketballs = []
              
        for b in range(40):
             self.booklist.append(Book(2,self.bookimg,10,10,2))
   

       
        for i in range (15):
            self.basketballs.append(B_Ball(2,self.b_ballimg,10,10,2))

      
        for j in range (25):
            self.drinks.append(CapriSun(2,self.caprisunimg,10,10,2))


    def display(self):
        while g.state == 'play':
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
            

        for j in self.drinks:
            j.display()
  

        for b in self.booklist:
            b.display()
                
        self.bird.display()
                 
    def update(self):
        self.time += 1



g = Game(1025,550,200)
         
def setup():
    size(g.w,g.h)
    background(0)
    g.CreateGame()
    

def draw():
    g.update()
    if g.state == 'menu':
        #g.display()
        background(0)
        textSize(30)
        if g.state == "menu" and g.w//2.5 < mouseX < g.w//2.5 + 220 and g.h//3 < mouseY < g.h//3+50:
            fill(0,128,225)
        else:
            fill(225)
            text(" PLAY GAME ", g.w//2.5+10, g.h//3+40)
            
        fill(225)
        text(" How to play: Avoid the books and collect the other objects\n \t \t  to score points before it gets dark!", 70, g.h//3+140)
        
            
    elif g.state == 'play':
        if not g.pause:
            background(0)
            g.display()
        else:
            fill(225,0,0)
            textSize(30)
            text("Paused.", g.w//2, g.h//2)

   


def mouseClicked():
 if g.state == "menu" and g.w//2.5 < mouseX < g.w//2.5 + 220 and g.h//3 < mouseY < g.h//3+50:
        g.state="play"




def keyPressed():
    if keyCode == LEFT:
        g.bird.keyHandler[LEFT]=True
    elif keyCode == RIGHT:
        g.bird.keyHandler[RIGHT]=True
    elif keyCode == UP:
        g.bird.keyHandler[UP]=True
    elif keyCode == DOWN:
        g.bird.keyHandler[DOWN]= True
        
    elif keyCode == 32:
        g.pause = not g.pause

def keyReleased():
    if keyCode == LEFT:
        g.bird.keyHandler[LEFT]=False
    elif keyCode == RIGHT:
        g.bird.keyHandler[RIGHT]=False
    elif keyCode == UP:
        g.bird.keyHandler[UP]=False
    elif keyCode == DOWN:
        g.bird.keyHandler[DOWN]= False
