from cmu_graphics import *
import math, copy
from PIL import Image
import os, pathlib
import random

"""Animations section"""
class Button:
    def __init__(self, x, y, width, height, color, message, textsize):
        self.x = x
        self.y = y
        self.buttonWidth = width
        self.buttonHeight = height
        self.color = color
        self.message = message
        self.textsize = textsize

    
    def drawButton(self):
        return drawRect(self.x, self.y, self.buttonWidth, self.buttonHeight, fill = self.color)
    
    def drawButtonLabel(self):
        return drawLabel(self.message, self.x + self.buttonWidth/2, self.y + self.buttonHeight/2, size = self.textsize)
    
class Card:
    def __init__(self, value, suit):
        self.value = value 
        self.suit = suit
    
    def __repr__(self):
        return f'{self.value} of {self.suit}'
    
    def __eq__(self, other):
        if isinstance(other, Card):
            if self.value == other.value and self.suit == other.suit:
                return True
            else:
                return False
        return False

class Player:
    def __init__(self, nickname, money, status, turn, card1, card2):
        self.nickname = nickname
        self.money = money
        self.status = status
        self.blind = "small"
        self.turn = turn
        self.card1 = card1
        self.card2 = card2
    def __repr__(self):
        return f"{self.nickname}"
    
    def drawPlayer(self, app):
        if self.status == "In":
            return drawRect(app.width/2 - app.buttonWidth/2, 9*app.height/16, app.buttonWidth, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
        elif self.status == "Out":
            return drawRect(app.width/2 - app.buttonWidth/2, 9*app.height/16, app.buttonWidth, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)
    def drawPlayerLabel(self, app):
        drawLabel(f"{self.nickname}: ${self.money}", app.width/2, 9*app.height/16 + app.buttonHeight/4)
    def drawPlayerCards(self, app):
        drawImage(app.sprites[self.card1],app.width/2 - 50, 9*app.height/16 + app.buttonHeight/2, width = 30, height = 40)
        drawImage(app.sprites[self.card2],app.width/2, 9*app.height/16 + app.buttonHeight/2, width = 30, height = 40)


class AI:
    def __init__(self, name, money, status, turn, card1, card2):
        self.name = name
        self.money = money
        self.status = status
        self.blind = None
        self.turn = turn
        self.card1 = card1
        self.card2 = card2

    def __repr__(self):
        return f"{self.name}"
    
    def drawPlayer(self, app):
        if self.name == "AI1":
            if self.status == "In":
                return drawRect(2*app.width/32, 16*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
            elif self.status == "Out":
                return drawRect(2*app.width/32, 16*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)
        
        elif self.name == "AI2":
            if self.status == "In":
                return drawRect(0, 11*app.height/32, 3*app.buttonWidth/4, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
            elif self.status == "Out":
                return drawRect(0, 11*app.height/32, 3*app.buttonWidth/4, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)
        
        elif self.name == "AI3":
            if self.status == "In":
                return drawRect(2*app.width/32, 6*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
            elif self.status == "Out":
                return drawRect(2*app.width/32, 6*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)
        
        elif self.name == "AI4":
            if self.status == "In":
                return drawRect(app.width/2 - app.buttonWidth/2, 2*app.height/16, app.buttonWidth, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
            elif self.status == "Out":
                return drawRect(app.width/2 - app.buttonWidth/2, 2*app.height/16, app.buttonWidth, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)
        
        elif self.name == "AI7":
            if self.status == "In":
                return drawRect(25*app.width/32, 16*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
            elif self.status == "Out":
                return drawRect(25*app.width/32, 16*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)
        
        elif self.name == "AI6":
            if self.status == "In":
                return drawRect(app.width -3*app.buttonWidth/4, 11*app.height/32, 3*app.buttonWidth/4, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
            elif self.status == "Out":
                return drawRect(app.width -3*app.buttonWidth/4, 11*app.height/32, 3*app.buttonWidth/4, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)
        
        elif self.name == "AI5":
            if self.status == "In":
                return drawRect(25*app.width/32, 6*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "green", borderWidth = 5)
            elif self.status == "Out":
                return drawRect(25*app.width/32, 6*app.height/32, app.buttonWidth, app.buttonHeight/2, fill = None, border = "red", borderWidth = 5)

    def drawPlayerLabel(self, app):
        if self.name == "AI1":
            return drawLabel(f"{self.name}: ${self.money}", 2*app.width/32 + app.buttonWidth/2, 16*app.height/32 + app.buttonHeight/4)
        elif self.name == "AI2":
            return drawLabel(f"{self.name}: ${self.money}", 3*app.buttonWidth/8, 11*app.height/32 + app.buttonHeight/4)
        elif self.name == "AI3":
            return drawLabel(f"{self.name}: ${self.money}", 2*app.width/32 + app.buttonWidth/2, 6*app.height/32 + app.buttonHeight/4)
        elif self.name == "AI4":
            return drawLabel(f"{self.name}: ${self.money}", app.width/2, 2*app.height/16 + app.buttonHeight/4)
        elif self.name == "AI7":
            return drawLabel(f"{self.name}: ${self.money}", 25*app.width/32 + app.buttonWidth/2, 16*app.height/32 + app.buttonHeight/4)
        elif self.name == "AI6":
            return drawLabel(f"{self.name}: ${self.money}", app.width -3*app.buttonWidth/4 + 3*app.buttonWidth/8, 11*app.height/32 + app.buttonHeight/4)
        elif self.name == "AI5":
            return drawLabel(f"{self.name}: ${self.money}", 25*app.width/32 + app.buttonWidth/2, 6*app.height/32 + app.buttonHeight/4)

    def drawPlayerCards(self, app):
        if self.name == "AI1":
            drawImage(app.sprites[self.card1],2*app.width/32, 16*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
            drawImage(app.sprites[self.card2],2*app.width/32 + 50, 16*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
        elif self.name == "AI2":
            drawImage(app.sprites[self.card1],0, 11*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
            drawImage(app.sprites[self.card2],0 + 50, 11*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
        elif self.name == "AI3":
            drawImage(app.sprites[self.card1],2*app.width/32, 6*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
            drawImage(app.sprites[self.card2],2*app.width/32 + 50, 6*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
        elif self.name == "AI4":
            drawImage(app.sprites[self.card1],app.width/2 - app.buttonWidth/2, 2*app.height/16 - 40, width = 30, height = 40)
            drawImage(app.sprites[self.card2],app.width/2 - app.buttonWidth/2 + 50, 2*app.height/16 - 40, width = 30, height = 40)
        elif self.name == "AI5":
            drawImage(app.sprites[self.card1],25*app.width/32 + app.buttonWidth - 100, 6*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
            drawImage(app.sprites[self.card2],25*app.width/32 + app.buttonWidth - 50, 6*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
        elif self.name == "AI6":
            drawImage(app.sprites[self.card1],app.width -3*app.buttonWidth/4, 11*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
            drawImage(app.sprites[self.card2],app.width -3*app.buttonWidth/4 + 50, 11*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
        elif self.name == "AI7":
            drawImage(app.sprites[self.card1],25*app.width/32, 16*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
            drawImage(app.sprites[self.card2],25*app.width/32 + 50, 16*app.height/32 + app.buttonHeight/2, width = 30, height = 40)
        

#import image of deck of cards, implemented from Lecture 
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))


def onAppStart(app):
    restart(app)
    #timer
    app.stepsPerSecond = 1
    app.onStepTimer = 0

    #Welcome screen buttons
    app.buttonWidth = (app.width)/5
    app.buttonHeight = (app.height)/8
    app.buttonBorder = False
    app.buttonBorderType = None
    app.leftColumnButtonsX = (app.width)/2 - (app.width)/10 - (app.width)/4
    app.middleColumnButtonsX = (app.width)/2 - (app.width)/10
    app.rightColumnButtonsX = (app.width)/2 - (app.width)/10 + (app.width)/4
    app.topRowButtonsY = 5*(app.height)/8
    app.bottomRowButtonsY = 6*(app.height)/8
   

    app.b1 = Button(app.leftColumnButtonsX, app.topRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Easy", 15)
    app.b2 = Button(app.leftColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, "red", "Hard", 15)
    app.b3 = Button(app.middleColumnButtonsX, app.topRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Nickname", 15)
    app.b4 = Button(app.middleColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Buy-In", 15)
    app.b5 = Button(app.rightColumnButtonsX, app.topRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Number of AI", 15)
    app.b6 = Button(app.rightColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Play Timer", 15)
    app.b7 = Button(app.middleColumnButtonsX, 17*(app.height)/32, app.buttonWidth, (app.height)/32, "green", "Play!", 15)
    app.b8 = Button(app.middleColumnButtonsX, 18*(app.height)/32, app.buttonWidth, (app.height)/32, "green", "Instructions", 15)

    #pause screen buttons
    app.b9 = Button(app.leftColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Instructions", 15)
    app.b10 = Button(app.rightColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "End Game", 15)

    #gameover screen buttons
    app.b11 = Button(app.leftColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Ledger", 15)
    app.b12 = Button(app.rightColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, "green", "Reset Game", 15)

    #playing screen buttons
    app.b13 = Button(app.width/2 - 2*app.buttonWidth, app.bottomRowButtonsY, app.buttonWidth - 10, app.buttonHeight/2, "green", "Check", 15)  
    app.b14 = Button(app.width/2 - app.buttonWidth, app.bottomRowButtonsY, app.buttonWidth - 10, app.buttonHeight/2, "green", "Fold", 15)
    app.b15 = Button(app.width/2 , app.bottomRowButtonsY, app.buttonWidth - 10, app.buttonHeight/2, "green", "Call", 15)
    app.b16 = Button(app.width/2 + app.buttonWidth, app.bottomRowButtonsY, app.buttonWidth -10, app.buttonHeight/2, "green", "Raise", 15)
    app.b17 = Button(app.width/2 - app.buttonWidth/2, app.bottomRowButtonsY + app.buttonHeight, app.buttonWidth -10, app.buttonHeight/2, "green", "Ledger", 15)
    app.b18 = Button(app.width - app.buttonWidth/2, app.buttonHeight/3, app.buttonWidth/10, app.buttonHeight/3, "black", "", 15)
    app.b19 = Button(app.width - app.buttonWidth/2 + app.buttonWidth/7, app.buttonHeight/3, app.buttonWidth/10, app.buttonHeight/3, "black", "", 15)

    #screen tracker
    app.prevscreen = None
    app.currscreen = "welcomescreen"

    #ledger buttons
    app.b20 = Button(app.buttonWidth/4, app.buttonHeight/2, app.buttonWidth/2, app.buttonHeight/4, "green", "Back", 15)

    #Deck of cards
    #Image from https://www.emanueleferonato.com/2017/03/04/html5-deck-of-cards-management/ 
    #Image from that website was sourced from http://game-icons.net/ 
    app.deck = createDeck()
    spritestrip = openImage('cardssprite.png')
    app.sprites = [ ]
    for row in range(4):
        for col in range(13):
            sprite = CMUImage(spritestrip.crop((61.6*col,80.5*row , 61.6*(col+1), 80.5*(row + 1))))
            app.sprites.append(sprite)
    app.drawCards = False
    
    


def createDeck():
    values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ['spades', 'clubs', 'diamonds', 'hearts' ]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(Card(value, suit))
    return deck


def restart(app):
    app.welcomescreen = True
    app.playing = False
    app.paused = False
    app.gameover = False
    app.ledger = False
    app.instructions = False
    app.drawBorder = False
    app.difficulty = None 
    app.nickname = ''
    app.ai = ''
    app.timer = ''
    app.buyin = ''
    
    app.playingGame = False
    app.welcomescreenerror = False

    #base playing values
    app.bigBlind = 10
    app.smallBlind = 5
    app.tableMoney = 0
    app.currBet = app.smallBlind
    app.betting = False
    app.bet = 0

    #player tracking
    app.currPlayer = None
    app.playerList= []
    app.roundPlayingList = []
    app.roundTurnsLeft = len(app.playerList)
    app.handWinner = None
    app.winningHand = None

    #round tracking
    app.roundList = ["preFlop", "postFlop", "postTurn", "postRiver"] 
    app.currRound = "preFlop"
    app.showFlop = False
    app.showTurn = False
    app.showRiver = False

    #user cheating
    app.revealCards = False

    #ledger
    app.action = None
    app.ledgerList = []
    app.ledgerY = 20

    #hand detection
    app.betterHand = ''



def onStep(app):
    if app.playing:
        app.onStepTimer += 1
        app.displayTimer -= 1
        if app.displayTimer == 0:
            call(app)
        else:
            if len(app.roundPlayingList) == 1:
                app.handWinner = app.roundPlayingList[0]
                app.handWinner.money += app.tableMoney
                app.tableMoney = 0
                nextRound(app)
            
            if isinstance(app.currPlayer, AI):
                if app.onStepTimer % 3 == 0:
                    if app.difficulty == "Easy":
                        easyAI(app, app.currRound, app.currPlayer)
                        app.onStepTimer = 0
                        app.displayTimer = int(app.timer)
                    else:
                        hardAI(app, app.currRound, app.currPlayer)
                        app.onStepTimer = 0
                        app.displayTimer = int(app.timer)

def onKeyPress(app, key):
    #User inputs on the welcome screen
    if app.welcomescreen == True:
        if app.buttonBorderType == "Nickname":
            if len(app.nickname) < 10:
                if key == "backspace":
                    app.nickname = app.nickname[:-1]
                elif key == "enter":
                    app.buttonBorderType = None
                elif key == "space":
                    pass
                elif key.isalpha() or key.isdigit():
                    app.nickname += key
            else:
                if key == "backspace":
                    app.nickname = app.nickname[:-1]
        elif app.buttonBorderType == "BuyIn":
            if key == "backspace":
                app.buyin = app.buyin[:-1]
            elif key == "enter":
                if int(app.buyin) >= 10:
                    app.buttonBorderType = None
            elif key.isdigit():
                app.buyin += key
        elif app.buttonBorderType == "PlayTimer":
            if key == "backspace":
                app.timer = app.timer[:-1]
            elif key == "enter":
                app.buttonBorderType = None
            elif key.isdigit():
                app.timer += key
        elif app.buttonBorderType == "AI":
            if key == "backspace":
                app.ai = app.ai[:-1]
            elif key == "enter":
                app.buttonBorderType = None
            elif key.isdigit() and (int(key) > 0) and (int(key) < 8):
                app.ai = key
        
    elif app.playing:
        if key == "p":
            app.welcomescreen = False
            app.playing = False
            app.paused = True
            app.gameover = False
            app.ledger = False
            app.instructions = False
            app.currscreen = "paused"

        elif key == "l":
            app.revealCards = not app.revealCards

        if isinstance(app.currPlayer, Player):
            #check
            if key == "k" and app.bet == 0:
                check(app)
                
            #call
            elif key == "c":
                call(app)
                
            #fold
            elif key == "f":
                fold(app)
                
            #raise
            elif key == "r" or app.betting:
                app.betting = True 
                if key == "backspace":
                    app.bet = app.bet//10
                elif key == "enter":
                    if ((app.bet >= app.currBet) and (app.bet <=app.currPlayer.money)):
                        bet(app)
                elif key.isdigit():
                    app.bet = app.bet*10 + int(key)

    elif app.ledger:
        if key == "up":
            app.ledgerY += 20
        elif key == "down":
            app.ledgerY -= 20           
        

def onMousePress(app, mouseX, mouseY):
    if app.welcomescreen == True:
        #NickName Button
        if (((mouseX >= app.middleColumnButtonsX) and (mouseX <= app.middleColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.topRowButtonsY) and (mouseY <= app.topRowButtonsY + app.buttonHeight))):
            app.buttonBorderType = "Nickname"
            app.buttonBorder = True  
            app.buttonBorderType = "Nickname"               
        #Buy-In button
        elif ((mouseX >= (app.middleColumnButtonsX) and (mouseX <= app.middleColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight))):
            app.buttonBorderType = "BuyIn"
            app.buttonBorder = True 
            app.buttonBorderType = "BuyIn"

        #Number of AI button
        elif (((mouseX >= app.rightColumnButtonsX) and (mouseX <= app.rightColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.topRowButtonsY) and (mouseY <= app.topRowButtonsY + app.buttonHeight))):
            app.buttonBorderType = "AI"
            app.buttonBorder = True
            app.buttonBorderType = "AI"                 
        #Play timer button 
        elif ((mouseX >= app.rightColumnButtonsX and (mouseX <= app.rightColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight))):
            app.buttonBorderType = "PlayTimer"
            app.buttonBorder = True 
            app.buttonBorderType = "PlayTimer"
        #Easy button
        elif (((mouseX >= app.leftColumnButtonsX) and (mouseX <= app.leftColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.topRowButtonsY) and (mouseY <= app.topRowButtonsY + app.buttonHeight))):
            app.difficulty = "Easy"
            app.buttonBorder = True
            app.buttonBorderType = "Easy"                 
        #Hard button
        elif (((mouseX >= app.leftColumnButtonsX) and (mouseX <= app.leftColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight))):
            app.difficulty = "Hard"
            app.buttonBorder = True 
            app.buttonBorderType = "Hard"
        #Play Button
        elif (((mouseX >= app.middleColumnButtonsX) and (mouseX <= app.middleColumnButtonsX + app.buttonWidth)
            and (mouseY >= (17*(app.height)/32)) and (mouseY <= (18*(app.height)/32 )))):
            if (app.difficulty != None) and (app.nickname != '') and (app.ai != '') and (app.timer != '') and (app.buyin != '') and (int(app.buyin)>0):
                app.welcomescreenerror = False
                app.welcomescreen = False
                app.playing = True
                app.paused = False
                app.gameover = False
                app.ledger = False
                app.instructions = False
                app.prevscreen = app.currscreen
                app.currscreen = "playing"
                app.playingGame = True
                addAI(app)
                addPlayer(app)
                assignBlinds(app)
                app.currPlayer = newRoundCurrPlayer(app)
                app.roundPlayingList = app.playerList + []
                dealCards(app)
                app.displayTimer = int(app.timer)
            else:
                app.welcomescreenerror = True
        #instructions button
        elif (((mouseX >= app.middleColumnButtonsX) and (mouseX <= app.middleColumnButtonsX + app.buttonWidth)
            and (mouseY >= 18*(app.height)/32) and (mouseY <= 19*(app.height)/32 ))):
            app.welcomescreen = False
            app.playing = False
            app.paused = False
            app.gameover = False
            app.ledger = False
            app.instructions = True
            app.prevscreen = app.currscreen
            app.currscreen = "instructions"
            
        else: 
            app.buttonBorder = False
        
    
    elif app.paused:
        if (((mouseX >= app.leftColumnButtonsX) and (mouseX <= app.leftColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight))):
            app.welcomescreen = False
            app.playing = False
            app.paused = False
            app.gameover = False
            app.ledger = False
            app.instructions = True
            app.prevscreen = app.currscreen
            app.currscreen = "playing"
        elif (((mouseX >= app.rightColumnButtonsX) and (mouseX <= app.rightColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight))):
            app.welcomescreen = False
            app.playing = False
            app.paused = False
            app.gameover = True
            app.ledger = False
            app.instructions = False
            app.prevscreen = app.currscreen
            app.currscreen = "gameover"
        elif (((mouseX >= app.width/2 - 50) and (mouseX <= app.width/2 + 100)
            and (mouseY >= 3*(app.height)/8 - 90 ) and (mouseY <= 3*(app.height)/8 + 90))):
            app.welcomescreen = False
            app.playing = True
            app.paused = False
            app.gameover = False
            app.ledger = False
            app.instructions = False
            app.prevscreen = app.currscreen
            app.currscreen = "playing"

    elif app.gameover:
        if (((mouseX >= app.leftColumnButtonsX) and (mouseX <= app.leftColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight))):
            app.welcomescreen = False
            app.playing = False
            app.paused = False
            app.gameover = False
            app.ledger = True
            app.instructions = False
            app.prevscreen = app.currscreen
            app.currscreen = "ledger"
        elif (((mouseX >= app.rightColumnButtonsX) and (mouseX <= app.rightColumnButtonsX + app.buttonWidth)
            and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight))):
            restart(app)
    
    elif app.playing:
        #ledger button
        if (((mouseX >= app.width/2 - app.buttonWidth/2) and (mouseX <= app.width/2 - app.buttonWidth/2 + app.buttonWidth -10)
            and (mouseY >= app.bottomRowButtonsY + app.buttonHeight) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight + app.buttonHeight/2))):
            app.welcomescreen = False
            app.playing = False
            app.paused = False
            app.gameover = False
            app.ledger = True
            app.instructions = False
            app.prevscreen = app.currscreen
            app.currscreen = "ledger"
        #pause button
        elif (((mouseX >= app.width - app.buttonWidth/2) and (mouseX <= app.width - app.buttonWidth/2 + app.buttonWidth/7 + app.buttonWidth/10)
            and (mouseY >= app.buttonHeight/3) and (mouseY <= 2*app.buttonHeight/3))):
            app.welcomescreen = False
            app.playing = False
            app.paused = True
            app.gameover = False
            app.ledger = False
            app.instructions = False
            app.prevscreen = app.currscreen
            app.currscreen = "paused"
        if isinstance(app.currPlayer, Player):
            #check button
            if (((mouseX >= app.width/2 - 2*app.buttonWidth) and (mouseX <= app.width/2 - 2*app.buttonWidth + app.buttonWidth - 10)
                and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight/2))):
                check(app)
                
            #Fold button
            elif (((mouseX >= app.width/2 - app.buttonWidth) and (mouseX <= app.width/2 - app.buttonWidth + app.buttonWidth - 10)
                and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight/2))):
                fold(app)
                
            #Call button
            elif (((mouseX >= app.width/2) and (mouseX <= app.width/2 + app.buttonWidth - 10)
                and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight/2))):
                call(app)
                
            #Raise button
            elif (((mouseX >= app.width/2 + app.buttonWidth) and (mouseX <= app.width/2 + app.buttonWidth + app.buttonWidth - 10)
                and (mouseY >= app.bottomRowButtonsY) and (mouseY <= app.bottomRowButtonsY + app.buttonHeight/2))):
                app.betting = True
               
            else:
                app.betting = False
            

    elif app.ledger:
        if (((mouseX >= app.buttonWidth/4) and (mouseX <= app.buttonWidth/4 + app.buttonWidth/2)
            and (mouseY >= app.buttonHeight/2) and (mouseY <= app.buttonHeight/2 + app.buttonHeight/4))):
            if app.prevscreen == "gameover":
                app.welcomescreen = False
                app.playing = False
                app.paused = False
                app.gameover = True
                app.ledger = False
                app.instructions = False
                app.prevscreen = app.currscreen
                app.currscreen = "gameover"
            elif app.prevscreen == "playing":
                app.welcomescreen = False
                app.playing = True
                app.paused = False
                app.gameover = False
                app.ledger = False
                app.instructions = False
                app.prevscreen = app.currscreen
                app.currscreen = "playing"
    
    elif app.instructions:
        if (((mouseX >= app.buttonWidth/4) and (mouseX <= app.buttonWidth/4 + app.buttonWidth/2)
            and (mouseY >= app.buttonHeight/2) and (mouseY <= app.buttonHeight/2 + app.buttonHeight/4))):
            if app.prevscreen == "paused":
                app.welcomescreen = False
                app.playing = False
                app.paused = True
                app.gameover = False
                app.ledger = False
                app.instructions = False
                app.prevscreen = app.currscreen
                app.currscreen = "paused"
            elif app.prevscreen == "welcomescreen":
                app.welcomescreen = True
                app.playing = False
                app.paused = False
                app.gameover = False
                app.ledger = False
                app.instructions = False
                app.prevscreen = app.currscreen
                app.currscreen = "welcomescreen"
    

def redrawAll(app):
    
    if app.welcomescreen:
        #Welcome screen backdrop
        drawRect(0, 0, app.width, app.height, fill = "lightBlue")
        
        #Welcome screen instructions for choosing options
        drawLabel("Welcome to Poker112!", app.width/2, app.height/8, size = 30)
        drawLabel("Please choose your...", app.width/2, app.height/4, size = 15)
        drawLabel("Desired difficulty(Easy or hard)", app.width/2, 3* app.height/10, size = 15)
        drawLabel("Nickname(Must be less than 10 characters)", app.width/2, 7*app.height/20, size = 15)
        drawLabel("Buy-in($10 Minimum)", app.width/2, 2*app.height/5, size = 15)
        drawLabel("Number of opponents(1-7)", app.width/2, 9*app.height/20, size = 15)
        drawLabel("Play timer(In seconds)", app.width/2, app.height/2, size = 15)

        #Welcome screen buttons
        app.b1.drawButton()
        app.b2.drawButton()
        app.b3.drawButton()
        app.b4.drawButton()
        app.b5.drawButton()
        app.b6.drawButton()
        app.b7.drawButton()
        app.b8.drawButton()

        app.b1.drawButtonLabel()
        app.b2.drawButtonLabel()
        app.b3.drawButtonLabel()
        app.b4.drawButtonLabel()
        app.b5.drawButtonLabel()
        app.b6.drawButtonLabel()
        app.b7.drawButtonLabel()
        app.b8.drawButtonLabel()
      
        #userchoices
        drawLabel(f"{app.nickname}", app.middleColumnButtonsX + (app.buttonWidth)/2, (app.topRowButtonsY + app.buttonHeight/2) + 15, size = 15) 
        drawLabel(f"{app.ai} AI", app.rightColumnButtonsX + (app.buttonWidth)/2, (app.topRowButtonsY + app.buttonHeight/2) + 15, size = 15) 
        drawLabel(f"{app.timer} seconds", app.rightColumnButtonsX + (app.buttonWidth)/2, (app.bottomRowButtonsY + app.buttonHeight/2) + 15, size = 15)
        drawLabel(f"${app.buyin}", app.middleColumnButtonsX + (app.buttonWidth)/2, (app.bottomRowButtonsY + app.buttonHeight/2) + 15, size = 15)

        if app.difficulty == "Easy":
            drawRect(app.leftColumnButtonsX, app.topRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "blue", borderWidth = 10)
        elif app.difficulty == "Hard":
            drawRect(app.leftColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "blue", borderWidth = 10)
    

        #error message for not including all information
        if app.welcomescreenerror:
            drawLabel("Please enter all information to play", app.width/2, 3*app.height/5, size = 15, fill = "red", bold = True)

        #Users can see what they have selected
        if app.buttonBorder:
            if app.buttonBorderType == "Easy":
                drawRect(app.leftColumnButtonsX, app.topRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "black", borderWidth = 5)
            
            elif app.buttonBorderType == "Hard":
                drawRect(app.leftColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "black", borderWidth = 5)
            
            elif app.buttonBorderType == "Nickname":
                drawRect(app.middleColumnButtonsX, app.topRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "black", borderWidth = 5)
            
            elif app.buttonBorderType == "BuyIn":
                drawRect(app.middleColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "black", borderWidth = 5)
            
            elif app.buttonBorderType == "AI":
                drawRect(app.rightColumnButtonsX, app.topRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "black", borderWidth = 5)
            
            elif app.buttonBorderType == "PlayTimer":
                drawRect(app.rightColumnButtonsX, app.bottomRowButtonsY, app.buttonWidth, app.buttonHeight, fill = None, border = "black", borderWidth = 5)
    
    elif app.playing:
        drawRect(0, 0, app.width, app.height, fill = "lightBlue")
        drawOval(app.width/2, 3*(app.height)/8, 2*app.width/3, app.height/3, border = "Brown", fill = "green", borderWidth = 10)
        drawLabel(f"Pot:{app.tableMoney}", app.width/2, 7*(app.height)/16, size = 20)
        drawLabel(f"Bet:{app.bet}", app.width/2, 4*(app.height)/8, size = 20)
        #timer
        drawLabel(f"Time left: {app.displayTimer}", app.width - 100, app.height - 40, size = 20)
        #check
        app.b13.drawButton()
        app.b13.drawButtonLabel()
        #fold
        app.b14.drawButton()
        app.b14.drawButtonLabel()
        #call
        app.b15.drawButton()
        app.b15.drawButtonLabel()
        #raise
        app.b16.drawButton()
        app.b16.drawButtonLabel()
        #ledger
        app.b17.drawButton()
        app.b17.drawButtonLabel()
        #pause icons
        app.b18.drawButton()
        app.b18.drawButtonLabel()
        app.b19.drawButton()
        app.b19.drawButtonLabel()

        #border for betting button
        if app.betting:
            drawRect(app.width/2 + app.buttonWidth, app.bottomRowButtonsY, app.buttonWidth -10, app.buttonHeight/2, fill = None, border = "black", borderWidth = 5)   

        #players icons
        for player in app.playerList:
            player.drawPlayer(app)
            player.drawPlayerLabel(app)
        #table cards
        if app.showRiver:
            
            sprite1 = app.sprites[app.tableCards[0]]
            sprite2 = app.sprites[app.tableCards[1]]
            sprite3 = app.sprites[app.tableCards[2]]
            sprite4 = app.sprites[app.tableCards[3]]
            sprite5 = app.sprites[app.tableCards[4]]
            drawImage(sprite1,app.width/2 - 170, 5*app.height/16)
            drawImage(sprite2,app.width/2 - 100, 5*app.height/16)
            drawImage(sprite3,app.width/2 - 30, 5*app.height/16)
            drawImage(sprite4,app.width/2 + 40, 5*app.height/16)
            drawImage(sprite5,app.width/2 + 110, 5*app.height/16)
        if app.showTurn:
        
            sprite1 = app.sprites[app.tableCards[0]]
            sprite2 = app.sprites[app.tableCards[1]]
            sprite3 = app.sprites[app.tableCards[2]]
            sprite4 = app.sprites[app.tableCards[3]]
            drawImage(sprite1,app.width/2 - 170, 5*app.height/16)
            drawImage(sprite2,app.width/2 - 100, 5*app.height/16)
            drawImage(sprite3,app.width/2 - 30, 5*app.height/16)
            drawImage(sprite4,app.width/2 + 40, 5*app.height/16)
        if app.showFlop:
        
            sprite1 = app.sprites[app.tableCards[0]]
            sprite2 = app.sprites[app.tableCards[1]]
            sprite3 = app.sprites[app.tableCards[2]]
            drawImage(sprite1,app.width/2 - 170, 5*app.height/16)
            drawImage(sprite2,app.width/2 - 100, 5*app.height/16)
            drawImage(sprite3,app.width/2 - 30, 5*app.height/16)
        
        #player cards
        for player in app.roundPlayingList:
            if isinstance(player, Player):
                player.drawPlayerCards(app)
            else:
                if app.revealCards:
                    player.drawPlayerCards(app)

        #turn and action statements
        if len(app.ledgerList) == 0:
            drawLabel(f"It's {app.currPlayer}'s turn!", app.width/2, 23*(app.height)/32, size = 15)
        else:
            drawLabel(f"{app.ledgerList[-1]}, It's {app.currPlayer}'s turn!", app.width/2, 23*(app.height)/32, size = 15)

        #blinds
        for i in range(len(app.playerList)):
            if app.playerList[i].blind == "small":
                smallBlindIndex = i
                bigBlindIndex = (i+1)%len(app.playerList)
        drawLabel(f"{app.playerList[smallBlindIndex]} has the small blind, {app.playerList[bigBlindIndex]} has the big blind!", app.width/2, 22*(app.height)/32, size = 15)


    elif app.instructions:
        #information from https://www.cardplayer.com/rules-of-poker/how-to-play-poker/games/texas-holdem 
        drawRect(0, 0, app.width, app.height, fill = "lightBlue")
        drawLabel("Texas Hold 'Em Instructions", app.width/2, app.height/16, size = 25)
        drawLabel("Players receive 2 down cards as their personal hand. Board cards are community cards, and a player can use any five-card combination ", app.width/2, app.height/8)
        drawLabel("from among the board and personal cards. Players can also use only board cards to form a hand. A dealer button is used with two blinds.", app.width/2, 5*app.height/32)
        
        drawLabel("There are 4 actions that can be played:", app.width/2, 8*app.height/32)
        drawLabel("1.   Call: Matching the bet amount that has been put in by another player in the form of a bet or a raise", app.width/5, 9*app.height/32, align = "left")
        drawLabel("2.   Raise: Increasing the bet", app.width/5, 10*app.height/32, align = "left")
        drawLabel("3.   Fold: Ending participation in a hand", app.width/5, 11*app.height/32, align = "left")
        drawLabel("4.   Check: Passing the action to the next player if the current bet is 0", app.width/5, 12*app.height/32, align = "left")
        
        drawLabel("Rounds of Betting", app.width/2, 14*app.height/32)
        drawLabel("1.   Opening Deal: Each player is dealt two cards face down, known as pocket cards", app.width/5, 15*app.height/32, align = "left")
        drawLabel("2.   First round of betting: Starting with the player on the left of the big blind, each player can call the big blind, ", app.width/5, 16*app.height/32, align = "left")
        drawLabel("     raise, or fold. The big blind also has the option to raise the upraised pot", app.width/5, 17*app.height/32, align = "left")
        drawLabel("3.   The Flop: 3 community cards are dealt to the table face up", app.width/5, 18*app.height/32, align = "left")
        drawLabel("4.   Second round of betting: Starting with the player to the left of the dealer button, each player can check or bet. ", app.width/5, 19*app.height/32, align = "left")
        drawLabel("      Once a bet has been made, each player can raise, call, or fold.", app.width/5, 20*app.height/32, align = "left")
        drawLabel("5.   The Turn: A 4th card is added face-up to the community cards", app.width/5, 21*app.height/32, align = "left")
        drawLabel("6.   Third round of betting: Follows the same format as the second round of betting", app.width/5, 22*app.height/32, align = "left")
        drawLabel("7.   The River: A 5th and final card is added face-up to the community cards", app.width/5, 23*app.height/32, align = "left")
        drawLabel("8.   Final round of betting: Follows the same format as the previous rounds", app.width/5, 24*app.height/32, align = "left")
        drawLabel("9.   The Showdown: Using the best 5-card combination of their pocket and community cards, the remaining players", app.width/5, 25*app.height/32, align = "left")
        drawLabel("      show their hands. The highest 5-card hand wins the pot", app.width/5, 26*app.height/32, align = "left")


        app.b20.drawButton()
        app.b20.drawButtonLabel()
        #plain screen with instructions, potentially examples with drawn cards
        #temporary drawing to test image import

    elif app.paused:
        drawRect(0, 0, app.width, app.height, fill = "lightBlue")
        drawRegularPolygon(app.width/2, 3*(app.height)/8, 100, 3, fill='pink', border='black', rotateAngle = 90)
        app.b9.drawButton()
        app.b9.drawButtonLabel()
        app.b10.drawButton()
        app.b10.drawButtonLabel()

    elif app.ledger:
        drawRect(0, 0, app.width, app.height, fill = "lightBlue")
        #drawLabel("Ledger", app.width/2, app.height/2)
        app.b20.drawButton()
        app.b20.drawButtonLabel()
        #draw lines of text from a list. Based on plays
        for i in range(len(app.ledgerList)):
            drawLabel(app.ledgerList[i], app.width/2, app.ledgerY + 20*i, size = 15)
            

    elif app.gameover:
        drawRect(0, 0, app.width, app.height, fill = "lightBlue")
        drawLabel("Gameover", app.width/2, app.height/2)
        app.b11.drawButton()
        app.b11.drawButtonLabel()
        app.b12.drawButton()
        app.b12.drawButtonLabel()




"""UI Functions"""
def addAI(app):
    numAI = int(app.ai)
    for i in range(numAI):
        newAI = AI(f"AI{i+1}", int(app.buyin), "In", False, 0, 0)
        app.playerList.append(newAI)

def addPlayer(app):
    newPlayer = Player(app.nickname, int(app.buyin), "In", True, 0, 0)
    app.playerList.append(newPlayer)
    app.roundPlayingList = app.playerList + []
    app.roundTurnsLeft = len(app.roundPlayingList)

def call(app):
    if app.currPlayer.blind == "small" and app.currRound == "preFlop":
        app.currPlayer.money += app.smallBlind
        app.tableMoney -= app.smallBlind
        app.currPlayer.money -= app.currBet
        app.tableMoney += app.currBet
    elif int(app.currPlayer.money) > app.currBet:
        app.currPlayer.money -= app.currBet
        app.tableMoney += app.currBet
    else:
        fold(app)
    app.action = "called"
    app.roundTurnsLeft -= 1
    if app.roundTurnsLeft == 0:
        nextTurn(app)
        nextRound(app)
    else:
        nextTurn(app)
    app.displayTimer = int(app.timer)


def check(app):
    if (app.currBet == 0) or (app.currPlayer.blind == "big" and app.currRound == "preFlop"):
        app.roundTurnsLeft -= 1
        app.action = "checked"
        if app.roundTurnsLeft == 0:
            nextTurn(app)
            nextRound(app)
        else:
            nextTurn(app)
        app.displayTimer = int(app.timer)

def fold(app):
    app.currPlayer.status = "Out"
    app.roundPlayingList.remove(app.currPlayer)
    app.roundTurnsLeft -= 1
    app.action = "folded"
    if app.roundTurnsLeft == 0:
        nextTurn(app)
        nextRound(app)
    else:
        nextTurn(app)
    app.displayTimer = int(app.timer)

def bet(app):
    app.currBet = app.bet
    app.betting = False
    app.tableMoney += app.bet
    app.currPlayer.money -= app.bet
    app.bet = 0
    app.action = "raised"
    nextTurn(app)
    app.roundTurnsLeft = len(app.roundPlayingList) - 1
    app.displayTimer = int(app.timer)


        
"""AI Functions"""
#hand chart from https://poker-coaching.s3.amazonaws.com/tools/preflop-charts/full-preflop-charts.pdf

#returns a value from 0 to 50
def simPreFlop(app, ai):
    card1 = ai.card1
    card2 = ai.card2
    #pair
    if app.deck[card1].value == app.deck[card2].value:
        if app.deck[card1].value > 9:
            return 50
        elif app.deck[card1].value > 4:
            return 40
        else:
            return 35
    #same suit cards, potential for a straight flush or a flish
    elif (app.deck[card1].suit == app.deck[card2].suit) and (abs(app.deck[card1].value - app.deck[card2].value) < 3):
        return 30
    elif (app.deck[card1].suit == app.deck[card2].suit) and (abs(app.deck[card1].value - app.deck[card2].value) <= 5):
        return 25
    elif (app.deck[card1].suit == app.deck[card2].suit) and (abs(app.deck[card1].value - app.deck[card2].value) > 5):
        return 15
    #off suit face cards, straight or top pair
    elif (app.deck[card1].value > 9) and (app.deck[card1].value > 9):
        return 25
    #off suit one face card high straight
    elif (abs(app.deck[card1].value - app.deck[card2].value) < 3) and ((app.deck[card1].value > 9) or (app.deck[card1].value > 9)):
        return 15
    #off suit one face low straight chance
    elif (abs(app.deck[card1].value - app.deck[card2].value) <=5) and ((app.deck[card1].value > 9) or (app.deck[card1].value > 9)):
        return 10
    #one face card, high pair potential 
    elif (abs(app.deck[card1].value - app.deck[card2].value) > 5) and ((app.deck[card1].value > 9) or (app.deck[card1].value > 9)):
        return 5
    #low card straight potential 
    elif (abs(app.deck[card1].value - app.deck[card2].value) < 3):
        return 10
    #low card low straight potential
    elif (abs(app.deck[card1].value - app.deck[card2].value) <= 5):
        return 5
    #low card very low hand potential
    elif (abs(app.deck[card1].value - app.deck[card2].value) > 5):
        return 0

#returns a value from 0 to 9, the higher, the better quality of hand
def simPostFlop(app, ai):
    card1 = ai.card1
    card2 = ai.card2
    tableCard1 = app.tableCards[0]
    tableCard2 = app.tableCards[1]
    tableCard3 = app.tableCards[2]
    #create deck indices
    tempDeck = []
    for i in range(0, 52):
        tempDeck.append(i)
    #remove knowns cards to avoid repeat selections
    tempDeck.remove(card1)
    tempDeck.remove(card2)
    tempDeck.remove(tableCard1)
    tempDeck.remove(tableCard2)
    tempDeck.remove(tableCard3)
    #list to create potential table hands
    tempHand = [tableCard1, tableCard2, tableCard3]
    totalScore = 0
    #runs 50 trials with a random turn and river card and computes and average winning hand score
    for i in range(50):
        copyTempDeck = tempDeck + []
        x = random.choice(copyTempDeck)
        copyTempDeck.remove(x)
        y = random.choice(copyTempDeck)
        copyTempDeck.remove(y)
        tempHand.append(x)
        tempHand.append(y)
        score = AIscoreHand(app, ai, tempHand, card1, card2)
        totalScore += score
    avgScore = totalScore/50
    return avgScore
 
#returns a value from 0 to 9, the higher, the better quality of hand
def simPostTurn(app, ai):
    card1 = ai.card1
    card2 = ai.card2
    tableCard1 = app.tableCards[0]
    tableCard2 = app.tableCards[1]
    tableCard3 = app.tableCards[2]
    tableCard4 = app.tableCards[3]
    #create deck indices
    tempDeck = []
    for i in range(0, 52):
        tempDeck.append(i)
    #remove knowns cards to avoid repeat selections
    tempDeck.remove(card1)
    tempDeck.remove(card2)
    tempDeck.remove(tableCard1)
    tempDeck.remove(tableCard2)
    tempDeck.remove(tableCard3)
    tempDeck.remove(tableCard4)
    #list to create potential table hands
    tempHand = [tableCard1, tableCard2, tableCard3, tableCard4]
    totalScore = 0
    #runs 50 trials with a random turn and river card and computes and average winning hand score
    for i in range(50):
        copyTempDeck = tempDeck + []
        x = random.choice(copyTempDeck)
        copyTempDeck.remove(x)
        tempHand.append(x)
        score = AIscoreHand(app, ai, tempHand, ai.card1, ai.card2)
        totalScore += score
    avgScore = totalScore/50
    return avgScore

#returns a value from 0 to 1 which is the probability of winning the hand based on sims
def simPostRiver(app, ai):
    aiScore = AIscoreHand(app, ai, app.tableCards, ai.card1, ai.card2)
    card1 = ai.card1
    card2 = ai.card2
    tableCard1 = app.tableCards[0]
    tableCard2 = app.tableCards[1]
    tableCard3 = app.tableCards[2]
    tableCard4 = app.tableCards[3]
    tableCard5 = app.tableCards[4]
    #create deck indices
    tempDeck = []
    for i in range(0, 52):
        tempDeck.append(i)
    #remove knowns cards to avoid repeat selections
    tempDeck.remove(card1)
    tempDeck.remove(card2)
    tempDeck.remove(tableCard1)
    tempDeck.remove(tableCard2)
    tempDeck.remove(tableCard3)
    tempDeck.remove(tableCard4)
    tempDeck.remove(tableCard5)
    totalScore = 0
    for i in range(50):
        copyTempDeck = tempDeck + []
        x = random.choice(copyTempDeck)
        copyTempDeck.remove(x)
        y = random.choice(copyTempDeck)
        copyTempDeck.remove(y)
        simScore = AIscoreHand(app, ai, app.tableCards, x, y)
        if simScore < aiScore:
            totalScore += 1
    winningProbability = totalScore/50
    return winningProbability


#modified version of scoreHand used for AI simulations
def AIscoreHand(app, player, hand, AICard1, AICard2):
    tableCards = hand
    handCards = [AICard1, AICard2]
    allCards = handCards + tableCards
    spades = []
    clubs = []
    diamonds = []
    hearts = []
    suitsLists = [spades, clubs, diamonds, hearts]
    for num in allCards:
        if app.deck[num].suit == "spades":
            spades.append(app.deck[num])
        elif app.deck[num].suit == "clubs":
            clubs.append(app.deck[num])
        elif app.deck[num].suit == "diamonds":
            diamonds.append(app.deck[num])
        elif app.deck[num].suit == "hearts":
            hearts.append(app.deck[num])
     

    #royal flush/straight flush/flush
    for suit in suitsLists:
        if suit == spades:
            name = "spaces"
        elif suit == clubs:
            name = "clubs"
        elif suit == diamonds:
            name = "diamonds"
        elif suit == hearts:
            name = "hearts"
    
        if len(suit) >= 5:
            if Card(14, f"{name}") in suit and Card(13, f"{name}") in suit and Card(12, f"{name}") in suit and Card(11, f"{name}") in suit and Card(10, f"{name}") in suit:
                return 9
            else:
                numbers = []
                for card in suit:
                    numbers.append(card.value) 
                numbers = sorted(numbers)
                numlength = len(numbers)
                if numlength == 5:
                    if  numbers[0] == (numbers[1]-1) == (numbers[2]-2) == (numbers[3]-3) == (numbers[4]-4):
                        return 9
                elif numlength == 6:
                    if  numbers[0] == (numbers[1]-1) == (numbers[2]-2) == (numbers[3]-3) == (numbers[4]-4): 
                        return 9
                    elif  numbers[1] == (numbers[2]-1) == (numbers[3]-2) == (numbers[4]-3) == (numbers[5]-4): 
                        return 9
                elif numlength == 7:
                    if  numbers[0] == (numbers[1]-1) == (numbers[2]-2) == (numbers[3]-3) == (numbers[4]-4): 
                        return 9
                    elif  numbers[1] == (numbers[2]-1) == (numbers[3]-2) == (numbers[4]-3) == (numbers[5]-4): 
                        return 9
                    elif  numbers[2] == (numbers[3]-1) == (numbers[4]-2) == (numbers[5]-3) == (numbers[6]-4): 
                        return 8
                else:
                    return 5
    
    #quads, full house, straight, trips, two pair, pair, high card
    numberdict = dict()
    for num in allCards:
        card = app.deck[num]
        if card.value in numberdict:
            numberdict[card.value] += 1
        else:
            numberdict[card.value] = 1
    #quads and full house
    for firstkey in numberdict: 
        straightList = []
        for secondkey in numberdict:
            straightList.append(secondkey)
            if numberdict[secondkey] == 4:
                return 7
            elif numberdict[secondkey] == 3 and numberdict[firstkey] == 2:
                return 6
    straightList = sorted(straightList)
    numlength = len(straightList)
    #checks for all possible straight combinations
    if numlength == 5:
        if  straightList[0] == (straightList[1]-1) == (straightList[2]-2) == (straightList[3]-3) == (straightList[4]-4):
            return 4
    elif numlength == 6:
        if  straightList[0] == (straightList[1]-1) == (straightList[2]-2) == (straightList[3]-3) == (straightList[4]-4): 
            return 4
        elif  straightList[1] == (straightList[2]-1) == (straightList[3]-2) == (straightList[4]-3) == (straightList[5]-4): 
            return 4
    elif numlength == 7:
        if  straightList[0] == (straightList[1]-1) == (straightList[2]-2) == (straightList[3]-3) == (straightList[4]-4): 
            return 4
        elif  straightList[1] == (straightList[2]-1) == (straightList[3]-2) == (straightList[4]-3) == (straightList[5]-4): 
            return 4
        elif  straightList[2] == (straightList[3]-1) == (straightList[4]-2) == (straightList[5]-3) == (straightList[6]-4): 
            return 4
    #trips, two pair, pair, high card
    for firstkey in numberdict: 
        for secondkey in numberdict:
            straightList.append(secondkey)
            if numberdict[firstkey] == 3:
                return 3
            elif numberdict[secondkey] == 2 and numberdict[firstkey] == 2:
                return 2
            elif numberdict[firstkey] == 2:
                return 1
    return 0

def easyAI(app, currentRound, ai):
    if app.currBet > ai.money:
        fold(app)
    elif currentRound == "preFlop":
        preFlopScore = simPreFlop(app, ai)
        if ai.blind == "big" and app.currBet == app.bigBlind:
            check(app)
        else:
            if preFlopScore >= 40:
                if app.currBet == app.bigBlind:
                    app.bet = 2*app.bigBlind
                    bet(app)
                else:
                    if preFlopScore > 45 and app.currBet < 4*app.bigBlind:
                        app.bet = 2*app.currBet
                        bet(app)
                    else:
                        call(app)
            elif preFlopScore >= 15:
                call(app)
            else:
                fold(app)

    elif currentRound == "postFlop":
        postFlopScore = simPostFlop(app, ai)
        if postFlopScore > 8:
            if app.currBet <= app.bigBlind:
                app.bet = 3*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postFlopScore > 7:
            if app.currBet <= app.bigBlind:
                app.bet = 2*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postFlopScore > 5 and (app.currBet < 3*app.bigBlind):
            call(app)
        elif postFlopScore > 3 and (app.currBet < 2*app.bigBlind):
            call(app)
        else:
            fold(app)
    
    elif currentRound == "postTurn":
        postTurnScore = simPostTurn(app, ai)
        if postTurnScore > 8:
            if app.currBet <= app.bigBlind:
                app.bet = 3*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postTurnScore > 7:
            if app.currBet <= app.bigBlind:
                app.bet = 2*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postTurnScore > 5 and (app.currBet < 3*app.bigBlind):
            call(app)
        elif postTurnScore > 3 and (app.currBet < 2*app.bigBlind):
            call(app)
        else:
            fold(app)
    
    elif currentRound == "postRiver":
        postRiverScore = simPostRiver(app, ai)
        if postRiverScore > 0.9:
            if app.currBet <= app.bigBlind:
                app.bet = 3*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postRiverScore > 0.8:
            if app.currBet <= app.bigBlind:
                app.bet = 2*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postRiverScore > 0.6:
            if app.currBet <= app.bigBlind:
                app.bet = app.bigBlind
                bet(app)
            else:
                call(app)
        elif postRiverScore > 0.5:
            if app.currBet <= app.bigBlind:
                call(app)
            else:
                fold(app)
        else:
            fold(app)
        

def hardAI(app, currentRound, ai):
    if app.currBet > ai.money:
        fold(app)
    elif currentRound == "preFlop":
        preFlopScore = simPreFlop(app, ai)
        if ai.blind == "big" and app.currBet == app.bigBlind:
            check(app)
        else:
            if preFlopScore >= 40:
                if app.currBet == app.bigBlind:
                    app.bet = 3*app.bigBlind
                    bet(app)
                else:
                    if preFlopScore > 45 and app.currBet < 5*app.bigBlind:
                        app.bet = 3*app.currBet
                        bet(app)
                    else:
                        call(app)
            elif preFlopScore >= 10:
                call(app)
            else:
                fold(app)

    elif currentRound == "postFlop":
        postFlopScore = simPostFlop(app, ai)
        if postFlopScore > 7:
            if app.currBet <= app.bigBlind:
                app.bet = 4*app.bigBlind
                bet(app)
            else:
                app.bet = 3*app.currBet
                bet(app)
        elif postFlopScore > 6:
            if app.currBet <= app.bigBlind:
                app.bet = 3*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postFlopScore > 4 and (app.currBet < 3*app.bigBlind):
            call(app)
        elif postFlopScore > 2 and (app.currBet < 2*app.bigBlind):
            call(app)
        else:
            fold(app)
    
    elif currentRound == "postTurn":
        postTurnScore = simPostTurn(app, ai)
        if postTurnScore > 7:
            if app.currBet <= app.bigBlind:
                app.bet = 4*app.bigBlind
                bet(app)
            else:
                app.bet = 3*app.currBet
                bet(app)
        elif postTurnScore > 6:
            if app.currBet <= app.bigBlind:
                app.bet = 3*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postTurnScore > 4 and (app.currBet < 3*app.bigBlind):
            call(app)
        elif postTurnScore > 3 and (app.currBet < 2*app.bigBlind):
            call(app)
        else:
            fold(app)
    
    elif currentRound == "postRiver":
        postRiverScore = simPostRiver(app, ai)
        if postRiverScore > 0.8:
            if app.currBet <= app.bigBlind:
                app.bet = 3*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postRiverScore > 0.65:
            if app.currBet <= app.bigBlind:
                app.bet = 2*app.bigBlind
                bet(app)
            else:
                app.bet = 2*app.currBet
                bet(app)
        elif postRiverScore > 0.5:
            if app.currBet <= app.bigBlind:
                app.bet = app.bigBlind
                bet(app)
            else:
                call(app)
        elif postRiverScore > 0.4:
            if app.currBet <= app.bigBlind:
                call(app)
            else:
                fold(app)
        else:
            fold(app)
        

"""In game playing functions"""
def dealCards(app):
    numPlayers = len(app.playerList)
    cardsNeeded = numPlayers*2 + 5
    i = 0
    handCards = []
    while i <= cardsNeeded:
        newDigit = random.randint(0,51)
        if newDigit not in handCards:
            handCards.append(newDigit)
            i += 1
    k = 0
    for player in app.playerList:
        player.card1 = handCards[k]
        k += 1
        player.card2 = handCards[k] 
        k += 1
    app.tableCards = handCards[k+1:]

def newHand(app):
    app.currRound = "preFlop"
    app.showRiver = False
    app.winningHand = None
    app.handWinner = None
    for player in app.playerList:
        player.status = "In"
    moveBlinds(app)
    for player in app.playerList:
        if player.blind == "small":
            player.money -= 5
            app.tableMoney += 5
        elif player.blind == "big":
            player.money -= 10
            app.tableMoney += 10
    app.currBet = 10

def nextTurn(app):
    app.ledgerList.append(f"{app.currPlayer} {app.action} ${app.currBet}")
    currPlayingList = []
    for player in app.playerList:
        if player.status == "In":
            currPlayingList.append(player)
    if len(app.roundPlayingList) > 0:
        k = 0
        i = app.playerList.index(app.currPlayer)
        while k < 1:
            nextPlayerIndex = (i+1)%len(app.playerList)
            if app.playerList[nextPlayerIndex].status == "In":
                app.playerList[nextPlayerIndex].turn = True
                app.currPlayer.turn = False
                app.currPlayer = app.playerList[nextPlayerIndex]
                k += 1
            else: 
                i = (i+1)%len(app.playerList)

def nextRound(app):
    app.roundTurnsLeft = len(app.roundPlayingList)
    index = app.roundList.index(app.currRound)  
    nextRoundIndex = (index + 1)%len(app.roundList)
    #checks if the next round will be a new hand or not
    if nextRoundIndex == 0 and app.currRound == "postRiver":
        endOfHand(app)
        app.currBet = 0
        newHand(app)
        #moveBlinds(app)
        app.currPlayer = newRoundCurrPlayer(app)
        dealCards(app)

    else:
        app.currRound = app.roundList[nextRoundIndex]
        app.currBet = 0


    if app.currRound == "preFlop":
        dealCards(app)
        app.roundPlayingList = app.playerList + []
        app.showRiver = False
        app.showTurn = False
        app.showFlop = False
        app.roundTurnsLeft = len(app.roundPlayingList)
        

    elif app.currRound == "postFlop":
        app.showFlop = True
        app.roundTurnsLeft = len(app.roundPlayingList)
        

    elif app.currRound == "postTurn":
        app.showFlop = False
        app.showTurn = True
        app.roundTurnsLeft = len(app.roundPlayingList)
        

    elif app.currRound == "postRiver":
        app.showTurn = False
        app.showRiver = True
        app.roundTurnsLeft = len(app.roundPlayingList)
        
def scoreHand(app, player):
    tableCards = app.tableCards
    handCards = [player.card1, player.card2]
    allCards = handCards + tableCards
    spades = []
    clubs = []
    diamonds = []
    hearts = []
    suitsLists = [spades, clubs, diamonds, hearts]
    for card in allCards:
        if app.deck[card].suit == "spades":
            spades.append(app.deck[card])
        elif app.deck[card].suit == "clubs":
            clubs.append(app.deck[card])
        elif app.deck[card].suit == "diamonds":
            diamonds.append(app.deck[card])
        elif app.deck[card].suit == "hearts":
            hearts.append(app.deck[card])
     

    #royal flush/straight flush/flush
    for suit in suitsLists:
        if suit == spades:
            name = "spaces"
        elif suit == clubs:
            name = "clubs"
        elif suit == diamonds:
            name = "diamonds"
        elif suit == hearts:
            name = "hearts"
    
        if len(suit) >= 5:
            if Card(14, f"{name}") in suit and Card(13, f"{name}") in suit and Card(12, f"{name}") in suit and Card(11, f"{name}") in suit and Card(10, f"{name}") in suit:
                return 9, 14, "royal flush"
            else:
                numbers = []
                for card in suit:
                    numbers.append(card.value) 
                numbers = sorted(numbers)
                numlength = len(numbers)
                if numlength == 5:
                    if  numbers[0] == (numbers[1]-1) == (numbers[2]-2) == (numbers[3]-3) == (numbers[4]-4):
                        return 9, numbers[4], "straight flush"
                elif numlength == 6:
                    if  numbers[0] == (numbers[1]-1) == (numbers[2]-2) == (numbers[3]-3) == (numbers[4]-4): 
                        return 9, numbers[4], "straight flush"
                    elif  numbers[1] == (numbers[2]-1) == (numbers[3]-2) == (numbers[4]-3) == (numbers[5]-4): 
                        return 9, numbers[5], "straight flush"
                elif numlength == 7:
                    if  numbers[0] == (numbers[1]-1) == (numbers[2]-2) == (numbers[3]-3) == (numbers[4]-4): 
                        return 9, numbers[4], "straight flush"
                    elif  numbers[1] == (numbers[2]-1) == (numbers[3]-2) == (numbers[4]-3) == (numbers[5]-4): 
                        return 9, numbers[5], "straight flush"
                    elif  numbers[2] == (numbers[3]-1) == (numbers[4]-2) == (numbers[5]-3) == (numbers[6]-4): 
                        return 8, numbers[6], "straight flush"
                else:
                    return 5, max(numbers), "flush"
    
    #quads, full house, straight, trips, two pair, pair, high card
    numberdict = dict()
    for num in allCards:
        card = app.deck[num]
        if card.value in numberdict:
            numberdict[card.value] += 1
        else:
            numberdict[card.value] = 1
    #quads and full house
    for firstkey in numberdict: 
        straightList = []
        for secondkey in numberdict:
            straightList.append(secondkey)
            if numberdict[secondkey] == 4:
                return 7, secondkey, "four of a kind"
            elif numberdict[secondkey] == 3 and numberdict[firstkey] == 2:
                return 6, secondkey, "full house"
    straightList = sorted(straightList)
    numlength = len(straightList)
    #checks for all possible straight combinations
    if numlength == 5:
        if  straightList[0] == (straightList[1]-1) == (straightList[2]-2) == (straightList[3]-3) == (straightList[4]-4):
            return 4, straightList[4], "straight"
    elif numlength == 6:
        if  straightList[0] == (straightList[1]-1) == (straightList[2]-2) == (straightList[3]-3) == (straightList[4]-4): 
            return 4, straightList[4], "straight"
        elif  straightList[1] == (straightList[2]-1) == (straightList[3]-2) == (straightList[4]-3) == (straightList[5]-4): 
            return 4, straightList[5], "straight"
    elif numlength == 7:
        if  straightList[0] == (straightList[1]-1) == (straightList[2]-2) == (straightList[3]-3) == (straightList[4]-4): 
            return 4, straightList[4], "straight"
        elif  straightList[1] == (straightList[2]-1) == (straightList[3]-2) == (straightList[4]-3) == (straightList[5]-4): 
            return 4, straightList[5], "straight"
        elif  straightList[2] == (straightList[3]-1) == (straightList[4]-2) == (straightList[5]-3) == (straightList[6]-4): 
            return 4, straightList[6], "straight"
    #trips, two pair, pair, high card
    for firstkey in numberdict: 
        for secondkey in numberdict:
            straightList.append(secondkey)
            if numberdict[firstkey] == 3:
                return 3, firstkey, "three of a kind"
            elif numberdict[secondkey] == 2 and numberdict[firstkey] == 2:
                return 2, max(secondkey, firstkey), "two pair"
            elif numberdict[firstkey] == 2:
                return 1, firstkey, "pair"
    return 0, max(player.card1, player.card2), "high card"

def winningHand(app):
    winningtotal = -1
    highnumber = 0
    for player in app.roundPlayingList:
        total, highcard, handType = scoreHand(app, player)
        if total > winningtotal:
            winningtotal = total
            highnumber = highcard
            app.handWinner = player
            app.betterHand = handType
        elif total == winningtotal:
            if highcard > highnumber:
                winningtotal = total
                highnumber = highcard
                app.handWinner = player
                app.betterHand = handType
            
def endOfHand(app):
    if len(app.roundPlayingList) == 1:
        app.handWinner = app.roundPlayingList[0]
        app.handWinner.money += app.tableMoney
        app.tableMoney = 0
        app.ledgerList.append(f"{app.handWinner} won the round!")
    else:
        #compares value of hand
        winningHand(app)
        app.handWinner.money += app.tableMoney
        app.tableMoney = 0
        app.ledgerList.append(f"{app.handWinner} won the round with a {app.betterHand}!")

def assignBlinds(app):
    for i in range(len(app.playerList)):
        if app.playerList[i].blind == "small":
            smallBlindIndex = i
    bigBlindIndex = (i+1)%(len(app.playerList))
    app.playerList[bigBlindIndex].blind = "big"
    app.playerList[bigBlindIndex].money -= 10
    app.playerList[smallBlindIndex].money -= 5
    app.currBet = 10
    app.tableMoney += 15

def moveBlinds(app):
    for i in range(len(app.playerList)):
        if app.playerList[i].blind == "small":
            smallBlindIndex = i
    newSmallBlindIndex = (smallBlindIndex+1)%(len(app.playerList))
    newBigBlindIndex = (smallBlindIndex+2)%(len(app.playerList))
    app.playerList[newBigBlindIndex].blind = "big"
    app.playerList[newSmallBlindIndex].blind = "small"
    app.playerList[smallBlindIndex].blind = None
    
def newRoundCurrPlayer(app):
    for i in range(len(app.playerList)):
        if app.playerList[i].blind == "big":
            bigBlindIndex = i
    nextPlayer = (bigBlindIndex + 1)%len(app.playerList)
    return app.playerList[nextPlayer]

def main():
    runApp(width = 800, height = 800)

main()