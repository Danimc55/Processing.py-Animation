import random
import math 

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
textX=250
textY=-300
textW=757
textH=97
textTimeOnScreen=0
textMovement=3
textSTOP=0

starTimer=1
starX=1200
starY=random.randint(0,200)
starSpeedTimer=0
starSpeedX=random.randint(10,20)
starSpeedY=-1

windList=[]
windListDel=[]
windTimer=0
windStayTimer=0
windStayCounter=0

backgroundClick=0
clickTimer=0

cloudClick=0
cloudClickTimer=0

fireWorkTimer=0
fireWorkList=[]
fireWorkLengthTimer=0
fireWorkExplodeTimer=0
fireWorkLineList=[]
fireWorkWork=0
randomFire=0
randomFireStop=0

prometejTimer=0
prometejState=0


def smoke(X,Y,speed,movement):
    global smokeList,smokeListDel,smokeTimer,smokeMovementTimer,smokeDirection,smokeDirectionTimer,smokeDirectionSpeed
    fill(0)
    if(smokeDirection == 1):
        wind(-1)
    if(smokeDirection == 2):
        wind(1)
    quad(800-325,900-75,1100-375,900-75,1000-350,200,900-350,200)
    smokeTimer=(smokeTimer+1)%12
    if(smokeTimer==11):
        smokeList.append([950-350,200,X,Y,movement,smokeDirectionTimer,smokeDirectionSpeed])
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
        UFOR=random.randint(0,255)
        UFOG=random.randint(0,255)
        UFOB=random.randint(0,255)
        UFOList.append([X,Y,direction,Ymove,Y+Ymove,0,UFOR,UFOG,UFOB])
    for UFOS in UFOList:
        if(UFOS[1]>0):
            fill(UFOS[6],UFOS[7],UFOS[8])
            ellipse(UFOS[0],UFOS[1]-30,50,75)
            fill(UFOS[7],UFOS[8],UFOS[6])
            ellipse(UFOS[0],UFOS[1],100,50)
            fill(UFOS[8],UFOS[6],UFOS[7])
            ellipse(UFOS[0],UFOS[1]+5,15,15)
            ellipse(UFOS[0]-25,UFOS[1]-5,15,15)
            ellipse(UFOS[0]+25,UFOS[1]-5,15,15)
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

def znakSTPS():
    global logo
    fill(57,57,56)
    rect(164,740,22,75)
    fill(121,65,0)
    rect(77,647,194,92)
    image(logo, 106, 659)

def text1():
    global textTimer,textX,textY,textW,textH,textTimeOnScreen,textMovement,textSTOP,textImg1,textImg2
    if(textSTOP==0):
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
    starSpeedTimer=(starSpeedTimer+1)%30
    if(starSpeedTimer==29):
        starSpeedY+=1
    if(starX<=-30):
        starX=1200
        starY=random.randint(0,200)
        starTimer=1
        starSpeedY=-1
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
        image(backgroundImg2,0,0)
        fill(200,200,200)
        ellipse(70,70,85,85)
        
    else:
        image(backgroundImg1,0,0)
        fill(255,255,0)
        ellipse(70,70,85,85)
    
def platforma():
    if(mousePressed and mouseButton == LEFT):
        fill(54,110,43)
    else:
        fill(91,187,71)
    ellipseMode(CORNER)
    ellipse(27,784,298,65)
    ellipse(395,772,410,90)
    ellipse(875,784,298,65)
    ellipseMode(CENTER)
    
def oblak():
    global cloudClick,cloudClickTimer,prometejTimer,prometejState,prometejImg1,prometejImg2,prometejImg3,oblakImg1, oblakImg2
    if(mousePressed and mouseButton == LEFT):
        image(oblakImg2,300,100,width/8, height/9)
        image(oblakImg2,800,120,width/8, height/9)
        prometejTimer=(prometejTimer+1)%60
        if(prometejTimer==59):
            prometejState+=1
        if(prometejState%2==0):
            image(prometejImg2,921,500)
        else:
            image(prometejImg3,921,500)
    else:
        image(oblakImg1,300,100,width/8, height/9)
        image(oblakImg1,800,120,width/8, height/9)
        image(prometejImg1,921,500)
    

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
            
def fireWork():
    global fireWorkTimer,fireWorkList,fireWorkLengthTimer,fireWorkExplodeTimer,fireWorkWork,randomFire,randomFireStop
    fireWorkTimer=(fireWorkTimer+1)%60
    strokeWeight(3);
    if(fireWorkTimer%60==59 and randomFire-1>randomFireStop):
        fireWorkLineX1=random.randint(200,1000)
        fireWorkLineY1=900
        fireWorkExplodeY=random.randint(200,500)
        fireWorkSize=2
        fireWorkRandomBoom=random.randint(10,20)*2
        fireWorkSplit=math.pi/fireWorkRandomBoom
        cosX=0
        sinY=0
        fireWorkLength=0
        fireR=random.randint(0,255)
        fireG=random.randint(0,255)
        fireB=random.randint(0,255)
        fireWorkX2=0
        fireWorkY2=0
        fireWorkX3=0
        fireWorkY3=0
        fireWorkList.append([fireWorkLineX1,fireWorkLineY1,fireWorkSize,fireWorkRandomBoom,fireWorkSplit,cosX,sinY,fireWorkExplodeY,fireWorkExplodeTimer,fireWorkLength,fireR,fireG,fireB,fireWorkX2,fireWorkY2,0,fireWorkX3,fireWorkY3,0,0,0,0,0])
    for fire in fireWorkList:
        if(fire[1]<=fire[7]):
            fire[8]+=1
        else:
            line(fire[0],fire[1],fire[0],fire[1]+10)
            fire[1]-=10
        if(fire[8]>=1):
            fire[5]=0
            fire[6]=0
            fire[18]+=0.5
            fire[19]+=1
            fire[20]+=1.5
            fire[21]+=2
            fire[22]+=3
            for j in range(fire[3]):
                if(fireWorkLengthTimer%3==0):
                    stroke(fire[10],fire[11],fire[12])
                elif(fireWorkLengthTimer%3==1):
                    stroke(fire[12],fire[10],fire[11])
                else:
                    stroke(fire[11],fire[12],fire[10])
                    stroke(255-fire[10],255-fire[11],255-fire[12])
                fire[9]=1
                fireWorkLengthTimer=(fireWorkLengthTimer+1)%3
                fire[5]+=fire[4]*2
                fire[6]+=fire[4]*2
                fireWorkCos=math.cos(fire[5])
                fireWorkSin=math.sin(fire[6])
                fireWorkRandomSpeed=random.randint(1,5)
                if(fireWorkRandomSpeed==1):
                    fire[15]=fire[18]
                elif(fireWorkRandomSpeed==2):
                    fire[15]=fire[19]
                elif(fireWorkRandomSpeed==3):
                    fire[15]=fire[20]
                elif(fireWorkRandomSpeed==4):
                    fire[15]=fire[21]
                else:
                    fire[15]=fire[22]
                fire[13]=fireWorkCos*(fire[2]+fire[15])*fire[9]+fire[0]
                fire[14]=fireWorkSin*(fire[2]+fire[15])*fire[9]+fire[1]
                fire[16]=fireWorkCos*(fire[2]+fire[15]-3)*fire[9]+fire[0]
                fire[17]=fireWorkSin*(fire[2]+fire[15]-3)*fire[9]+fire[1]
                line(fire[16],fire[17],fire[13],fire[14])
                
        if(fire[8]==60):
            randomFireStop+=1
            fireWorkList.remove(fire)
                
def setup():
    global prometejImg1,prometejImg2,prometejImg3, oblakImg1, oblakImg2,logo,textImg1,textImg2,backgroundImg1,backgroundImg2,fireWorkList
    size(1200,900)
    prometejImg1=loadImage("prometej.png")
    prometejImg2=loadImage("prometejGlow.png")
    prometejImg3=loadImage("prometejGlowHeart.png")
    oblakImg1=loadImage("oblak.png")
    oblakImg2=loadImage("oblakD.png")
    logo=loadImage("logotip.png")
    textImg1=loadImage("napis0.png")
    textImg2=loadImage("napis1.png")
    backgroundImg1=loadImage("background1.png")
    backgroundImg2=loadImage("background2.png")
    
def draw():
    global smokeTimer,textTimer,textSTOP,starX,starY,starTimer,fireWorkWork,randomFire,randomFireStop
    stroke(0)
    strokeWeight(1)
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
    platforma()
    znakSTPS()
    smoke(smokeRandomWidth,smokeRandomHeight,smokeRandomSpeed,smokeMovement)
    oblak()
    UFOS(UFOX,UFOY,UFODirection,UFOYMovement)
    if(keyPressed and key=="f" or key == "F"):
        if(fireWorkWork==0):
            fireWorkWork=1
            randomFire=random.randint(5,10)
    if(fireWorkWork==1 and randomFireStop<randomFire):
        fireWork()
    if(randomFireStop==randomFire):
        fireWorkWork=0
        randomFireStop=0
        fireWorkList=[]
    stroke(0)
    strokeWeight(1);
    if(keyPressed and key=="n" or key == "N"):
        textTimer=0
    if(textTimer==0):
        textSTOP=0
        text1()
