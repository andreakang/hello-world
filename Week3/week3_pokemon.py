
#           uuuuuuuuuuuuuuuuuuuu
#          u" uuuuuuuuuuuuuuuuuu "u
#        u" u$$$$$$$$$$$$$$$$$$$$u "u
#      u" u$$$$$$$$$$$$$$$$$$$$$$$$u "u
#    u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
#  u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
#u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
#$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
#$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
#$ $$$" ... "$...  ...$" ... "$$$  ... "$$$ $
#$ $$$u `"$$$$$$$  $$$  $$$$$  $$  $$$  $$$ $
#$ $$$$$$uu "$$$$  $$$  $$$$$  $$  """ u$$$ $
#$ $$$""$$$  $$$$  $$$u "$$$" u$$  $$$$$$$$ $
#$ $$$$....,$$$$$..$$$$$....,$$$$..$$$$$$$$ $
#$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
#"u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
#  "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
#    "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
#      "u "$$$$$$$$$$$$$$$$$$$$$$$$" u"
#        "u "$$$$$$$$$$$$$$$$$$$$" u"
#          "u """""""""""""""""" u"
#            """"""""""""""""""""

#--------PLEASE FOLLOW THESE INSTRUCTIONS BEFORE YOU START---------------------------------
#--------OTHERWISE YOU WON'T HAVE ANY WORKING MUSIC----------------------------------------

#--------type this first into terminal: sudo easy_install pip
#--------type this second into terminal: sudo pip install pyglet 

#--------GO TO THIS LINK AND DOWNLOAD THE SOUND FOLDER: https://www.dropbox.com/sh/zwjlfa307q1pi16/AACT4SMbLE6N3fxjUDR-9A4-a?dl=0
#--------DRAG THE 'SOUND' FOLDER INTO YOUR DESKTOP. MAKE SURE IT IS CALLED 'sound' LOWERCASE
#--------COPY AND PASTE WHAT'S BELOW AND REPLACE THE SECTION MARKED AS 'REPLACE HERE'------
#--------THEN, DELETE THE '#' SIGN IN FRONT OF EACH LINE TO MAKE THE CODE ACTIVE-----------
#--------REPLACE 'andreakang' WITH YOUR USER NAME, CASE SENSITIVE -------------------------
#--------YOU'RE GOOD TO GO. IF IT DOESN'T WORK...WELL SORRY, NOT SORRY? FIGURE IT OUT------

#-----COPY PASTE BELOW THIS ----------------------------------------------------------------
#titleSound = pyglet.media.load("/Users/andreakang/Desktop/sound/title.wav", streaming=False)
#pikachuSound = pyglet.media.load("/Users/andreakang/Desktop/sound/pikachu.wav", streaming=False)
#balSound = pyglet.media.load("/Users/andreakang/Desktop/sound/bal.wav", streaming=False)
#beingHitSound = pyglet.media.load("/Users/andreakang/Desktop/sound/beinghit.wav", streaming=False)
#thunderboltSound = pyglet.media.load("/Users/andreakang/Desktop/sound/tunderbolt.wav", streaming=False)
#pikaDyingSound = pyglet.media.load("/Users/andreakang/Desktop/sound/pikachuDying.wav", streaming=False)
#squirtleSound = pyglet.media.load("/Users/andreakang/Desktop/sound/squirtle.wav", streaming=False)
#tackleSound = pyglet.media.load("/Users/andreakang/Desktop/sound/tackle.wav", streaming=False)
#battleSound = pyglet.media.load("/Users/andreakang/Desktop/sound/battle.wav", streaming=False)
#catchPokemonSound = pyglet.media.load("/Users/andreakang/Desktop/sound/catch_pokemon.wav", streaming=False)
#-----COPY PASTE ABOVE THIS ----------------------------------------------------------------


import pyglet

# an object describing our player
player = { 
    "name": "p1", 
    "health": 100,
    "pokemon" : ["pikachu"],
    "location" : "start"
    }


thunderbolt = 40

global healthB
healthB = 100
global healthP
healthP = 100
global healthS
healthS = 100
thunder = 40
tack = 25
grow = 0

#-----REPLACE HERE----------------

titleSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/title.wav", streaming=False)
pikachuSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/pikachu.wav", streaming=False)
balSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/bal.wav", streaming=False)
beingHitSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/beinghit.wav", streaming=False)
thunderboltSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/tunderbolt.wav", streaming=False)
pikaDyingSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/pikachuDying.wav", streaming=False)
squirtleSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/squirtle.wav", streaming=False)
tackleSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/tackle.wav", streaming=False)
battleSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/battle.wav", streaming=False)
catchPokemonSound = pyglet.media.load("/Users/andreakang/Desktop/hello-world/Week_3/class/sound/catch_pokemon.wav", streaming=False)


#-----REPLACE HERE-----------------

playerTitleSound = pyglet.media.Player()
playerTitleSound.queue(titleSound)

playerBattleSound = pyglet.media.Player()
playerBattleSound.queue(battleSound)

playerCatchPokemonSound = pyglet.media.Player()
playerCatchPokemonSound.queue(catchPokemonSound)

#------places in Viridian City-----#
#forkInRoad ()
#gameEntrance ()
#bulbasaur ()
#goHome ()

#------pikachu moves------#
#thunderbolt ()
#tackle ()
#growl ()

#------------------------#

def growl ():
    print "---------------------------"
    print '                     ,/      '
    print '          ,/       ,`/___,   '
    print '        ,`/___,  .`__,  ,`   '
    print '      .`__,  ,`     / ,`     '
    print '         / ,`      /,        '
    print '        /,        /`         '
    print '       /`                    '
    print "             "
    print "Pikachu used growl!"
    print "The enemy shakes a little. Nothing happens."
    print "---------------------------"

def thunderbolt ():
    print "---------------------------"
    print '                      ,/     '
    print '                    ,`/      '
    print '                  ,` /       '
    print '                ,`  /_____,  '
    print '              .`____     ,`  '
    print '                   /  ,`     '
    print '                  / ,`       '
    print '                 /,`         '
    print '                /`           '
    print "             "
    print "Pikachu used thunderbolt!"
    print "The enemy lost 40 points!"
    print "---------------------------"


def tackle ():
    print "---------------------------"
    print "Pikachu used tackle!"
    print "The enemy lost 25 points!"
    print "---------------------------"

def goHome ():
    #----------audio is "LAAAAAME!"---------
    print "Alright, guess you're going back home."
    print "See you next time."
    introStory ()


    #end scene

def runAway ():
    playerBattleSound.pause()
    print "You ran away!"
    playerMove = raw_input("press enter >")
    print "What do you want to do now?"        
    playerMove = raw_input("please choose 'go home' or 'keep going' >")
    if (playerMove == "go home"): 
        goHome ()
    else: 
        print "                                "
        print "You're back where you started..."
        print "                                "
        forkInRoad ()

def nowWhatPostBulbasaur ():
    playerBattleSound.pause()
    playerCatchPokemonSound.pause()
    print "                                   "
    print "Now, what do you want to do?"
    playerMove = raw_input("please choose 'go back' or 'explore the blue road'> ")
    if (playerMove == "go back"):
        print "Damn dude, that's lame."
        goHome ()
    else:
        playerMove = raw_input("press enter > ")
        print "Cool, you're at the blue road..."
        roundSquirtleStartAgain ()

def nowWhatPostSquirtle ():
    playerBattleSound.pause()
    playerCatchPokemonSound.pause()
    print "                                   "
    print "Now, what do you want to do?"
    playerMove = raw_input("please choose 'go back' or 'explore the yellow road'> ")
    if (playerMove == "go back"):
        print "Damn dude, that's lame."
        goHome ()
    else:
        playerMove = raw_input("press enter > ")
        print "Cool, you're at the yellow road..."
        roundBulbasaurStartAgain ()

#-----if it's not first time fighting a pokemon-----

def roundBulbasaurStartAgain ():
	global healthB
	healthB = 100
	bulbasaur ()

#-----if it's not first time fighting a pokemon-----

def roundSquirtleStartAgain ():
	global healthS
	healthS = 100
	squirtle ()

#------bulbasaurFight2------------------------------------------------------------------------

def roundBulbasaur2 ():
    global healthB
    global healthP
    print "         "
    print "---------------------------"
    print "Bulbasaur used tackle!"
    print "---------------------------"
    tackleSound.play()
    healthP = healthP - tack
    print "                                "
    print "Bulbasaur Level 3, HP:"
    print healthB
    print "Pikachu Level 5, HP:"
    print healthP
    playerMove = raw_input("press enter > ")
    if (healthP <= 0 ):
        playerBattleSound.pause()
        print "Dude...."
        pikaDyingSound.play ()
        playerMove = raw_input ("press enter > ")
        print "---------------------------"
        print "Pikachu dies forever."
        print "---------------------------"
        print '     `;-.          ___,          '
        print '       `.`\_...._/`.-"`          '
        print '         \        /      ,       '
        print '         / X   X  \    ./ `-._   '
        print '        |)  .    ()\  /   _.""   '
        print '        \  ---     ,; ". <       '
        print '         ;.__     ,;|   > \      '
        print '        / ,    / ,  |.-".-"      '
        print '       (_/    (_/ ,;|.<`         '
        print '         \    ,     ;-`          '
        print '          >   \    /             '
        print '         (_,-``> ./              '
        print '              (_,/               '
        #-------ADD SAD IMAGE ABOUT PIKACHU-----
        playMove = raw_input ("press enter > ")
        print "But!     "
        playerMove = raw_input ("press enter > ")
        print "You found a new Pikachu! It's your lucky day I guess. "
        pikachuSound.play ()
        playerMove = raw_input("press enter > ")
        print "But never forget. You just killed your Pikachu. RIP... "
        pikaDyingSound.play ()
        global health
        healthP = 100
        playerMove = raw_input ("press enter > ")
        nowWhatPostBulbasaur ()
    else:
        print "          "
        roundBulbasaur1 ()


#------bulbasaurFight1------------------------------------------------------------------------



def roundBulbasaur1 ():
    global healthB
    global healthP
    pikachuSound.play()
    print "What do you want to do?"
    playerMove = raw_input("please choose fight, item or run >")
    if (playerMove == "fight"):
        print "Ohhhh shit, let the fight begin!"
        print "                                "
        playerMove = raw_input("please choose 'thunderbolt' (40), 'tackle' (30), 'growl' (0) >")
        if (playerMove == "thunderbolt"): 
            thunderbolt ()
            thunderboltSound.play()
            healthB = healthB - thunder
            playerMove = raw_input("press enter >")
            print "                                "
            print "Bulbasaur Level 3, HP:"
            print healthB
            print "Pikachu Level 5, HP:"
            print healthP


        elif (playerMove == "tackle"):
            tackle ()
            tackleSound.play()
            healthB = healthB - tack
            playerMove = raw_input ("press enter >")
            print "                                "
            print "Bulbasaur Level 3, HP:"
            print healthB
            print "Pikachu Level 5, HP:"
            print healthP
            
        else: 
            growl ()
            healthB = healthB - grow
            PlayerMove = raw_input ("press enter >")
            print "Bulbasaur Level 3, HP:"
            print healthB
            print "Pikachu Level 5, HP:"
            print healthP


    elif (playerMove == "item"):
        print "                                "
        playerMove = raw_input ("please choose 'pokeball' or 'back' > ")
        if (playerMove == "pokeball"):
            print "                                "
            print "---------------------------"
            print "You used poke ball!"
            print "---------------------------"
            print '                                                     /       '
            print '                                                    /        '
            print '                                                   /         '
            print ' -------/----------------------\------     /      /    /     '
            print ' -----/                         \-----    /      /    /      '
            print ' ----/                           \----   /      /    /       '
            print ' ---/                             \---  /      /    /        '
            print ' --/                               \-- /      /    /         '
            print ' -/                                 \ /      /    /          '
            print ' |                                   |      /    /           '
            print ' |               NNNNN               |     /    /            '
            print ' |              NN   NN |            |    /    /             '
            print ' |_____________ NN   NN_|____________|   /    /              '
            print ' |NNNNNNNNNNNN  NN   NN  NNNNNNNNNNNN   /    /               '
            print '  NNNNNNNNNNNN   NNNNN  NNNNNNNNNNNNN  /                     '
            print '  NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN /                      '
            print '   NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN /                       '
            print '    NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN                          '
            print '     NNNNNNNNNNNNNNNNNNNNNNNNNNNNN                           '
            print '      NNNNNNNNNNNNNNNNNNNNNNNNNNN                            '
            print '       NNNNNNNNNNNNNNNNNNNNNNNNN                             '
            print '          NNNNNNNNNNNNNNNNNNN                                '
            print "                                "
            playerMove = raw_input ("press enter >")
            if (healthB >= 25):
                print "                                "
                print "---------------------------"
                print "Shit, it didn't work!" 
                print "---------------------------"
                playerMove = raw_input ("press enter >")
                roundBulbasaur2 ()
            else: 
                playerBattleSound.pause()
                playerCatchPokemonSound.play()
                print "                                "
                print "Dude, you caught Bulbasaur!"
                print "CONGRATS!"   
                print '      _______  _______  __    _  _______  ______    _______  _______  _______     ____   '
                print '     |       ||       ||  |  | ||       ||    _ |  |   _   ||       ||       |   |   |   '
                print '     |      _||   _   ||   |_| ||    ___||   | ||  |  | |  ||_     _||  _____|   |   |   '
                print '     |     |  |  | |  |        ||   | __ |   |_||_ |  |_|  |  |   |  | |_____        |   '
                print '     |     |  |  |_|  ||  _    ||   ||  ||    __  ||       |  |   |  |_____  |   |   |   '
                print '     |     |_ |       || | |   ||   |_| ||   |  | ||   _   |  |   |   _____| |   |   |   '
                print '     |_______||_______||_|  |__||_______||___|  |_||__| |__|  |___|  |_______|   |___|   '
                print '                                                                                  ___    '
                print '                                                                                 |   |   '
                print '                                                                                  ---    '  
                nowWhatPostBulbasaur () 
        else:
            roundBulbasaur1 ()          
    else:
        runAway ()
    
    playerMove = raw_input("press enter > ")
    if (healthB >= 0): 
        roundBulbasaur2 ()
    else: 
        playerBattleSound.pause()
        print "----------------------------"
        print "Oh no! You just murdered Bulbasaur."
        print "----------------------------"
        playerMove = raw_input("press enter > ")
        nowWhatPostBulbasaur ()

#-----------------squirtleFight----------

def squirtle ():
    print "                                "
    print "As you're walking down the path, you hear a splash in the water."
    print "It's a wild squirtle!!!!!!!!!!!!!"
    print "                                "
    playerMove = raw_input("press enter > ")
    playerBattleSound.play ()
    print '                     .._______                                                    '
    print '             ,-""            "`-.                                                 '
    print '           ,""                   `-.                                              '
    print '         ,""                        \                                             ' 
    print '       /                           .                                              '
    print '       ."\               ,"".       `                                             '
    print '      ._./|             / |  `       \                                            '
    print '     |   |            `-./  ||       `.                                           '
    print '     |   |            `-._,`||       | \                                          '
    print '     .`.,`             `..,`.`       , |`-.                                       '
    print '     l                       .``.  _/  |   `.                                     '
    print '     `-.._`-   ,          _ _`   -" \  .     `                                    '
    print '`."""""`-.`-...,---------`,`         `. `....__.                                  '
    print '.`        `"-..___      __,`\          \  \     \                                 '
    print '\_ .          |   `""""`    `.           . \     \                                '
    print '  `.          |              `.          |  .     L                               '
    print '    `.        |`--...________.`.        j   |     |                               '
    print '      `._    .`      |          `.     .|   ,     |                               '
    print '         `--,\       .            `7""` |  ,      |                               '
    print '            ` `      `            /     |  |      |    _,-`"""`-.                 '
    print '             \ `.     .          /      |  `      |  ,`          `.               '
    print '              \  v.__  .        `       .   \    /| /              \              '
    print '               \/    `""-"""""`.       \   \  /.``                |             '
    print '                `        .        `._ ___,j.  `/ .-       ,---.     |             '
    print '                ,`-.      \         ."     `.  |/        j     `    |             '
    print '               /    `.     \       /         \ /         |     /    j             '
    print '              |       `-.   7-.._ .          |"          `         /              '
    print '              |          `./_    `|          |            .     _,`               '
    print '              `.           / `----|          |-............`---`                  '
    print '                \          \      |          |                                    '
    print '               ,`           )     `.         |                                    '
    print '                7____,,..--`      /          |                                    '
    print '                                  `---.__,--.`=                                   '
    print '          '
    print "Squirtle has to FIGHT!"
    squirtleSound.play()
    playerMove = raw_input("press enter > ")
    print "Squirtle Level 7, HP:"
    print healthS
    print "Pikachu Level 5, HP:"
    print healthP
    print '                         '
    roundSquirtle1 ()

#------squirtleFight2------------------------------------------------------------------------

def roundSquirtle2 ():
    global healthS
    global healthP
    print "         "
    print "----------------------"
    print "Squirtle used tackle!"
    print "----------------------"
    tackleSound.play()
    healthP = healthP - tack
    print "                                "
    print "Squirtle Level 7, HP:"
    print healthS
    print "Pikachu Level 5, HP:"
    print healthP
    playerMove = raw_input("press enter > ")
    if (healthP <= 0 ):
        playerBattleSound.pause ()
        print "---------------------------"
        print "Dude...."
        print "---------------------------"
        pikaDyingSound.play()
        playerMove = raw_input ("press enter > ")
        print "---------------------------"
        print "Pikachu dies forever."
        print "---------------------------"
        print '     `;-.          ___,          '
        print '       `.`\_...._/`.-"`          '
        print '         \        /      ,       '
        print '         / X   X  \    ./ `-._   '
        print '        |)  .    ()\  /   _.""   '
        print '        \  ---     ,; ". <       '
        print '         ;.__     ,;|   > \      '
        print '        / ,    / ,  |.-".-"      '
        print '       (_/    (_/ ,;|.<`         '
        print '         \    ,     ;-`          '
        print '          >   \    /             '
        print '         (_,-``> ./              '
        print '              (_,/               '
        #-------ADD SAD IMAGE ABOUT PIKACHU-----
        playMove = raw_input ("press enter > ")
        print "---------------------------"
        print "But!     "
        print "---------------------------"
        playerMove = raw_input ("press enter > ")
        print "---------------------------"
        print "You found a new Pikachu! It's your lucky day I guess. "
        print "---------------------------"
        pikachuSound.play()
        playerMove = raw_input("press enter > ")
        pikaDyingSound.play()
        print "---------------------------"
        print "But never forget. You just killed your Pikachu. RIP... "
        print "---------------------------"
        global health
        healthP = 100
        playerMove = raw_input ("press enter > ")
        nowWhatPostSquirtle ()
    else:
        print "          "
        roundSquirtle1 ()

#----------squirtleFight1--------------

def roundSquirtle1 ():
    global healthS
    global healthP
    pikachuSound.play()
    print "What do you want to do?"
    playerMove = raw_input("please choose fight, item or run >")
    if (playerMove == "fight"):
        print "Ohhhh shit, let the fight begin!"
        print "                                "
        playerMove = raw_input("please choose 'thunderbolt' (40), 'tackle' (30), 'growl' (0) >")
        if (playerMove == "thunderbolt"): 
            thunderbolt ()
            thunderboltSound.play()
            healthS = healthS - thunder
            playerMove = raw_input("press enter >")
            print "                                "
            print "Squirtle Level 7, HP:"
            print healthS
            print "Pikachu Level 5, HP:"
            print healthP
            roundSquirtle2 ()

        elif (playerMove == "tackle"):
            tackle ()
            tackleSound.play()
            healthS = healthS - tack
            playerMove = raw_input ("press enter >")
            print "                                "
            print "Squirtle Level 7, HP:"
            print healthS
            print "Pikachu Level 5, HP:"
            print healthP
            roundSquirtle2 ()

        else: 
            growl ()
            healthS = healthS - grow
            PlayerMove = raw_input ("press enter >")
            print "Squirtle Level 7, HP:"
            print healthS
            print "Pikachu Level 5, HP:"
            print healthP
            roundSquirtle2 ()

    elif (playerMove == "item"):
        print "                                "
        playerMove = raw_input ("please choose 'pokeball' or 'back' > ")
        if (playerMove == "pokeball"):
            print "                                "
            print "---------------------------"
            print "You used poke ball!"
            print "---------------------------"
            print '                                                     /       '
            print '                                                    /        '
            print '                                                   /         '
            print ' -------/----------------------\------     /      /    /     '
            print ' -----/                         \-----    /      /    /      '
            print ' ----/                           \----   /      /    /       '
            print ' ---/                             \---  /      /    /        '
            print ' --/                               \-- /      /    /         '
            print ' -/                                 \ /      /    /          '
            print ' |                                   |      /    /           '
            print ' |               NNNNN               |     /    /            '
            print ' |              NN   NN |            |    /    /             '
            print ' |_____________ NN   NN_|____________|   /    /              '
            print ' |NNNNNNNNNNNN  NN   NN  NNNNNNNNNNNN   /    /               '
            print '  NNNNNNNNNNNN   NNNNN  NNNNNNNNNNNNN  /                     '
            print '  NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN /                      '
            print '   NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN /                       '
            print '    NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN                          '
            print '     NNNNNNNNNNNNNNNNNNNNNNNNNNNNN                           '
            print '      NNNNNNNNNNNNNNNNNNNNNNNNNNN                            '
            print '       NNNNNNNNNNNNNNNNNNNNNNNNN                             '
            print '          NNNNNNNNNNNNNNNNNNN                                '
            print "                                "
            playerMove = raw_input ("press enter >")
            if (healthS >= 25):
                print "                                "
                print "Shit, it didn't work!" 
                playerMove = raw_input ("press enter >")
                roundSquirtle2 ()
            else: 
                playerBattleSound.pause ()
                playerCatchPokemonSound.play()
                print "                                "
                print "Dude, you caught Squirtle!"
                print "CONGRATS!"
                print '      _______  _______  __    _  _______  ______    _______  _______  _______     ____   '
                print '     |       ||       ||  |  | ||       ||    _ |  |   _   ||       ||       |   |   |   '
                print '     |      _||   _   ||   |_| ||    ___||   | ||  |  | |  ||_     _||  _____|   |   |   '
                print '     |     |  |  | |  |        ||   | __ |   |_||_ |  |_|  |  |   |  | |_____        |   '
                print '     |     |  |  |_|  ||  _    ||   ||  ||    __  ||       |  |   |  |_____  |   |   |   '
                print '     |     |_ |       || | |   ||   |_| ||   |  | ||   _   |  |   |   _____| |   |   |   '
                print '     |_______||_______||_|  |__||_______||___|  |_||__| |__|  |___|  |_______|   |___|   '
                print '                                                                                  ___    '
                print '                                                                                 |   |   '
                print '                                                                                  ---    '     
                nowWhatPostSquirtle () 
        else:
            roundSquirtle1 ()          
    else:
        runAway ()

#------bulbasaurFight------------------------------------------------------------------------

def bulbasaur ():
    print '                                                              '
    print '                              _,.------....___,.--,.          '
    print '                         ,---/         _,.__,,      |         '
    print '                       _/         _.""              .         ' 
    print '                      /   ,     ,/                   `        '
    print '                      .   /     /                     ``.     '
    print '                     |  |     .                       \.\     '
    print '          ____        |___._.  |       __               \ `.  '
    print '        .`    `---```       ```-.--```  \               .  \  '
    print '        .  ,            __               `              |   . '
    print '      `,"         ,- --.               \             |    L   '
    print '     ,`          :    _.:                -._          /    |  '
    print '     ,`-.    ,". `----`                      >.      ,     |  '
    print '     . ."\   `-"      __    ,  ,-.         /  `.__.-       ,  '
    print '     ||:, .           ,  ;  /  / \ `        `.    .      ./   '
    print '     j|:D  \          `--`  `,`_  . .         `.__, \   , /   '
    print '     / L:___|                .  "" :_;                `."."   '
    print '     .                        `----"                    V     '
    print '     `.                                 .    `.   _,..  `     '
    print '       `,_   .    .                _,-`/    .. `,`   __  `    '
    print '        ) \`._        ___....----""  ,"   ."  \ |   "  \  .   '
    print '       /   `. ``-.--""         _,` ,`     `---" |    `./  |   '
    print '       .   _  ```--.._____..--"   ,             |         |   ' 
    print '      | ." `. `-.                /-.           /          ,   '
    print '      | `._."    `,_            ;  /         ,`          .    '
    print '      .          /| `-.        .,"         ,           ,      '
    print '      `-.__ __ _,`,`    ``-..___;-...__   ,."\ ____.___."     '
    print '      ``^--`..`   `-`-^-""--    `-^-``."""""`.,^.`.--"        '
    print 'Bulbasaur wants to FIGHT!'
    print "                                "
    balSound.play()
    playerBattleSound.play()
    
    
    #-----player starts fight with bulbasaur with 100% health-----
    playerMove = raw_input("press enter >")
    print "Bulbasaur Level 3, HP:"
    print healthB
    print "Pikachu Level 5, HP:"
    print healthP
    print '                         '
    roundBulbasaur1 ()

#-----forkInRoad------------------------------------------------------------------------
def forkInRoad ():
    # this is the beginning of the game
    print "You see a yellow road that leads to the forest, and a blue road that leads to a river. Which road do you want to take?"
    playerMove = raw_input("please choose yellow or blue > ")
    if (playerMove == "yellow"):
        print "As you're walking down the path, you hear a rustle in the leaves."
        print "                "
        print "It's a wild bulbasaur!!!!!!!!!!!!"
        print "                                "
        playerMove = raw_input("press enter > ")
        playerTitleSound.pause()
        bulbasaur ()

    else: 
        playerTitleSound.pause()
        squirtle ()
            # i'm going to write this code later! PAY ATTENTION HERE

#------intro------------------------------------------------------------------------
def introStory():
    # this is the introduction to the story
    titleSound.play()
    print "Welcome! What should I call you?"
    player["name"] = raw_input("Please enter your name > ")
    
    # intro story, quick and dirty (think star wars style)
    print "Welcome to Viridian City " + player["name"] + "!"
    print "         "
    print '                                                                                 '
    print '                                        +                                        '         
    print '                                       / \                                       '
    print '      _____        _____     __________/ o \/\_________      __________          '
    print '     |o o o|_______|    |___|               | | # # #  |____|o o o o  | /\       '
    print '     |o o o|  * * *|: ::|. .|               |o| # # #  |. . |o o o o  |//|)\     '
    print '     |o o o|* * *  |::  |. .| []  []  []  []|o| # # #  |. . |o o o o  |((|))     '
    print '     |o o o|**  ** |:  :|. .| []  []  []    |o| # # #  |. . |o o o o  |((|))     '
    print '     |_[]__|__[]___|_||_|__<|____________;;_|_|___/\___|_.|_|____[]___|  |       '
    print "             "
    print "             "
    print "It's a beautiful, sunny day. You're off for an adventure this afternoon."
    print "After grabbing your lunch, you call out to your pal..."
    print "Pikachu!"
    playerMove = raw_input("press enter > ")
    print "Pikachu arrives..! You're ready to head out."
    pikachuSound.play ()
    print "             "
    print '     `;-.          ___,          '
    print '       `.`\_...._/`.-"`          '
    print '         \        /      ,       '
    print '         /()   () \    ./ `-._   '
    print '        |)  .    ()\  /   _.""   '
    print '        \  -"-     ,; ". <       '
    print '         ;.__     ,;|   > \      '
    print '        / ,    / ,  |.-".-"      '
    print '       (_/    (_/ ,;|.<`         '
    print '         \    ,     ;-`          '
    print '          >   \    /             '
    print '         (_,-``> ./              '
    print '              (_,/               '
    playerMove = raw_input("press enter > ")

    print "After walking for a while, you see a mountain in the near distance."
    print "Do you head there?"
    playerMove = raw_input("please choose yes or no > ")

    # the player can choose yes or no
    if (playerMove == "yes"):
        print "You walk closer to the mountain, and you are in front of a fork in the road..."
        raw_input("press enter>")
        forkInRoad ()
    else: 
        print "No? Do you want to go home?"
        playerMove = raw_input("please choose yes or no >")
        if (playerMove == "yes"):
            goHome ()
        else: 
            print "Alright, let's keep going!"
            print '            _            '
            print '           /(|           '
            print '          (  :           '
            print '         __\  \          '  
            print '       (____)  `|-----   '
            print '      (____)|   |        '
            print '       (____).__|        '
            print '        (___)__.|_____   '

            playerMove = raw_input("press enter >")
            forkInRoad ()

#------story starts----------------------------------------------------------------------
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmoNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo``-dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh-`.:sdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy/sdNMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMNNmdhyyyhdmNMMMMMMMMMMMMMMMMNNmhs+/MMMMm+yNMMMMMMMMMMMMMMMMMMMMMMMMdhhhhdMMo---sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMNdy+:.`        `./sNMMMMMMMMMMMMM:-    `NMMy` `-yNMMMMMNhs+///+sdNMMMMMN`    .MM`   -MMMMMMMMMMMMMsyhdNNNMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMNs/.                  .sMMMMMMMMMMMMdN`   `dN/     `-mMMh:`  ```   `-yMMMMs     `hh    `mMMMMMMMMMMMN+.  `.-oMMMMNNNMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMN:              ``     `sMMMMMMMMMMMMM-   `o.      :dMM/  `odmmNy   +mMMMM:     `+/    `sMMMMMMMMMMMMM/     .NMMM:`.-/+NMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMM+           +NNNmy`   :MMMMMMMMMMMMM+          -hMMMo   yMMNNy. :dMMMMMN       ``     :MMMMNdhyyhNMM:     `sMMd     +MMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMs:oo       .NNdsMy   sMMMMmyoooshNMy        .yMMMMM:   sMMd- -dMdsNMMMs              :MMy::o:`  `:hMo     -MM/    .NMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMM+       +MMdM+  /MMN+..o+`  ``oNh`     .sdMMMMMs   `+/  /s+. `.omMd/            +Md. oMd   `: `hM:    `dm     hMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMM/      `dMd/  oMMs` -NM-   +``/My       ``-+yNMo             `/dMd-   s/   `` -Mm` `sMMmssms  /Ms    `//    /MMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMM:      --  /mMMy   -MMNhydm` `NM   +:`     `.yMmo-`     .:+yNMMy    `mM:  y/ sM+   `+hmmh+   sM+ /   `    .NMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMN-      `sNMMMM-   `-shdho`  -Mm  `mMNdo:`   `-odNNNmmmNMMMMMMM:    -MMN-+Mh`+My     ```    /Mh `h        yMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMm.     `mMMMMM:      ``    .dM:  `mMMMMMNdo:`  ``.:NMMMMMMMMMMs+/:-sMMMNMMN``hMo`        -yMs` .M`      /MMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMd`    `+MMMMMm-         `/mMy   `mMMMMMMMMMNho:` `NMMMMMMMMMMMMMMNMMMMMMMM: `omms/:::/sdNN-   +M`     `mMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMh`    `mMMMMMNy/-```-/smMMMh  `-mMMMMMMMMMMMMMNhoNMMMMMMMMMMMMMMMMMMMMMMMh::--/mMMMMMMMMy   `dM.     yMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMy    `+MMMMMMMMNNNNNMMMMMMMmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMMMMMNdyssMM-    :MMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo    `mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-   `mMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+.-/smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMds+:sMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
print 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'

introStory()

