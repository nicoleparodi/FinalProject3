add_library('sound')
add_library('minim')

import os, random
path = os.getcwd()
player = Minim(this)

#PFont font 

class Creature():
    def __init__(self,x,y,r,gr,img,w,h,F,vx=0,vy=0):
        self.x=x
        self.y=y
        self.r=r
        self.gr=gr
        self.vx=vx
        self.vy=vy
        self.w=w
        self.h=h
        self.F=F
        self.f=0
        self.img = img
        self.dir = 1

    def update(self):

        self.x += self.vx
        self.y += self.vy
        if self.x > g.w:
            self.x = 0
        if self.x < 0:
            self.x = g.w
        if self.y > g.h:
            self.y = 0
        if self.y < 0:
            self.y = g.h
        
    def display(self):
        self.update()
        image(self.img,self.x,self.y)


        if self.dir > 0:
            image(self.img,200,100,self.w,self.h)
        elif self.dir < 0:
            image(self.img,200,100,self.w,self.h,self.x,0,0,self.y) 
        # stroke(255)
        # noFill()
        # strokeWeight(5)
        # ellipse(self.x + self.r, self.y + self.r, 2 * self.r, 2 * self.r)

class Bird(Creature):
    def __init__(self,x,y,r,gr,img,w,h,F):
        Creature.__init__(self,x,y,r,gr,img,w,h,F,vx=0,vy=0)
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

        # detect collision with basketballs
        for b in g.basketballs:
            if self.distance(b) < self.r + b.r:
                print('collidee')
                g.basketballs.remove(b)
                del b
                
                self.Score += 20
    
        for p in g.drinks:
            
            if self.distance(p) < self.r + p.r:
                print('collide w drinks')
                g.drinks.remove(p)
                del p
                
                self.Score += 10

        for e in g.booklist:
            print ('Book: ' + str(self.distance(e)) + " " +str(self.r + e.r))
            print ("The xspeed is" + str(e.vx))
            print ("The xspeed is" + str(e.vy))
            if self.distance(e) < self.r + e.r:
                # there is a collision with e
                g.booklist.remove(e)
                del e
                self.Lives -= 1
                        
                    
        if self.Lives == 0: 
            g.state = 'lost'
            g.tRtime = False
        
            

    def distance (self,e):
        return (((self.x + self.r - e.x - e.r)**2+(self.y + self.r - e.y - e.r)**2)**0.5)
    
    def display (self):
        self.update()
        image(self.img,self.x,self.y)        
        # stroke(255)
        # noFill()
        # strokeWeight(5)
        # ellipse(self.x + self.r, self.y + self.r, 2 * self.r, 2 * self.r)
        
class Book(Creature):#book is an enemie
    def __init__(self,r,img,w,h,F,vx,vy):
        
        
        self.offset = 20
        x = random.randint(-self.offset,g.w+self.offset)
        y = random.randint(-self.offset,g.h+self.offset)
        
        while x in range(g.w) and y in range(g.h):
            x = random.randint(-self.offset,g.w+self.offset)
            y = random.randint(-self.offset,g.h+self.offset)
            
        gr = 0
        
        Creature.__init__(self,x,y,r,gr,img,w,h,F,vx,vy)
        
        # self.vx = random.randint(-50,5)
        # self.vy = random.randint(-50,5)
   

        


class B_Ball(Creature):
     def __init__(self,r,img,w,h,F,vx,vy):
        
        self.offset = 20
        x = random.randint(-self.offset,g.w+self.offset)
        y = random.randint(-self.offset,g.h+self.offset)
        
        while x in range(g.w) and y in range(g.h):
            x = random.randint(-self.offset,g.w+self.offset)
            y = random.randint(-self.offset,g.h+self.offset)
            
        gr = 0
        
        Creature.__init__(self,x,y,r,gr,img,w,h,F)
        
        
        self.vx = random.randint(-30,20)
        self.vy = random.randint(-30,15)

class CapriSun(Creature): 
      def __init__(self,r,img,w,h,F,vx,vy):
        
        self.offset = 20
        x = random.randint(-self.offset,g.w+self.offset)
        y = random.randint(-self.offset,g.h+self.offset)
        
        while x in range(g.w) and y in range(g.h):
            x = random.randint(-self.offset,g.w+self.offset)
            y = random.randint(-self.offset,g.h+self.offset)
            
        gr = 0
        
        Creature.__init__(self,x,y,r,gr,img,w,h,F)
        
        
        self.vx = random.randint(-30,15)
        self.vy = random.randint(-20,15)

class Game():
    def __init__(self,w,h,gr):
        self.w=w
        self.h=h
        self.gr=gr
        self.state = "menu"
        self.tRtime = True
        self.time = 0
        self.counter = 0
    #self.music = SoundFile(this,path+'chase.mp3')
        self.pause = False 
    #self.pauseSound = SoundFile(this,path+'pause.mp3')
        self.birdimg = loadImage(path+"/images/bird2.png")
        self.bookimg = loadImage(path+"/images/book2.png")
        self.b_ballimg = loadImage(path+"/images/bball.png")
        self.caprisunimg = loadImage(path+"/images/caprisun1.png")
        
        
    def CreateGame(self):
        self.bird = Bird(50,100,50,100,self.birdimg,16,12,2)


        self.booklist = [] # will add 2 different books to list
        self.drinks = []  
        self.basketballs = []
              
        for b in range(7):
            vx = random.randint(-30,20)
            vy = random.randint(-30,15)
            self.booklist.append(Book(50,self.bookimg,10,10,2,vx, vy))
             
        for i in range (7):
            vx = random.randint(-30,20)
            vy = random.randint(-30,15)
            self.basketballs.append(B_Ball(20,self.b_ballimg,10,10,2,vx,vy))

        for j in range (7):
            vx = random.randint(-30,20)
            vy = random.randint(-30,15)
            self.drinks.append(CapriSun(20,self.caprisunimg,10,10,2,vx,vy))


    def display(self):

            
        if g.state == 'play':
            print('game.display state:play', self.time % 300)
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
        
        font =loadFont("Courier-28.vlw");
        
        fill(224,224,224)
        rect(0, 0, 180,50)
        textFont(font)
        textSize(24)
        fill(0)
        text("Score: " + str(self.bird.Score), 30, 35)
        
        #lives
        fill(224,224,224)   
        rect(400, 0, 150,50)
        textFont(font)
        textSize(24)
        fill(0)
        text("Lives: " + str(self.bird.Lives), 424, 35)
        
    
        #time
        fill(224,224,224)
        rect(800, 0, 150,50)
        textFont(font)
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
        if self.pause == False and g.tRtime == True and g.state == 'play':
            self.time += 1
        
        if self.time == 300:
            g.state = 'done'
            self.totalscore = self.bird.Score
            
            
            



g = Game(1025,550,200)
         
def setup():
    size(g.w,g.h)
    background(0)
    g.CreateGame()
    

def draw():
    font =loadFont("Courier-28.vlw");
    g.update()
    print(g.state)
    if g.state == 'menu':
        #g.display()
        background(0)
        textFont(font)
        textSize(30)
        if g.state == "menu" and g.w//2.5 < mouseX < g.w//2.5 + 220 and g.h//3 < mouseY < g.h//3+50:
            fill(102,178,225)
        else:
            fill(225)
        textFont(font)
        text(" PLAY GAME ", g.w//2.5+10, g.h//3+40)
            
        fill(225)
        textFont(font)
        text(" How to play: Avoid the books and collect the other\n \t  \t objects to score points before it gets dark!\n P.S: Use the arrow keys to control the bird!", 70, g.h//3+140)
        
            
    elif g.state == 'play':
        if not g.pause:
            background(0)
            print(' play display')
            g.display()
        else:
            fill(102,102,255)
            textSize(30)
            textFont(font)
            text("Paused.", 450, g.h//2)
            
    elif g.state == 'lost':
        background(0)
        textFont(font)
        textSize(30)
        fill(255,0,0)
        text("Game Over! You Lost!", 350, g.h//2)
  
        
            
    elif g.state == 'done':
        background(0)
        textFont(font)
        textSize(30)
        fill(128,255,0)
        text("\t Game Over!\n Your score: " + str(g.totalscore), 350, g.h//2)
    
    
   


def mouseClicked():
 if g.state == "menu" and g.w//2.5 < mouseX < g.w//2.5 + 220 and g.h//3 < mouseY < g.h//3+50:
        g.time = 0
        #g.music.play()
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
        
        # g.pauseSound.rewind()
        # g.pauseSound.play()
  
        
   
  
        
        #     g.music.pause()
            
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
