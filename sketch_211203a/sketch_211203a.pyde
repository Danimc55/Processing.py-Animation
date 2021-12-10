import random

smokeList = []
smokeListDel = []
smokeTimer=0
smokeMovementTimer=0
smokeDirection=0
smokeDirectionTimer=0
smokeDirectionSpeed=0

UFOList=[]
UFOListDel=[]
UFOTimer=0
UFOStop=0


textTimer=1
textX=350
textY=-300
textW=562
textH=202
textTimeOnScreen=0
textMovement=3
textSTOP=0

starTimer=1
starX=1200
starY=random.randint(0,200)
starSpeedTimer=0
starSpeedX=random.randint(10,20)
starSpeedY=1

windList=[]
windListDel=[]
windTimer=0
windStayTimer=0
windStayCounter=0

backgroundClick=0
clickTimer=0

cloudClick=0
cloudClickTimer=0

def smoke(X,Y,speed,movement):
    global smokeList,smokeListDel,smokeTimer,smokeMovementTimer,smokeDirection,smokeDirectionTimer,smokeDirectionSpeed
    fill(0)
    if(smokeDirection == 1):
        wind(-1)
    if(smokeDirection == 2):
        wind(1)
    quad(800,900,1100,900,1000,200,900,200)
    smokeTimer=(smokeTimer+1)%12
    if(smokeTimer==11):
        smokeList.append([950,200,X,Y,movement,smokeDirectionTimer,smokeDirectionSpeed])
    for el in smokeList:
        if(el[1]>0):
            fill(128,128,128)
            ellipse(el[0],el[1],el[2],el[3])
            if(smokeDirection == 1):
                el[1]-= speed/1
                el[0]-= el[6]
                el[5]=(el[5]+1)%10
                if(el[5]==9):
                   el[6]+=1
            elif(smokeDirection == 2):
                el[1]-= speed/1
                el[0]+= el[6]
                el[5]=(el[5]+1)%10
                if(el[5]==9):
                    el[6]+=1
            else:
                 el[1]-= speed
                 el[6]=0
            smokeMovementTimer=(smokeMovementTimer+1)%2
            if(smokeMovementTimer==0):
                el[0]+=movement
            
        else:
            smokeListDel.append(el)
    try:
        for el in smokeListDel:
            if(len(smokeListDel)!=0):
                smokeList.remove(el)
    except:
        pass

def UFOS(X,Y,direction,Ymove):
    global UFOList,UFOListDel,UFOTimer,UFOStop
    if(mousePressed and mouseButton == LEFT):
        STOP=1
    else:
        STOP=0
    if(STOP==0):
        UFOTimer=(UFOTimer+1)%120
    if(UFOTimer==119):
        UFOList.append([X,Y,direction,Ymove,Y+Ymove,0])
    for UFOS in UFOList:
        if(UFOS[1]>0):
            fill(128,128,128)
            ellipse(UFOS[0],UFOS[1],100,50)
            if(STOP==0):
                UFOS[0]+= UFOS[2]
                if(UFOS[4]<=UFOS[1] and UFOS[5]==0):
                    change=random.randint(20,60)
                    UFOS[4]=UFOS[1]-change
                    UFOS[5]=1
                if(UFOS[4]>=UFOS[1] and UFOS[5]==1):
                    change=random.randint(20,60)
                    UFOS[4]=UFOS[1]+change
                    UFOS[5]=0
                if(UFOS[4]>UFOS[1] and UFOS[5]==0):
                    UFOS[1]+=3
                if(UFOS[4]<UFOS[1] and UFOS[5]==1):
                    UFOS[1]-=3
        else:
            UFOListDel.append(UFOS)
    try:
        for UFOS in UFOListDel:
            if(len(UFOListDel)!=0):
                UFOList.remove(UFOS)
    except:
        pass

def text1():
    global textTimer,textX,textY,textW,textH,textTimeOnScreen,textMovement,textSTOP,textImg1,textImg2
    textImg1=loadImage("napis1.png")
    textImg2=loadImage("napis2.png")
    if(textSTOP==0):
        fill(255,255,255)
        rect(textX,textY,textW,textH)
        image(textImg1,textX,textY)
        textY+=textMovement
        if(textY>=200 and textMovement == 3 or textMovement==0):

            image(textImg2,textX,textY)
            textTimeOnScreen+=1
            textMovement=0
        if(textTimeOnScreen==300):
            textMovement=-3
            textTimeOnScreen =0
        if(textMovement==-3 and textY<=-300):
            textSTOP=1
            textMovement=3
            textTimer=1
            
def star():
    global starTimer,starX,starY,starSpeedTimer,starSpeedX,starSpeedY
    fill(255,255,0)
    ellipse(starX,starY,30,30)
    starX-=starSpeedX
    starY+=starSpeedY
    starSpeedTimer=(starSpeedTimer+1)%40
    if(starSpeedTimer==39):
        starSpeedY+=0.5
    if(starX<=-30):
        starX=1200
        starY=random.randint(0,200)
        starTimer=1
        starSpeedY=1
        starSpeedX=random.randint(10,20)
        
def keyPressed():
    global smokeDirection
    if (key == CODED):
        if (keyCode == LEFT):
            smokeDirection=1
    if  (key == CODED):
        if(keyCode == RIGHT):
            smokeDirection=2

def keyReleased():
    global smokeDirection
    smokeDirection=0

def backgroundTest():
    global backgroundClick,clickTimer
    if(mousePressed and mouseButton == LEFT):
        clickTimer+=1
    else:
        clickTimer=0
    if(clickTimer==1):
        backgroundClick=(backgroundClick+1)%2
    if(backgroundClick%2==0):
        fill(81,136,216)
        rect(0,0,1200,900)
        fill(255,255,0)
        ellipse(70,70,85,85)
    else:
        fill(24,41,64)
        rect(0,0,1200,900)
        fill(200,200,200)
        ellipse(70,70,85,85)

        
def oblak():
    global cloudClick,cloudClickTimer
    oblakImg1=loadImage("oblak.png")
    oblakImg2=loadImage("oblakD.png")
    if(mousePressed and mouseButton == LEFT):
        cloudClickTimer+=1
    else:
        cloudClickTimer=0
    if(cloudClickTimer==1):
        cloudClick=(cloudClick+1)%2
    if(cloudClick%2==0):
        image(oblakImg1,300,100,width/8, height/9)
        image(oblakImg1,600,120,width/8, height/9)
    else:
        image(oblakImg2,300,100,width/8, height/9)
        image(oblakImg2,600,120,width/8, height/9)
    

def wind(windDirection):
    global windList,windListDel,windTimer,windStayTimer,windStayCounter
    while(len(windList)!=30):
        windX=random.randint(10,120)*10
        windY=random.randint(10,70)*10
        windList.append([windX,windY,windStayTimer,windStayCounter])
    for el in windList:
        el[2]=(el[2]+1)%4
        if(el[2]==3):
            el[3]+=1
        if(el[3]>=0):
            point(el[0], el[1])
            point(el[0]+(windDirection*1), el[1])
            point(el[0],el[1]-1)
            point(el[0]+(windDirection*1), el[1]-1)
        if(el[3]>=1):
            point(el[0]+(windDirection*2), el[1])
            point(el[0]+(windDirection*3), el[1])
            point(el[0]+(windDirection*2),el[1]-1)
            point(el[0]+(windDirection*3), el[1]-1)
        if(el[3]>=2):
            point(el[0]+(windDirection*4), el[1])
            point(el[0]+(windDirection*5), el[1])
            point(el[0]+(windDirection*4),el[1]-1)
            point(el[0]+(windDirection*5), el[1]-1)
        if(el[3]>=3):
            point(el[0]+(windDirection*6), el[1])
            point(el[0]+(windDirection*7), el[1])
            point(el[0]+(windDirection*6),el[1]-1)
            point(el[0]+(windDirection*7), el[1]-1)
        if(el[3]>=4):
            point(el[0]+(windDirection*8), el[1])
            point(el[0]+(windDirection*9), el[1])
            point(el[0]+(windDirection*8),el[1]-1)
            point(el[0]+(windDirection*9), el[1]-1)
        if(el[3]>=5):
            point(el[0]+(windDirection*10), el[1])
            point(el[0]+(windDirection*11), el[1])
            point(el[0]+(windDirection*10),el[1]-1)
            point(el[0]+(windDirection*11), el[1]-1)
        if(el[3]>=6):
            point(el[0]+(windDirection*12), el[1]-2)
            point(el[0]+(windDirection*13), el[1]-2)
            point(el[0]+(windDirection*12),el[1]-3)
            point(el[0]+(windDirection*13), el[1]-3)
        if(el[3]>=7):
            point(el[0]+(windDirection*12), el[1]-4)
            point(el[0]+(windDirection*13), el[1]-4)
            point(el[0]+(windDirection*12),el[1]-5)
            point(el[0]+(windDirection*13), el[1]-5)
        if(el[3]>=8):     
            point(el[0]+(windDirection*10), el[1]-6)
            point(el[0]+(windDirection*11), el[1]-6)
            point(el[0]+(windDirection*10),el[1]-7)
            point(el[0]+(windDirection*11), el[1]-7)
        if(el[3]>=9):    
            point(el[0]+(windDirection*8), el[1]-5)
            point(el[0]+(windDirection*9), el[1]-5)
            point(el[0]+(windDirection*8),el[1]-4)
            point(el[0]+(windDirection*9), el[1]-4)
        if(el[3]>=10):
            windList=[]
        
def setup():
    size(1200,900)
    
def draw():
    global smokeTimer,textTimer,textSTOP,starX,starY,starTimer
    backgroundTest()

    smokeRandomWidth=random.randint(50,100)
    smokeRandomHeight=random.randint(40,80)
    smokeRandomSpeed=random.randint(1,5)
    smokeMovement=random.randint(-1,1)
    UFORandom=random.randint(0,1)
    UFOY=random.randint(100,300)
    if(UFORandom==1):
        UFOX=0
        UFODirection=6
    else:
        UFOX=1200
        UFODirection=-6
    UFOYMovement=random.randint(20,40)
    if(keyPressed and key=="k" or key == "K"):
        starTimer=0

    if(starTimer==0):
        star()
    smoke(smokeRandomWidth,smokeRandomHeight,smokeRandomSpeed,smokeMovement)
    oblak()
    UFOS(UFOX,UFOY,UFODirection,UFOYMovement)
    if(keyPressed and key=="n" or key == "N"):
        textTimer=0
    if(textTimer==0):
        textSTOP=0
        text1()
