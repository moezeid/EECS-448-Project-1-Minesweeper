
# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
from workspace.tile import tile
from workspace.executive import executive
from GUI.inputgui import inputGui
from tkinter import *

import pygame
import os.path
import uuid
import time
import random
import datetime
import os.path

def print_board2():
    screen.fill(DARKGREY)

    for i in range(row):
        for j in range(column):
            color = GREY

            if exe.cheatBoard.board[j][i].isVisible == False:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])

            if exe.cheatBoard.board[j][i].isVisible == True:
                color = WHITE
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
            if exe.cheatBoard.board[j][i].isBomb == True and exe.cheatBoard.board[j][i].isVisible == True:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                temp = grid[j][i].move(-5, -5)
                screen.blit(bomb, temp)
            if exe.cheatBoard.board[j][i].adjBomb > 0 and exe.cheatBoard.board[j][i].isVisible == True:
                temp = grid[j][i].move(5, 5)
                screen.blit(font.render(str(exe.cheatBoard.board[j][i].adjBomb), True, BLACK), (temp))
            if exe.cheatBoard.board[j][i].isFlagged == True and exe.cheatBoard.board[j][i].isVisible == False:
                screen.blit(flag, grid[j][i])

    pygame.draw.rect(screen, (255, 255, 255),
                     ((column * 20 + MARGIN * column + MARGIN), 0, 100,50))
    pygame.display.flip()


pygame.init()
pygame.display.init()


def print_board():
    """ handles printing of board. prints updated board onto screen with
    each successive move """
    screen.fill(DARKGREY)
    for i in range(row):
        for j in range(column):
            color = GREY

            if exe.gameBoard.board[j][i].isVisible == False:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])

            if exe.gameBoard.board[j][i].isVisible == True:
                color = WHITE
                grid[j][i] =  pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
            if exe.gameBoard.board[j][i].isBomb == True and exe.gameBoard.board[j][i].isVisible == True :
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                temp = grid[j][i].move(-5, -5)
                screen.blit(bomb, temp)
            if exe.gameBoard.board[j][i].adjBomb >  0 and exe.gameBoard.board[j][i].isVisible == True:
                temp = grid[j][i].move(5,5)
                screen.blit(font.render(str(exe.gameBoard.board[j][i].adjBomb), True, BLACK), (temp))
            if exe.gameBoard.board[j][i].isFlagged == True and exe.gameBoard.board[j][i].isVisible == False:
                screen.blit(flag,grid[j][i])
    pygame.draw.rect(screen, (255, 255, 255), ((column * 20 + MARGIN * column + MARGIN), 0, 100, 50))
    pygame.display.flip()


pygame.init()
pygame.display.init()

"""definition of colors
"""
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
BLACK = (0, 0, 0)
DARKGREY = (169, 169, 169)

# tile width and height constant
WIDTH = 20
HEIGHT = 20

# margin between tiles
MARGIN = 5

w=2
h=2
b=1
incorrect = True
clickCount = 0
#sound effects
winSound = pygame.mixer.Sound("soundEffects/Applause.wav")
loseSound = pygame.mixer.Sound("soundEffects/Explosion.wav")
revealSound = pygame.mixer.Sound("soundEffects/Click.wav")
flagSound = pygame.mixer.Sound("soundEffects/Ding-flag.wav")

while (incorrect == True):
    try:
        screen = Tk()
        screen.iconbitmap(r'GUI\MemoryLeakLogo.ico')
        inputScreen = inputGui(screen)
        screen.protocol("WM_DELETE_WINDOW", sys.exit)
        screen.mainloop()
        w = int(inputScreen.getWidth())
        h = int(inputScreen.getHeight())
        b = int(inputScreen.getBombNum())
        if (40>= w >= 2) and (72>= h >= 2) and (b >= 1) and 1 <= ((w*h)-b) <= 1088:
            incorrect = False
        if(incorrect == True):
            raise ValueError()
        break;
    except ValueError:
        badCase = Tk()
        badCase.iconbitmap(r'GUI\MemoryLeakLogo.ico')
        required = 1
        if ((w * h) > 1088):
            required = (w*h) - 1088
        Label(badCase, text="Please enter a valid integer.\n1<Width<73 and 1<Height<41\nMust "
                            "have at least " + str(required) + " bomb(s) with that size." , ).grid(row=0)
        Button(badCase, text="Ok", command=badCase.destroy).grid(row=1)
        badCase.mainloop()





"""calculate the required screen size based on amount of tiles
"""
screen_width = (int(w) * 20) + ((int(w)+1)*5)
screen_height = (int(h) * 20) + ((int(h)+1)*5 + 100)

""" create the screen surface
"""
size =  screen_height, screen_width
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pysweeper")
icon = pygame.image.load("GUI/MemoryLeakLogo.png")
pygame.display.set_icon(icon)
"""create tile grid
"""
board = [[tile() for i in range(int(w))]for j in range(int(h))]

"""main draw loop
"""
program_end = False
font = pygame.font.SysFont('Ariel', 22)

"""looping multiple rects
"""
row = int(w)
column = int(h)

"""game logic grid
"""
grid = [[0] * row for i in range(column)]
bomb = pygame.image.load("GUI/bomb.png")
flag = pygame.image.load("GUI/flag.png")


"""Sets clock rate
"""

top_five =[""]*5;
top_five_count =0;
second =0
clockTick = pygame.USEREVENT+1
pygame.time.set_timer(clockTick, 1000)



clock = pygame.time.Clock()
exe = executive(int(w), int(h), int(b))
exe.run()
gamestate = 0
cheatMode= 0
"""Main game loop
"""
start=time.time()



while not program_end and gamestate == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                pos = pygame.mouse.get_pos()
                originalc = pos[0]
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)
                if(c >= column):
                    c = column - 1
                if(r >= row):
                    r = row - 1
                if (originalc > (WIDTH + MARGIN) * column):
                    if (cheatMode == 0):
                        cheatMode = 1
                        exe.cheatBoard.reveal_all()
                        # print_board2()
                    else:
                        cheatMode = 0
                else:
                    if (cheatMode == 1):
                        cheat1 = Tk()
                        cheat1.iconbitmap('GUI/MemoryLeakLogo.ico')
                        Label(cheat1, text="please exit the cheatMode first!", ).grid(row=0)
                        cheat1.mainloop()
                    else:
                        exe.gameBoard.reveal_tile(c,r)
                        revealSound.play()
                        revealSound.set_volume(0.1)
                        clickCount += 1

            elif(event.button == 3):
                pos = pygame.mouse.get_pos()
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)
                exe.gameBoard.flag_tile(c,r)
                flagSound.play()
                flagSound.set_volume(0.1)

            # print_board()
    if (cheatMode == 1):
        print_board2()
    else:
        print_board()
    gamestate = exe.checkWinLose()

    clock.tick(60)

if (gamestate == 2):


    end = time.time()
    timeTaken = (end - start)

    timeApprox = round(timeTaken, 2)
    timeApproxStr = str(timeApprox)

    clickRate = clickCount / timeTaken

    clickRateApprox = round(clickRate, 2)
    clickRateStr = str(clickRateApprox)

    score = 100 * clickRateApprox
    score = round(score, 2)
    score = str(score)

    scoreMsg = "Not so great. \n  You took " + timeApproxStr
    scoreMsg = scoreMsg + " seconds to lose. \n You clicked at a rate of "
    scoreMsg = scoreMsg + clickRateStr
    scoreMsg = scoreMsg + " clicks/sec \n This means your score is: " + score + "\n keep in mind "
    scoreMsg = scoreMsg + "only winning scores are recorded."

    exe.gameBoard.reveal_all()
    print_board()
    loseCase = Tk()
    loseCase.iconbitmap('GUI/MemoryLeakLogo.ico')
    loseSound.play()
    loseSound.set_volume(1.0)
    Label(loseCase, text="YOU LOSE!!", ).grid(row=0, column=1)
    Label(loseCase, text=scoreMsg, ).grid(row=1, column=1)
    loseCase.mainloop()
elif (gamestate == 1):
    textFileName = str(row) + "x" + str(column) + " Scores.txt"
    end = time.time()
    timeTaken = (end - start)

    timeApprox = round(timeTaken, 2)
    timeApproxStr = str(timeApprox)

    clickRate = clickCount / timeTaken

    clickRateApprox = round(clickRate, 2)
    clickRateStr = str(clickRateApprox)

    score = 100*clickRateApprox
    score = round(score, 2)
    score = str(score)
    winFileMsg = "You took " + timeApproxStr + " seconds to finish. \n You click at a rate of "
    winFileMsg = winFileMsg + clickRateStr
    winFileMsg = winFileMsg + " clicks/sec \n This means your score is: " + score
    scoreMsg = "Nice job. \n  You took " + timeApproxStr
    scoreMsg = scoreMsg + " seconds to finish. \n You click at a rate of "
    scoreMsg = scoreMsg + clickRateStr
    scoreMsg = scoreMsg + " clicks/sec \n This means your score is: " + score

    winCase = Tk()
    winCase.iconbitmap('GUI/MemoryLeakLogo.ico')
    Label(winCase, text="YOU WIN!!", ).grid(row=0 ,column=1)
    Label(winCase, text=scoreMsg,).grid(row=1, column=1)


    if(os.path.isfile(textFileName) != True):
        text_file = open(textFileName, "w")
        text_file.write(score+'\n')
        text_file.close()

    else:
        with open(textFileName, 'r+') as file:
            content = file.readlines()
            for temp in content:
                top_five_count = top_five_count+1

            if(top_five_count < 5):
                top_five_count = top_five_count + 1
                for i in range(top_five_count-1):
                    top_five[i] = content[i].replace('\n','')
                top_five[top_five_count-1] = score
                top_five.sort(reverse=True)
                file.seek(0)
                for i in range(top_five_count):
                    file.write(str(top_five[i])+'\n')
                file.truncate()

            else:

                for i in range(5):
                    top_five[i] = content[i].replace('\n','')
                top_five.sort(reverse=True)
                if(float(score) > float(top_five[top_five_count-1])):
                    top_five[top_five_count-1] = score;
                    top_five.sort(reverse=True)
                file.seek(0)
                for i in range(5):
                    file.write(str(top_five[i])+'\n')
                file.truncate()

    print('The highest score in '+ str(row)+'x'+str(column)+' board is:' + top_five[0])
    winSound.play()
    winSound.set_volume(1.0)
    winCase.mainloop()

end = time.time()

pygame.quit()
