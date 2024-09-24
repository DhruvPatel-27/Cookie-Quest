

import pygame, random, math

#Pygame Global Variables
WIDTH, HEIGHT = (1280, 720) #size of the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #the surface that everything is drawn on
FPS = 60 #frames per second of the game


#This function is used to initialize variables or objects before the game begins
def init():
    gameStates()
    loadAssets()
    initLevel()
    initGrid()
    gridPosition()
    timer()
    initCookies()
    initEnemy()
    initMenuSelector()
    initSound()

#Initializes all the variables associated with states
def gameStates():
    global MENU_STATE, PLAY_STATE, QUIT_STATE, WIN_STATE, LOSE_STATE, FINISH_STATE, gameState, fontLose
    MENU_STATE, PLAY_STATE, QUIT_STATE, WIN_STATE, LOSE_STATE, FINISH_STATE = (0, 1, 2, 3, 4, 5)
    gameState = MENU_STATE

    fontLose = pygame.font.SysFont("Comic Sans ms", 32)

#Loads all the assets used in the game
def loadAssets():
    global blocks, bg, PLAYER_INDEX, ENEMY_INDEX, DEATH_INDEX, CHECKERED_INDEX, JAIL_INDEX, COOKIE_INDEX, WALL_INDEX, WARP_INDEX, BG_INDEX, MENU_INDEX, WIN_INDEX, FINISH_INDEX
    blocks = []
    bg = []

    blocks.append(pygame.image.load("playerblock.png"))
    blocks.append(pygame.image.load("enemyblock.png"))
    blocks.append(pygame.image.load("deathblock.png"))
    blocks.append(pygame.image.load("checkeredblock.png"))
    blocks.append(pygame.image.load("jailblock.png"))
    blocks.append(pygame.image.load("cookie.png"))
    blocks.append(pygame.image.load("wallblock.png"))
    blocks.append(pygame.image.load("warpblock.png"))


    bg.append(pygame.image.load("bg.png"))
    bg.append(pygame.image.load("menu.png"))
    bg.append(pygame.image.load("winstatebg.png"))
    bg.append(pygame.image.load("finishstatebg.png"))

    PLAYER_INDEX, ENEMY_INDEX, DEATH_INDEX, CHECKERED_INDEX, JAIL_INDEX, COOKIE_INDEX, WALL_INDEX, WARP_INDEX = (0, 1, 2, 3, 4, 5, 6, 7)

    BG_INDEX, MENU_INDEX, WIN_INDEX, FINISH_INDEX = (0, 1, 2, 3)

#Initializes the level
def initLevel():
    global level, fontLevel
    level = 1
    fontLevel = pygame.font.SysFont("Comic San ms", 50)

#Initializes the grid, grid specs, and reads the level text file
def initGrid():
    global levelGrid, textFile, gridPos, BLOCK_SPACING, playerIndexRow, playerIndexCol, enemy1IndexRow, enemy1IndexCol, enemy2IndexCol, enemy2IndexRow, jailIndexRow, jailIndexCol
    levelGrid = []
    textFile = "level1.txt"
    BLOCK_SPACING = 32
    playerIndexRow, playerIndexCol, enemy1IndexRow, enemy1IndexCol, enemy2IndexCol, enemy2IndexRow = [-1, -1, -1, -1, -1, -1]
    if level == 2:
        textFile = "level2.txt"
    if level == 3:
        textFile = "level3.txt"
    with open(textFile, 'r') as fh:  # opens the file and the variable fh (file handler)
        for line in fh:
            row = []
            for char in line.strip():
                row.append(char)
            levelGrid.append(row)


    if 8 <= (len(levelGrid)) <= 12:
        blocksWidth = len(levelGrid[0]) * BLOCK_SPACING
        blocksHeight = (len(levelGrid) / 2) * BLOCK_SPACING
        x = WIDTH / 2 - blocksWidth / 2
        y = (HEIGHT-160) / 2 - blocksHeight / 2 + BLOCK_SPACING
        gridPos = (y, x)
    else:
        blocksWidth = len(levelGrid[0]) * (BLOCK_SPACING+0.15)
        blocksHeight = (len(levelGrid) / 2) * BLOCK_SPACING
        x = WIDTH / 2 - blocksWidth / 2
        y = (HEIGHT - 160) / 2 - blocksHeight / 2
        gridPos = (y, x)


#Initializes and finds the position of the enemy, player, and jail in the grid
def gridPosition():
    global levelGrid, playerIndexRow, playerIndexCol, enemy1IndexRow, enemy1IndexCol, enemy2IndexRow, enemy2IndexCol, jailIndexRow, jailIndexCol, enemies1Row, enemies1Col, enemies2Row, enemies2Col
    playerIndexRow, playerIndexCol, enemy1IndexRow, enemy1IndexCol, enemy2IndexCol, enemy2IndexRow,  jailIndexCol, jailIndexRow = [-1, -1, -1, -1, -1, -1,  -1, -1]
    enemies1Row = []
    enemies1Col = []
    enemies2Row = []
    enemies2Col = []

    for i in range(len(levelGrid)):
        for j in range(len(levelGrid[0])):
            if levelGrid[i][j] == "p":
                playerIndexRow = i
                playerIndexCol = j
            elif levelGrid[i][j] == "1":
                enemy1IndexRow = i
                enemy1IndexCol = j
                enemies1Row.append(i)
                enemies1Col.append(j)
            elif levelGrid[i][j] == "2":
                enemy2IndexRow = i
                enemy2IndexCol = j
                enemies2Row.append(i)
                enemies2Col.append(j)
            elif levelGrid[i][j] == "e":
                jailIndexRow = i
                jailIndexCol = j



#Initalizes the timer
def timer():
    global timer, fontTimer, colourTime, clockTime
    timer = math.ceil(len(levelGrid) * len(levelGrid[0]) * 0.20)
    clockTime = 0
    fontTimer = pygame.font.SysFont("Comic San ms", 50)
    colourTime = (255, 255, 255)

#Initializes the cookie and the random location of the cookie
def initCookies():
    global cookies, fontCookies, cookieRow, cookieCol
    cookies = 0
    fontCookies = pygame.font.SysFont("Comic San ms", 50)
    cookieRow = random.randint(1, len(levelGrid) - 2)
    cookieCol = random.randint(1, len(levelGrid[0]) - 2)


#Initializes the enemy and its speed
def initEnemy():
    global verticalAmountOne, verticalAmountTwo, verticalAmountThree, verticalAmountFour, verticalAmountFive, horizontalAmountOne, horizontalAmountTwo, horizontalAmountThree, horizontalAmountFour, horizontalAmountFive
    verticalAmountOne, verticalAmountTwo, verticalAmountThree, verticalAmountFour, verticalAmountFive = [1, 1, 1, 1, 1]
    horizontalAmountOne, horizontalAmountTwo, horizontalAmountThree, horizontalAmountFour, horizontalAmountFive = [1, 1, 1, 1, 1]


#Initializes the menu selector and its specs
def initMenuSelector():
    global selectorPos, selectorIndex, xPos, yPos, blockPos
    xPos, yPos = (550, 420)
    blockPos = (xPos, yPos)
    selectorPos = blockPos
    selectorIndex = 0

#Initializes the sound tracks used throughout the game
def initSound():
    global playerMovementSound, deathSound, winSound, unlockGoalSound, timerSound, playerNCookie, enemyNCookie
    playerMovementSound = pygame.mixer.Sound("playermovement.wav")
    deathSound = pygame.mixer.Sound("deathsound.wav")
    winSound = pygame.mixer.Sound("winsound.wav")
    unlockGoalSound = pygame.mixer.Sound("unlockgoal.wav")
    timerSound = pygame.mixer.Sound("timer.wav")
    playerNCookie = pygame.mixer.Sound("playerncookie.wav")
    enemyNCookie = pygame.mixer.Sound("enemyncookie.wav")


#This function is used to modify the data portions of things shown on screen
def update():
    updateClockNCookie()
    resetGame()
    playerNCookieCollision()

#Updates the timer and manages other aspects of the game regarding game state and cookies
def updateClockNCookie():
    global timer, colourTime, gameState, PLAYER_INDEX, JAIL_INDEX, unlockGoalSound
    if gameState == PLAY_STATE:
        timer = timer - 1/60
    if timer <= 3.5:
        colourTime = (255, 0, 0)
    if 2 <= timer <= 3:
        timerSound.play()
    if timer <= 0:
        deathSound.play()
        PLAYER_INDEX = DEATH_INDEX
        drawGrid()
        timer = 0
    if PLAYER_INDEX == DEATH_INDEX:
        gameState = LOSE_STATE
    if cookies >= 5:
        JAIL_INDEX = CHECKERED_INDEX
    if gameState == PLAY_STATE:
        if clockTime % 5 == 0:
            enemyMovementHorNCollision_One()
            enemyMovementHorNCollision_Two()
            enemyMovementHorNCollision_Three()
            enemyMovementHorNCollision_Four()
            enemyMovementHorNCollision_Five()
        if clockTime % 3 == 0:
            enemyMovementVerNCollision_One()
            enemyMovementVerNCollision_Two()
            enemyMovementVerNCollision_Three()
            enemyMovementVerNCollision_Four()
            enemyMovementVerNCollision_Five()


#Reset the game specs if the players dies or wants to play again
def resetGame():
    global timer, level, cookies, PLAYER_INDEX, cookieRow, cookieCol, colourTime, JAIL_INDEX, CHECKERED_INDEX
    if gameState == LOSE_STATE or gameState == FINISH_STATE:
        level = 1
        initGrid()
        gridPosition()
        enemyMovementHorNCollision_One()
        enemyMovementHorNCollision_Two()
        enemyMovementHorNCollision_Three()
        enemyMovementHorNCollision_Four()
        enemyMovementHorNCollision_Five()
        enemyMovementVerNCollision_One()
        enemyMovementVerNCollision_Two()
        enemyMovementVerNCollision_Three()
        enemyMovementVerNCollision_Four()
        enemyMovementVerNCollision_Five()
        cookies = 0
        timer = math.ceil(len(levelGrid) * len(levelGrid[0]) * 0.15)
        PLAYER_INDEX = 0
        JAIL_INDEX = 4
        CHECKERED_INDEX = 3
        colourTime = (255, 255, 255)
        cookieRow = random.randint(1, len(levelGrid) - 2)
        cookieCol = random.randint(1, len(levelGrid[0]) - 2)
        if levelGrid[cookieRow][cookieCol] != "_":
            cookieRow = random.randint(1, len(levelGrid) - 2)
            cookieCol = random.randint(1, len(levelGrid[0]) - 2)


#Moves enemy # "1"; the first enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementHorNCollision_One():
    global nextPos, levelGrid, numberOfBlocks, horizontalAmountOne, enemies1Col, enemies1Row, PLAYER_INDEX, cookieRow, cookieCol
    if enemies1Col != []:
        nextPos = enemies1Col[0] + horizontalAmountOne
        if levelGrid[enemies1Row[0]][nextPos] == "_":
            temp = levelGrid[enemies1Row[0]][enemies1Col[0]]
            levelGrid[enemies1Row[0]][enemies1Col[0]] = levelGrid[enemies1Row[0]][nextPos]
            levelGrid[enemies1Row[0]][nextPos] = temp
            enemies1Col[0] = enemies1Col[0] + horizontalAmountOne
        elif levelGrid[cookieRow][cookieCol] == "1":
            enemyNCookie.play()
        elif levelGrid[enemies1Row[0]][nextPos] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[enemies1Row[0]][nextPos] == "x":
            horizontalAmountOne = horizontalAmountOne * -1



#Moves enemy # "1"; the second enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementHorNCollision_Two():
    global nextPos, levelGrid, numberOfBlocks, horizontalAmountTwo, enemies1Col, enemies1Row, PLAYER_INDEX
    if len(enemies1Col) >= 2:
        nextPos = enemies1Col[1] + horizontalAmountTwo
        if levelGrid[enemies1Row[1]][nextPos] == "_":
            temp = levelGrid[enemies1Row[1]][enemies1Col[1]]
            levelGrid[enemies1Row[1]][enemies1Col[1]] = levelGrid[enemies1Row[1]][nextPos]
            levelGrid[enemies1Row[1]][nextPos] = temp
            enemies1Col[1] = enemies1Col[1] + horizontalAmountTwo
        elif levelGrid[cookieRow][cookieCol] == "1":
            enemyNCookie.play()
        elif levelGrid[enemies1Row[1]][nextPos] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[enemies1Row[1]][nextPos] == "x":
            horizontalAmountTwo = horizontalAmountTwo * -1


#Moves enemy # "1"; the third enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementHorNCollision_Three():
    global nextPos, levelGrid, numberOfBlocks, horizontalAmountThree, enemies1Col, enemies1Row, PLAYER_INDEX
    if len(enemies1Col) >= 3:
        nextPos = enemies1Col[2] + horizontalAmountThree
        if levelGrid[enemies1Row[2]][nextPos] == "_":
            temp = levelGrid[enemies1Row[2]][enemies1Col[2]]
            levelGrid[enemies1Row[2]][enemies1Col[2]] = levelGrid[enemies1Row[2]][nextPos]
            levelGrid[enemies1Row[2]][nextPos] = temp
            enemies1Col[2] = enemies1Col[2] + horizontalAmountThree
        elif levelGrid[cookieRow][cookieCol] == "1":
            enemyNCookie.play()
        elif levelGrid[enemies1Row[2]][nextPos] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[enemies1Row[2]][nextPos] == "x":
            horizontalAmountThree = horizontalAmountThree * -1


#Moves enemy # "1"; the fourth enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementHorNCollision_Four():
    global nextPos, levelGrid, numberOfBlocks, horizontalAmountFour, enemies1Col, enemies1Row, PLAYER_INDEX
    if len(enemies1Col) >= 4:
        nextPos = enemies1Col[3] + horizontalAmountFour
        if levelGrid[enemies1Row[3]][nextPos] == "_":
            temp = levelGrid[enemies1Row[3]][enemies1Col[3]]
            levelGrid[enemies1Row[3]][enemies1Col[3]] = levelGrid[enemies1Row[3]][nextPos]
            levelGrid[enemies1Row[3]][nextPos] = temp
            enemies1Col[3] = enemies1Col[3] + horizontalAmountFour
        elif levelGrid[cookieRow][cookieCol] == "1":
            enemyNCookie.play()
        elif levelGrid[enemies1Row[3]][nextPos] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[enemies1Row[3]][nextPos] == "x":
            horizontalAmountFour = horizontalAmountFour * -1


#Moves enemy # "1"; the fifth enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementHorNCollision_Five():
    global nextPos, levelGrid, numberOfBlocks, horizontalAmountFive, enemies1Col, enemies1Row, PLAYER_INDEX
    if len(enemies1Col) >= 5:
        nextPos = enemies1Col[4] + horizontalAmountFive
        if levelGrid[enemies1Row[4]][nextPos] == "_":
            temp = levelGrid[enemies1Row[4]][enemies1Col[4]]
            levelGrid[enemies1Row[4]][enemies1Col[4]] = levelGrid[enemies1Row[4]][nextPos]
            levelGrid[enemies1Row[4]][nextPos] = temp
            enemies1Col[4] = enemies1Col[4] + horizontalAmountFive
        elif levelGrid[cookieRow][cookieCol] == "1":
            enemyNCookie.play()
        elif levelGrid[enemies1Row[4]][nextPos] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[enemies1Row[4]][nextPos] == "x":
            horizontalAmountFive = horizontalAmountFive * -1


#Moves enemy # "2"; the first enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementVerNCollision_One():
    global nextPos, levelGrid, verticalAmountOne, enemies2Col, enemies2Row, PLAYER_INDEX
    if enemies2Row != []:
        nextPos = enemies2Row[0] + verticalAmountOne
        if levelGrid[nextPos][enemies2Col[0]] == "_":
            temp = levelGrid[enemies2Row[0]][enemies2Col[0]]
            levelGrid[enemies2Row[0]][enemies2Col[0]] = levelGrid[nextPos][enemies2Col[0]]
            levelGrid[nextPos][enemies2Col[0]] = temp
            enemies2Row[0] = enemies2Row[0] + verticalAmountOne
        elif levelGrid[cookieRow][cookieCol] == "2":
            enemyNCookie.play()
        elif levelGrid[nextPos][enemies2Col[0]] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[nextPos][enemies2Col[0]] == "x":
            verticalAmountOne = verticalAmountOne * -1

#Moves enemy # "2"; the second enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementVerNCollision_Two():
    global nextPos, levelGrid, verticalAmountTwo, enemies2Col, enemies2Row, PLAYER_INDEX
    if len(enemies2Row) >= 2:
        nextPos = enemies2Row[1] + verticalAmountTwo
        if levelGrid[nextPos][enemies2Col[1]] == "_":
            temp = levelGrid[enemies2Row[1]][enemies2Col[1]]
            levelGrid[enemies2Row[1]][enemies2Col[1]] = levelGrid[nextPos][enemies2Col[1]]
            levelGrid[nextPos][enemies2Col[1]] = temp
            enemies2Row[1] = enemies2Row[1] + verticalAmountTwo
        elif levelGrid[cookieRow][cookieCol] == "2":
            enemyNCookie.play()
        elif levelGrid[nextPos][enemies2Col[1]] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[nextPos][enemies2Col[1]] == "x":
            verticalAmountTwo = verticalAmountTwo * -1


#Moves enemy # "2"; the third enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementVerNCollision_Three():
    global nextPos, levelGrid, verticalAmountThree, enemies2Col, enemies2Row, PLAYER_INDEX
    if len(enemies2Row) >= 3:
        nextPos = enemies2Row[2] + verticalAmountThree
        if levelGrid[nextPos][enemies2Col[2]] == "_":
            temp = levelGrid[enemies2Row[2]][enemies2Col[2]]
            levelGrid[enemies2Row[2]][enemies2Col[2]] = levelGrid[nextPos][enemies2Col[2]]
            levelGrid[nextPos][enemies2Col[2]] = temp
            enemies2Row[2] = enemies2Row[2] + verticalAmountThree
        elif levelGrid[cookieRow][cookieCol] == "2":
             enemyNCookie.play()
        elif levelGrid[nextPos][enemies2Col[2]] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[nextPos][enemies2Col[2]] == "x":
            verticalAmountThree = verticalAmountThree * -1


#Moves enemy # "2"; the fourth enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementVerNCollision_Four():
    global nextPos, levelGrid, verticalAmountFour, enemies2Col, enemies2Row, PLAYER_INDEX
    if len(enemies2Row) >= 4:
        nextPos = enemies2Row[3] + verticalAmountFour
        if levelGrid[nextPos][enemies2Col[3]] == "_":
            temp = levelGrid[enemies2Row[3]][enemies2Col[3]]
            levelGrid[enemies2Row[3]][enemies2Col[3]] = levelGrid[nextPos][enemies2Col[3]]
            levelGrid[nextPos][enemies2Col[3]] = temp
            enemies2Row[3] = enemies2Row[3] + verticalAmountFour
        elif levelGrid[cookieRow][cookieCol] == "2":
            enemyNCookie.play()
        elif levelGrid[nextPos][enemies2Col[3]] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[nextPos][enemies2Col[3]] == "x":
            verticalAmountFour = verticalAmountFour * -1


#Moves enemy # "2"; the fifth enemy in the list and checks collision with wall, player, and cookie if it is in its path
def enemyMovementVerNCollision_Five():
    global nextPos, levelGrid, verticalAmountFive, enemies2Col, enemies2Row, PLAYER_INDEX
    if len(enemies2Row) == 5:
        nextPos = enemies2Row[4] + verticalAmountFive
        if levelGrid[nextPos][enemies2Col[4]] == "_":
            temp = levelGrid[enemies2Row[4]][enemies2Col[4]]
            levelGrid[enemies2Row[4]][enemies2Col[4]] = levelGrid[nextPos][enemies2Col[4]]
            levelGrid[nextPos][enemies2Col[4]] = temp
            enemies2Row[4] = enemies2Row[4] + verticalAmountFive
        elif levelGrid[cookieRow][cookieCol] == "2":
            enemyNCookie.play()
        elif levelGrid[nextPos][enemies2Col[4]] == "p":
            PLAYER_INDEX = DEATH_INDEX
            deathSound.play()
        elif levelGrid[nextPos][enemies2Col[4]] == "x":
            verticalAmountFive = verticalAmountFive * -1


#Checks if to see if the player has eaten the cookie
def playerNCookieCollision():
    global cookieRow, cookieCol, cookies, PLAYER_INDEX
    if gameState == PLAY_STATE:
        if cookieRow == playerIndexRow and cookieCol == playerIndexCol:
            cookies = cookies + 1
            playerNCookie.play()
        if levelGrid[cookieRow][cookieCol] != "_":
            cookieRow = random.randint(1, len(levelGrid) - 2)
            cookieCol = random.randint(1, len(levelGrid[0]) - 2)
            if cookies == 5:
                unlockGoalSound.play()


#This function is used to draw things onto the screen
def draw():
    drawBackground()
    pygame.display.flip() #should always be the last line in this function


#Draws the background according to the game state
def drawBackground():
    global fontLose
    if gameState == MENU_STATE:
        SCREEN.blit(bg[MENU_INDEX], (0, 0))
        SCREEN.blit(blocks[PLAYER_INDEX], (selectorPos[0], selectorPos[1]))
    elif gameState == PLAY_STATE:
        SCREEN.blit(bg[BG_INDEX], (0, 0))
        drawGrid()
        drawTimer()
        drawLevel()
        drawCookies()
    elif gameState == LOSE_STATE:
        loseText = fontLose.render("PRESS ENTER TO PLAY AGAIN OR PRESS Q TO QUIT", True, (0, 255, 255))
        SCREEN.blit(loseText, (WIDTH/2-450, HEIGHT/2))
    elif gameState == WIN_STATE:
       SCREEN.blit(bg[WIN_INDEX], (0, 0))
    elif gameState == FINISH_STATE:
        SCREEN.blit(bg[FINISH_INDEX], (0, 0))


#Draws the grid on the screen
def drawGrid():
    global totalRows, totalCols, PLAYER_INDEX
    totalRows = len(levelGrid)
    totalCols = len(levelGrid[0])


    for i in range(totalRows):
        for j in range(totalCols):
            block = levelGrid[i][j]
            row = gridPos[0] + BLOCK_SPACING * i
            col = gridPos[1] + BLOCK_SPACING * j
            cookiesRow = gridPos[0] + cookieRow * BLOCK_SPACING
            cookiesCol = gridPos[1] + cookieCol * BLOCK_SPACING


            if block == "x":
                SCREEN.blit(blocks[WALL_INDEX], (col, row))
            elif block == "p":
                SCREEN.blit(blocks[PLAYER_INDEX], (col, row))
            elif block == "e":
                SCREEN.blit(blocks[JAIL_INDEX], (col, row))
            elif block == "1":
                SCREEN.blit(blocks[ENEMY_INDEX], (col, row))
            elif block == "2":
                SCREEN.blit(blocks[ENEMY_INDEX], (col, row))
            elif block == "_":
                SCREEN.blit(blocks[COOKIE_INDEX], (cookiesCol, cookiesRow))
            elif block == "w":
                SCREEN.blit(blocks[WARP_INDEX], (col, row))


#Draws the timer on the screen
def drawTimer():
    timeImg = fontTimer.render(str(format(timer, ".0f")), True, colourTime)
    SCREEN.blit(timeImg, (400, 25))

#Draws the level on the screen
def drawLevel():
    levelImg = fontLevel.render(str(level), True, (255, 255, 255))
    SCREEN.blit(levelImg, (735, 25))

#Draws the cookie on the screen
def drawCookies():
    CookiesImg = fontCookies.render(str(cookies), True, (255, 255, 255))
    SCREEN.blit(CookiesImg, (1087, 25))


#Checks and veirfies if a key is pressed and the game state of the game and the loop runs until the player does not quit
def main():
    global gameState, timer, level, clockTime
    pygame.init()
    init()
    clock = pygame.time.Clock()

    while gameState != QUIT_STATE:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = QUIT_STATE
            elif event.type == pygame.KEYDOWN:
                handlePlayerNCollision()
                playerToFinishBlock()
                handlerMenuSelector()
                if event.key == pygame.K_RETURN and gameState == MENU_STATE and selectorIndex == 1:
                    gameState = QUIT_STATE
                if event.key == pygame.K_RETURN and gameState == MENU_STATE and selectorIndex == 0:
                    gameState = PLAY_STATE
                if event.key == pygame.K_q and gameState == LOSE_STATE:
                    gameState = QUIT_STATE
                if event.key == pygame.K_RETURN and gameState == LOSE_STATE:
                    gameState = PLAY_STATE
                if event.key == pygame.K_q and gameState == WIN_STATE:
                    updateGameLevel()
                    gameState = QUIT_STATE
                if event.key == pygame.K_RETURN and gameState == WIN_STATE:
                    updateGameLevel()
                    gameState = PLAY_STATE
                if event.key == pygame.K_q and gameState == FINISH_STATE:
                    resetGame()
                    gameState = QUIT_STATE
                if event.key == pygame.K_RETURN and gameState == FINISH_STATE:
                    resetGame()
                    gameState = PLAY_STATE


        update()
        draw()
        clockTime = clockTime + 1
    pygame.quit()


#Moves the player and checks if the player collides with a wall or enemy
def handlePlayerNCollision():
    global levelGrid, playerIndexRow, playerIndexCol
    keys = pygame.key.get_pressed()
    if gameState == PLAY_STATE:
        if not timer <= 0:

            if keys[pygame.K_UP]:
                nextPos = playerIndexRow - 1
                if levelGrid[nextPos][playerIndexCol] == "_":
                    temp = levelGrid[playerIndexRow][playerIndexCol]
                    levelGrid[playerIndexRow][playerIndexCol] = levelGrid[nextPos][playerIndexCol]
                    levelGrid[nextPos][playerIndexCol] = temp
                    playerIndexRow = playerIndexRow - 1
                    playerMovementSound.play()
                if levelGrid[nextPos][playerIndexCol] == "1" or levelGrid[nextPos][playerIndexCol] == "2":
                    playerTouchesEnemy()

            elif keys[pygame.K_DOWN]:
                nextPos = playerIndexRow + 1
                if levelGrid[nextPos][playerIndexCol] == "_":
                    temp = levelGrid[playerIndexRow][playerIndexCol]
                    levelGrid[playerIndexRow][playerIndexCol] = levelGrid[nextPos][playerIndexCol]
                    levelGrid[nextPos][playerIndexCol] = temp
                    playerIndexRow = playerIndexRow + 1
                    playerMovementSound.play()
                if levelGrid[nextPos][playerIndexCol] == "1" or levelGrid[nextPos][playerIndexCol] == "2":
                    playerTouchesEnemy()

            elif keys[pygame.K_LEFT]:
                nextPos = playerIndexCol - 1
                if levelGrid[playerIndexRow][nextPos] == "_":
                    temp = levelGrid[playerIndexRow][playerIndexCol]
                    levelGrid[playerIndexRow][playerIndexCol] = levelGrid[playerIndexRow][nextPos]
                    levelGrid[playerIndexRow][nextPos] = temp
                    playerIndexCol = playerIndexCol - 1
                    playerMovementSound.play()
                if levelGrid[playerIndexRow][nextPos] == "2" or levelGrid[playerIndexRow][nextPos] == "1":
                    playerTouchesEnemy()

            elif keys[pygame.K_RIGHT]:
                nextPos = playerIndexCol + 1
                if levelGrid[playerIndexRow][nextPos] == "_":
                    temp = levelGrid[playerIndexRow][playerIndexCol]
                    levelGrid[playerIndexRow][playerIndexCol] = levelGrid[playerIndexRow][nextPos]
                    levelGrid[playerIndexRow][nextPos] = temp
                    playerIndexCol = playerIndexCol + 1
                    playerMovementSound.play()
                if levelGrid[playerIndexRow][nextPos] == "2" or levelGrid[playerIndexRow][nextPos] == "1":
                    playerTouchesEnemy()


#Helper function for handlePlayerNCollision
def playerTouchesEnemy():
    global PLAYER_INDEX
    deathSound.play()
    PLAYER_INDEX = DEATH_INDEX
    drawGrid()


#Allows the player to reach the goal block and finish the level
def playerToFinishBlock():
    global nextPos, playerIndexRow, gameState, CHECKERED_INDEX, PLAYER_INDEX, playerIndexCol
    keys = pygame.key.get_pressed()
    nextPos = playerIndexRow - 1
    if JAIL_INDEX == CHECKERED_INDEX:
        if nextPos == jailIndexRow and playerIndexCol == jailIndexCol:
            if keys[pygame.K_UP]:
                temp = levelGrid[playerIndexRow][playerIndexCol]
                levelGrid[playerIndexRow][playerIndexCol] = levelGrid[nextPos][playerIndexCol]
                levelGrid[nextPos][playerIndexCol] = temp
                playerIndexRow = playerIndexRow - 1
                drawGrid()
            if playerIndexRow == jailIndexRow and playerIndexCol == jailIndexCol:
                winSound.play()
                gameState = WIN_STATE
            if playerIndexRow == jailIndexRow and playerIndexCol == jailIndexCol and level == 3:
                winSound.play()
                gameState = FINISH_STATE


#Handles the menu selector and moves it according to the key pressed
def handlerMenuSelector():
    global selectorPos, selectorIndex, gameOverSelectorPos, gameOverSelectorIndex
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        if 0 <= selectorIndex < 1:
            selectorIndex += 1
            x = selectorPos[0]
            y = selectorPos[1] + 2*(BLOCK_SPACING+6)
            selectorPos = (x, y)

    if keys[pygame.K_UP]:
        if 1 >= selectorIndex > 0:
            selectorIndex -= 1
            x = selectorPos[0]
            y = selectorPos[1] - 2*(BLOCK_SPACING+6)
            selectorPos = (x, y)


#Updates the game level if the player successful finishes a level
def updateGameLevel():
    global timer, level, cookies, PLAYER_INDEX, cookieRow, cookieCol, colourTime, JAIL_INDEX, level, CHECKERED_INDEX

    if gameState == WIN_STATE:
        cookies = 0
        level = level + 1
        initGrid()
        gridPosition()
        enemyMovementHorNCollision_One()
        enemyMovementHorNCollision_Two()
        enemyMovementHorNCollision_Three()
        enemyMovementHorNCollision_Four()
        enemyMovementHorNCollision_Five()
        enemyMovementVerNCollision_One()
        enemyMovementVerNCollision_Two()
        enemyMovementVerNCollision_Three()
        enemyMovementVerNCollision_Four()
        enemyMovementVerNCollision_Five()
        timer = math.ceil(len(levelGrid) * len(levelGrid[0]) * 0.15)
        PLAYER_INDEX = 0
        JAIL_INDEX = 4
        CHECKERED_INDEX = 3
        colourTime = (255, 255, 255)
        cookieRow = random.randint(1, len(levelGrid) - 2)
        cookieCol = random.randint(1, len(levelGrid[0]) - 2)
        if levelGrid[cookieRow][cookieCol] != "_":
            cookieRow = random.randint(1, len(levelGrid) - 2)
            cookieCol = random.randint(1, len(levelGrid[0]) - 2)




if __name__ == "__main__":
    main()