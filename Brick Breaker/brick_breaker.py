from graphics import *
import random
import math


margin = 10 # height of the paddle from the ground
moveIncrement = 15 # paddle movement
ballRadius = 15
BOUNCE_WAIT= 1200
lives = 2
clear_bubbles = []
minusLives = False
win = GraphWin("Brick Breaker", 300, 600)
win.setBackground("Black")

BALL_COUNT = 1  # If we change this, the number of ball changes!

class Timer:
    def __init__(self):
        self.value = 0


class Paddle:

    def __init__(self, color, width, height, coordx, win):
        self.color = color
        self.width = width
        self.height = height
        self.x = coordx
        self.shape = Rectangle(Point(self.x - int(self.width / 2), win.getHeight() - margin - self.height),
                               Point(self.x + int(self.width / 2), win.getHeight() - margin))
        self.shape.setFill(self.color)
        self.window = win
        self.shape.draw(self.window)

    def move_left(self):  
        if self.x == 45:
            pass
        else:
            self.x -= moveIncrement
            self.shape.move(-moveIncrement, 0)

    def move_right(self):  
        if self.x == 255:
            pass
        else:
            self.x += moveIncrement
            self.shape.move(moveIncrement, 0)



class Bubbles:
    def __init__(self, bcoordx, bcoordy, color, radius, win):
        self.shape = Circle(Point(bcoordx, bcoordy), radius)
        self.x = bcoordx
        self.y = bcoordy
        self.color = color
        self.window = win
        self.shape.setFill(self.color)
        self.shape.draw(self.window)
        self.radius = radius




class Ball:

    def __init__(self, coordx, coordy, color, radius, x_direction, speed, win):
        self.shape = Circle(Point(coordx, coordy), radius)
        self.x = coordx
        self.y = coordy
        self.xMovement = 0 # Current x movement
        self.yMovement = 0 # Current y movement
        self.color = color
        self.window = win
        self.shape.setFill(self.color)
        self.shape.draw(self.window)
        self.radius = radius
        self.timer = 0
        self.x_direction = x_direction   # Initial x direction. This variable will be 0 or 1. 1:right 0:left
        self.speed = speed

    def is_moving(self):   
        if self.xMovement == 1 or self.xMovement == -1:
            return True
        else:
            return False

    def bounce(self, gameTimer, minX, maxX, maxY):
        # Calculating x-axis ball movement and bouncing
        # minX: min x coord. of paddle
        # maxX: max x coord. of paddle
        # maxY: max y coord. at which the ball can be move. If it goes further, it falls to the ground.
        global BOUNCE_WAIT,lives,minusLives
        gameOver = False

        if gameTimer >= self.timer + BOUNCE_WAIT:
            self.timer = gameTimer
            if self.x <= 0:
                self.xMovement = 1
                self.x_direction = 0
            elif self.x >= 300:
                self.xMovement = -1
                self.x_direction = 1
            elif self.y <= 0:
                self.yMovement = 1
            elif (self.x >= minX and self.x <= maxX) and ( self.y > 560 and self.y <= maxY ):
                self.yMovement = -1
                if self.xMovement == 1:
                    self.xMovement = 1
                else:
                    self.xMovement = -1
            elif self.y > maxY:
                lives -= 1
                self.yMovement = -1
                minusLives = True
                if lives == 0:
                    gameOver = True

            if self.xMovement == 1:
                self.x += self.speed
            elif self.xMovement == -1:
                self.x -= self.speed
            if self.yMovement == 1:
                self.y += self.speed
            elif self.yMovement == -1:
                self.y -= self.speed
            self.shape.move(self.xMovement * self.speed, self.yMovement * self.speed)
            
            
            return gameOver



def main():
    global lives, minusLives, win
    myPaddle = Paddle("White", 100, 15, 150, win)
    ColorsList = ["Cyan","Red","Green","Yellow"]   
    BallList = list()
    for i in range(BALL_COUNT):
        rand_speed = random.randint(5, 20) # random speed for ball
        
        rand_direction = random.randint(0, 1) # This variable will be 0 or 1 randomly.
        ball = Ball(myPaddle.x - int(myPaddle.width/2) + i*30, win.getHeight() - margin - myPaddle.height - ballRadius, ColorsList[i%4] , ballRadius,rand_direction,rand_speed, win)
        BallList.append(ball)
    

    b1 = Bubbles(30,30,ColorsList[random.randint(0,3)], 30, win)
    b2 = Bubbles(90,30,ColorsList[random.randint(0,3)], 30, win)
    b3 = Bubbles(150,30,ColorsList[random.randint(0,3)], 30, win)
    b4 = Bubbles(210,30,ColorsList[random.randint(0,3)], 30, win)
    b5 = Bubbles(270,30,ColorsList[random.randint(0,3)], 30, win)
    b6 = Bubbles(30,90,ColorsList[random.randint(0,3)], 30, win)
    b7 = Bubbles(90,90,ColorsList[random.randint(0,3)], 30, win)
    b8 = Bubbles(150,90,ColorsList[random.randint(0,3)], 30, win)
    b9 = Bubbles(210,90,ColorsList[random.randint(0,3)], 30, win)
    b10 = Bubbles(270,90,ColorsList[random.randint(0,3)], 30, win)
    b11 = Bubbles(30,150,ColorsList[random.randint(0,3)], 30, win)
    b12 = Bubbles(90,150,ColorsList[random.randint(0,3)], 30, win)
    b13 = Bubbles(150,150,ColorsList[random.randint(0,3)], 30, win)
    b14 = Bubbles(210,150,ColorsList[random.randint(0,3)], 30, win)
    b15 = Bubbles(270,150,ColorsList[random.randint(0,3)], 30, win)
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    c5 = False
    c6 = False
    c7 = False
    c8 = False
    c9 = False
    c10 = False
    c11 = False
    c12 = False
    c13 = False
    c14 = False
    c15 = False
    bubbles = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    clear_bubbles = []

    
    livesCounter = Text(Point(win.getWidth() - int(win.getWidth() / 5), 250), f'Lives -- {lives}')
    livesCounter.setTextColor("Cyan")
    livesCounter.setSize(15)
    livesCounter.draw(win)
    gameTimer = Timer()
    
    gameOver = False
    quit_game = False
    while lives > 0:
        while not gameOver:
            try:
                keyPress = win.checkKey()
            except GraphicsError:
                quit_game = True
                win.close()
                break
            for b in BallList:
                if b.x >= 0 and b.x < 60 and b.y >= 0 and b.y < 60 and c1 == False:
                    bubbles[0].shape.undraw()
                    c1 = True
                    clear_bubbles.append(1)
                if b.x >= 60 and b.x < 120 and b.y >= 0 and b.y < 60 and c2 == False:
                    bubbles[1].shape.undraw()
                    c2 = True
                    clear_bubbles.append(1)
                if b.x >= 120 and b.x < 180 and b.y >= 0 and b.y < 60 and c3 == False:
                    bubbles[2].shape.undraw()
                    c3 = True
                    clear_bubbles.append(1)
                if b.x >= 180 and b.x < 240 and b.y >= 0 and b.y < 60 and c4 == False:
                    bubbles[3].shape.undraw()
                    c4 = True
                    clear_bubbles.append(1)
                if b.x >= 240 and b.x < 300 and b.y >= 0 and b.y < 60 and c5 == False:
                    bubbles[4].shape.undraw()
                    c5 = True
                    clear_bubbles.append(1)
                if b.x >= 0 and b.x < 60 and b.y >= 60 and b.y < 120 and c6 == False:
                    bubbles[5].shape.undraw()
                    c6 = True
                    clear_bubbles.append(1)
                if b.x >= 60 and b.x < 120 and b.y >= 60 and b.y < 120 and c7 == False:
                    bubbles[6].shape.undraw()
                    c7 = True
                    clear_bubbles.append(1)
                if b.x >= 120 and b.x < 180 and b.y >= 60 and b.y < 120 and c8 == False:
                    bubbles[7].shape.undraw()
                    c8 = True
                    clear_bubbles.append(1)
                if b.x >= 180 and b.x < 240 and b.y >= 60 and b.y < 120 and c9 == False:
                    bubbles[8].shape.undraw()
                    c9 = True
                    clear_bubbles.append(1)
                if b.x >= 240 and b.x < 300 and b.y >= 60 and b.y < 120 and c10 == False:
                    bubbles[9].shape.undraw()
                    c10 = True
                    clear_bubbles.append(1)
                if b.x >= 0 and b.x < 60 and b.y >= 120 and b.y < 180 and c11 == False:
                    bubbles[10].shape.undraw()
                    c11 = True
                    clear_bubbles.append(1)
                if b.x >= 60 and b.x < 120 and b.y >= 120 and b.y < 180 and c12 == False:
                    bubbles[11].shape.undraw()
                    c12 = True
                    clear_bubbles.append(1)
                if b.x >= 120 and b.x < 180 and b.y >= 120 and b.y < 180 and c13 == False:
                    bubbles[12].shape.undraw()
                    c13 = True
                    clear_bubbles.append(1)
                if b.x >= 180 and b.x < 240 and b.y >= 120 and b.y < 180 and c14 == False:
                    bubbles[13].shape.undraw()
                    c14 = True
                    clear_bubbles.append(1)
                if b.x >= 240 and b.x < 300 and b.y >= 120 and b.y < 180 and c15 == False:
                    bubbles[14].shape.undraw()
                    c15 = True
                    clear_bubbles.append(1)

            if keyPress == 'a':
                myPaddle.move_left()

            if keyPress == 'd':
                myPaddle.move_right()

            if keyPress == 'l': # balls will move faster
                for item in BallList:
                    item.speed += 1

            if keyPress == 'k':  # Balls will move slower. Note that in our case min speed is 2.
                for item in BallList:
                    if item.speed > 2:
                        item.speed -= 1

            if keyPress == 's':  # Initial movement of balls
                for item in BallList:
                    if(not item.is_moving()):
                        if item.x_direction == 1:   # it means ball moves to right in x direction
                            item.xMovement = 1
                        else:                   # it means ball moves to left in x direction
                            item.xMovement = -1
                        item.yMovement = -1 # at initial ball moves up in y direction


            gameTimer.value += 1
            for item in BallList:
                gameOver = item.bounce(gameTimer.value, (myPaddle.x-int(myPaddle.width/2)), (myPaddle.x+int(myPaddle.width/2)), win.getHeight() - margin - myPaddle.height)
                if minusLives:
                    for i in BallList:
                        i.shape.undraw()
                    myPaddle.shape.undraw()
                    for i in bubbles:
                        i.shape.undraw()
                    minusLives = False
                    livesCounter.undraw()
                    if lives == 0:
                        livesCounter = Text(Point(win.getWidth() - int(win.getWidth() / 5), 250), f'Lives -- 0')
                        livesCounter.setTextColor("Cyan")
                        livesCounter.setSize(15)
                        livesCounter.draw(win)
                        pass
                    else:
                        main()


                if len(clear_bubbles) == 15:
                    item.shape.undraw()
                    myPaddle.shape.undraw()
                    for i in bubbles:
                        i.shape.undraw()
                    redText1 = Text(Point(150, 300), f'GAME  OVER')
                    redText1.setStyle('normal')
                    redText1.setTextColor("Red")
                    redText1.setSize(15)
                    redText1.draw(win)
                    redText2 = Text(Point(150, 340), f'YOU  WIN!')
                    redText2.setStyle('normal')
                    redText2.setTextColor("Red")
                    redText2.setSize(15)
                    redText2.draw(win)
                    redText3 = Text(Point(150, 380), f'Press  Any  Key  to  Quit')
                    redText3.setStyle('normal')
                    redText3.setTextColor("Red")
                    redText3.setSize(15)
                    redText3.draw(win)
                    try:
                        if win.getKey():
                            win.close()
                            break
                    except GraphicsError:
                        win.close()
                        break
                if gameOver == True:
                    for i in bubbles:
                        i.shape.undraw()
                    myPaddle.shape.undraw()
                    item.shape.undraw()
                    redText1 = Text(Point(150, 300), f'GAME OVER!')
                    redText1.setStyle('normal')
                    redText1.setTextColor("Red")
                    redText1.setSize(15)
                    redText1.draw(win)
                    redText2 = Text(Point(150, 340), f'YOU  LOST!')
                    redText2.setStyle('normal')
                    redText2.setTextColor("Red")
                    redText2.setSize(15)
                    redText2.draw(win)
                    redText3 = Text(Point(150, 380), f'Press  Any  Key  to  Quit')
                    redText3.setStyle('normal')
                    redText3.setTextColor("Red")
                    redText3.setSize(15)
                    redText3.draw(win)
                    try:
                        if win.getKey():
                            win.close()
                            break
                    except GraphicsError:
                        win.close()
                        break
        if quit_game:
            win.close()
            break

main()




