######################### IMPORTING MODULES/PACKAGES ###############################
import random
import time, sys, string

from playsound import playsound

###################### BOOLS ############################
key = False
radio = False


###################### DEFINITIONS OF REUSABLE FUNCTIONS ############################

# You can copy choice function from the unfinished example file... unless you took
# ICS2O last year...

# chooseOption function to force user to select 1 of ? options
def chooseOption(numberOfOptions):
    choice = 0
    while choice < 1 or choice > numberOfOptions:
        print("1 to " + str(numberOfOptions) + "> ", end="")
        choice = input()
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            choice = 0
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
            choice = int(choice)
    print("\n\n")
    return choice


def narratorDialogue(speech):
    line = "\u001b[36m" + speech + "\u001b[0m"
    return line


def consoleMessages(condition, text):
    if condition == "end":
        print("\u001b[31m" + text + "\u001b[0m")
    elif condition == "win":
        print("\u001b[32m" + text + "\u001b[0m")
    elif condition == "secret":
        print("\u001b[34m" + text + "\u001b[0m")
    elif condition == "radio":
        print("\u001b[30;47m" + text + "\u001b[0m")


def monsterDescription():
    print("A ͟sque͟a̡l͝ i͜n ͟th͞e ̀f̧òg, ̴a͠ ̡ja͞n̨g̵l͞ing ͢of ̡cha̵ins,̵ ̛a͞n͝d̢ suddenly y͟óu'̛re gree͡ted by͜ a͏ s̡i̷c̷kén͠ing͠ ̢ent͘ity̢ ̶of ̴sm͝o͢ke ҉a͢ńd͜ d̴ec̛ay.͏ ͘F͢o̢u̸r͠ ̀vio̵lęnt ̷ey҉e̴s͘ sta͏re͘ at yòu̶ w̶ith ̕a ͘s͢ic̢k͢e͠n̡ing ̵c̷oǹt͡o̵rt҉įon̴, a̧n͠d͝ an͘ot̵he͠r s̕q͞u̢e̵a̧l r͟eson͞a̴tes̷ ͠fro̸m ̡its̕ ̧co̵nt̨r̨a͝cte̵d ̸mòu̴th w͜it͠h ̕d̛ea͝fen҉ing̨ ̨i̸n͏te͢n̴sity͘.̀͟͠"
          "S͟mo̢ĺderi͢ng ͘ànd ͠s͢m͜oķi̡ng s̶k̢in ad̷o͠ŗn͞s i̶ts s̨kele͡t͞a̢l̛ head, w͏h̷i̸c͠h͟ i̡tself͡ i̢ś ̵c̀ove̷r͏ed i̵n sm̀all͞ ga̷sh̢es. Ţhe͡ ̧sound of̧ ҉a ŕoa͞ŕing̶ ͜fire es̴c͠apes͝ ͢t͞h́ȩ ̶c̵ŕea̕tur̷e'͢s̵ c͠o͏n̢vex́ nostri̵l͏s ̀se҉t w͘i͜th̢iņ a ͝gau̢n̵t͏ ̡noşe̷.͏̶͢͠"
          "̡I̶t̀s̴ s͜k̕e͞l̸e҉t͟al͏ h̨ea̢d̶ si̸t̸s ̀at́op a͡ ̸h́ard,҉ heav͞y͝ ͝b̶ǫd̡y̷.͠ ̷B̷izaŕr̷e͢ b͏ulge͢s̀ c̷r͟awl ̸b͜eņȩa̷t͞h its śk͡i̕n,̢ ͡w͜ho ̧kǹows ̡what̢ th̴e͢ ̷st͡ory ͘be҉hin͟d̛ ͏t̴hi̸s̕ ̨i̶s͝.͢͟͟͠͡͡"
          "͢T̕he͝ cr̶eat͠ure͝ bol̶ts t͏ow̶ard ̵y̕ou,̸ ̶i̶ts ̢fou͢r ͜le͝g͠s ͝effort̸lessl̕y̸ ̴ca͜rr҉y i̕t͟s dem̷oǹi͞c ̴b͏o̧d͡y ͡w͢ith̨ a̷ ͡d̵is̸t͠ur̴b̶i̢n҉g͢ ̸e̛n̕e̕r̵gy. ͜A̢ ja͏g͘g͟e͟ḑ t͏a͟i̵l s̛li̶de͢s ͟bȩh͘índ̕ ͝i͢t, ̡yo̴u҉'̀ŗe ̸c͞er͜t́ai̵n͜ t̶his cr͞e͜a̧t͠u̵r̴e͟ u̴s͟es ̴įt ̢a̸ş a̕ ͝we̡a̴pon.̕͞͝"
          "̨S̴mol̛d̨ering a̸n҉d͏ s҉m̡o͘kín͢ģ ̕sk͞i͘n ad̢orn͝s i҉t̸s͡ s͠k̸e͞le̷t͡a̸l ͜head̀,̢ whic̨h itself is̶ ̴c͏ove̢r̡ed in̸ ̷sm̛all ͘gas҉h̸e̢s.̶͜")


def pause():
    input("Press enter to continue")


def hackChallenge(numberOfCharacters=0, duration=0):
    challenge = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(numberOfCharacters))
    consoleMessages("radio",
                    "The code is ready, you will have to enter %d characters, you only have %d seconds, you only have one shot!" % (
                    numberOfCharacters, duration))
    pause()
    consoleMessages("radio", "The code is %s, go quickly!!!!" % challenge)
    startTime = time.time()
    answer = input("> ")
    endTime = time.time()
    elapsedTime = endTime - startTime
    timeLeft = duration - elapsedTime
    if answer == challenge and elapsedTime < duration:
        consoleMessages("radio", "You did it thank god! With only %d seconds to spare!" % timeLeft)
        win = True
        return win
    else:
        consoleMessages("radio", "You failed, that was it, it's all over now...")
        win = False
        return win


###################### DEFINITIONS OF YOUR FUNCTIONS ############################
# Skip tutorial function
def titleScreen():
    print(titleArt)
    print("\n\n\n")
    print("1 Play")
    print("2 Settings")
    print("3 Quit")
    time.sleep(1)
    choice = chooseOption(3)

    if choice == 1:
        skipTutorial()
    elif choice == 2:
        settings()
    elif choice == 3:
        print("Quitting...")
        time.sleep(1)
        sys.exit(0)
    else:
        print("Error")


def settings():
    print("Would you like music?")
    print("1 Yes")
    print("2 No")
    time.sleep(1)
    choice = chooseOption(2)
    global music
    if choice == 1:
        playsound("Media/Abuse-In-The-Orphanage.mp3")
    elif choice == 2:
        music = False
    else:
        print("Error")
    pause()
    titleScreen()


def skipTutorial():
    skipTutorial = "null"
    print("Would you like to skip the tutorial?(NOT RECOMMENDED FOR NEW PLAYERS)")
    while skipTutorial != "Y" or skipTutorial != "y" or skipTutorial != "N" or skipTutorial != "n":
        skipTutorial = input("Y/N> ")
        if skipTutorial == "Y" or skipTutorial == "y":
            start()
            break
        elif skipTutorial == "N" or skipTutorial == "n":
            tutorial()
            break


# TUTORIAL function
# function to introduce the game and then start it
def tutorial():
    print("\n")
    # introduce story and provide simple instructions
    print(
        "Welcome to LABRATXD42069, this is a Choose Your Own Adventure Game where the choices you make determine your fate. You will die, you will be reborn, don't make the same mistake twice! Your sole objective is survival, you play be selecting the choice you wish to make by entering the corresponding number.")
    print(
        "\nThere several secret elements thoughout the game, be sure to explore areas to unlock the special events and areas. They may be advantageous.")
    print(
        "\nBe sure to read answers carefully and think of things from multiple perspectives, this will not be an easy journey. Begin.\n")
    input("Press Enter to Begin\n\n")

    # call start() function to being the game
    start()


# START function
# start the game by setting up the location/scene/action
def start():
    # continue story line and proceed to first location/scene/action
    print(
        "You wake up in a cold sweat in a dark, small and lonely room, you've lost count how many times you've been here. A familiar monotone voice starts speaking over the intercom, as it does every day no matter what you do. \"Subject your trials begin anew, please exit your room and begin the test\"")
    print("\n")
    print(
        "The door opens automatically making you remember the first time you woke up here, when the door slammed you in the face so hard it killed you. As you step outside you notice the first new thing you've seen for what feels like years. Along the padded white walls of the room there is now doors with padlocks on them. \"Subject your trials are different today, you will test our new simulated reality doors. To progress from one door to the next, the previous reality must have been completed succesfully.\" Suddenly the padlock of the door in front of you shatters, and the door slams open to reveal an arcade")

    # Then jump to the first scene/location/action
    # In while loop


def narratorRespawn():
    choice = random.randint(1, 4)
    line1 = narratorDialogue("Wakey wakey, corpse!")
    line2 = narratorDialogue("Welcome back, dead already?")
    line3 = narratorDialogue("You know the drill, pick a door, get moving.")
    line4 = narratorDialogue("Do I even have to say it, through the door. Now.")
    line5 = narratorDialogue("Don't just stand there, all you did was die, I don't have all day, get moving.")
    choiceList = [line1, line2, line3, line4, line5]
    print(choiceList[choice])


########################## LOCATION/SCENE/ACTION Functions #######################

# RENAME location1() function to reflect your actual first location/scene/action
def spawnRoom():
    playsound("Media/Spawn.mp3")
    global respawn
    if respawn < 1:
        print(narratorDialogue("There are some doors you can go through, pick one."))
        respawn += 1
    elif respawn > 0:
        narratorRespawn()
    # list players options
    print("")
    print("Which door do you go through?")
    print("1 The Plastered one")
    if key == True:
        print("2 The Metallic one")
    if radio == True and key == True:
        print("3 Follow the radio chatter through the golden door")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(3)
    if 1 == choice and key == False:
        print(openDoorArt)
        time.sleep(1)
        arcadeDoor()
    elif 1 == choice and key == True:
        print(closedDoorArt)
        print("You've already been here? Why would you go back?")
        print("INTERRUPTED SIMULATION, REBOOTING")
        time.sleep(2)
        spawnRoom()
    elif 2 == choice and key == True and radio == False:
        print(openDoorArt)
        time.sleep(1)
        cliffDoor()
    elif 2 == choice and key == True and radio == True:
        print(closedDoorArt)
        print("You've already been here? Why would you go back?")
        print("INTERRUPTED SIMULATION, REBOOTING")
        time.sleep(2)
        spawnRoom()
    elif 3 == choice and radio == True:
        print(openDoorArt)
        time.sleep(1)
        radioChatter()
    else:
        print("DISRUPTED SIMULATION, REBOOTING")
        spawnRoom()


def arcadeDoor():
    print(
        "The plastered door with a crude drawing of a yellow creature with a weird mouth presents itself to you, you walk through")
    playsound("Media/Door.mp3")
    arcade()


def cliffDoor():
    print(
        "You walk towards a door that says FORD matching the Key's inscription. As you walk through, a mustang appears before you, you get in the car and start the engine.")
    playsound("Media/Door.mp3")
    cliffStart()


########################## ARCADE PATH #######################
# rename function to reflect your actual location/scene/action
def arcade():
    print("You walk into an arcade with a restaraunt, a bowling alley and a arcade game section where do you go first?")
    time.sleep(1.5)
    print("1 Restaraunt")
    print("2 Bowling Alley")
    print("3 Arcade")
    choice = chooseOption(3)

    if 1 == choice:
        restaraunt()
    elif 2 == choice:
        bowlingAlley()
    elif 3 == choice:
        arcadeGames()
    else:
        print("Error")


def restaraunt():
    print("You walk into the restaraunt and are seated, a waitress arrives and asks what you'd like to eat.")
    time.sleep(1.5)
    print("1 Burger")
    print("2 Pasta")
    print("3 Pizza")
    print("4 Just Water")
    choice = chooseOption(4)

    if 1 == choice:
        leaveRestaraunt()
    elif 2 == choice:
        leaveRestaraunt()
    elif 3 == choice:
        leaveRestaraunt()
    elif 4 == choice:
        waterDeath()
    else:
        print("Error")


def waterDeath():
    print(
        "The waitress brings you a cold and refreshing glass of water, you drink it in it's entirety. Within one minute you collapse on the floor and asphyxiate, you were poisoned by the chef for not spending money, not that anyone knows that.")
    time.sleep(1.5)
    # CHANGE BOOLS


def leaveRestaraunt():
    print("You enjoy a delicious meal, pay and walk outside the restaraunt. Where do you go?")
    time.sleep(1.5)
    print("1 Bowling Alley")
    print("2 Arcade")
    choice = chooseOption(2)

    if 1 == choice:
        bowlingAlley()
    elif 2 == choice:
        arcadeGames()
    else:
        print("Error")


def bowlingAlley():
    print("You buy a lane and start bowling, but the ball return machine breaks. What do you do?")
    time.sleep(1.5)
    print("1 Reach into the machine to try and grab a ball")
    print("2 Become the bowling ball")
    print("3 Stop playing")
    choice = chooseOption(3)

    if 1 == choice:
        handCrush()
    elif 2 == choice:
        skullCrush()
    elif 3 == choice:
        leaveAlley()
    else:
        print("Error")


def handCrush():
    consoleMessages("end",
                    "As you reach into the machine a ball comes out, before you can react your hand is brutally crushed between the metal machine and the bowling ball. Before you can remove your hand someone grabs you from behind and drags you to the bathroom. Your captor throws you to the ground, you look up to see... nothing, just a hole in reality that is impossible to discern, the very nature of the world broken by this fiend. You see it come closer, almost reaching out with a eerie touch, you feel impossibly cold and close your eyes before it can reach you. This is however no escape from the horror before you, in your mind now you can truely see it.")
    monsterDescription()
    pause()


def skullCrush():
    consoleMessages("end",
                    "Without a bowling ball you decide to do the only logical thing and dive down the lane. As you land you can hear the splintering of your ribs, but it's too late to stop now as you continue to build momentum. With a crash you fly straight into the head pin, crushing your skull. The last thing you hear as your vision goes black is the TV above you say \"STRIKE!\"")
    pause()


def leaveAlley():
    print("You decide to leave the alley and notice the restaurant has closed, you go to the Arcade")
    time.sleep(1.5)
    arcadeGames()


def arcadeGames():
    print(
        "You arrive in the arcade proper, it's absolutely packed with people and no games are open, the blinking neon and quarter sucking machines remind you of your childhood. What do you do?")
    time.sleep(1)
    print("1 Stand and watch")
    print("2 Go look at the prizes")
    choice = chooseOption(2)

    if choice == 1:
        watch()
    elif choice == 2:
        prizes()
    else:
        print("Error")


def watch():
    print("You decide to save your money and watch some other people play")
    time.sleep(1)
    print(
        "Across the room you notice something odd, a kid playing PacMan disappeared in the second you spent looking at the other side of the room. You look back at the other side to see the Frogger machine which had someplaying it and a 3 person line is now open. A feeling of dread starts building in your gut, a shiver runs down your spine and your head starts to ache. You close your eyes and hold your head to rebalance yourself, when you look up at the arcade again only one other person is left. A black clad man hiding in the shadows, yet you blink and he has disappeared too. What do you do?")
    time.sleep(10)
    print("1 Run as fast as you can")
    print("2 Wait for the inevitable")
    choice = chooseOption(2)

    if choice == 1:
        runDeath()
    elif choice == 2:
        waitDeath()
    else:
        print("Error")


def runDeath():
    consoleMessages("end",
                    "In a feeble attempt to escape you run for the exit, before you even make it 10 steps an ice cold and wet claw grips your throat. You try to scream but there's no air in your lungs, the claw is squeezing too hard. You begin to be tilted back into the gaping maw of the beast behind you, the heat coming off it makes you pass out saving you from the worst of it. Yet in your dreams you see it...")
    monsterDescription()
    pause()


def waitDeath():
    consoleMessages("end",
                    "You know what's coming and you decide to accept it, that doesn\'t make it any less terrifying when you feel something approaching you. Darkness overtakes you as your heart is pierced by an invisible appendage.")
    time.sleep(5)


def prizes():
    print(
        "You go up to the counter to look at the prizes, there's plenty of normal prizes like army men, gum and much much more. But what catches your eyes is a Golden Key inscribed with the word Ford. A strange feeling comes over you as you look at the key, almost like this why you\'re here. You don\'t have the tickets to buy it though, what do you do?")
    time.sleep(5)
    print("1 Steal tickets")
    print("2 Beg for tickets")
    print("3 Bully kids for tickets")
    print("4 Try to steal the keys")
    time.sleep(1)
    choice = chooseOption(4)

    if 1 == choice:
        stealTicket()
    elif 2 == choice:
        begTicket()
    elif 3 == choice:
        bullyTicket()
    elif 4 == choice:
        stealKey()
    else:
        print("Error")


def stealTicket():
    print(
        "You decide to steal tickets to buy the keys, you walk around grabbing tickets that fell or hanging out of pockets. After a few minutes of thievery you collected enough tickets to buy the Key. But before you can buy it the manager approaches you and accuses you of stealing tickets from children. What do you do?")
    time.sleep(4)
    print("1 Return the tickets")
    print("2 Deny it")
    choice = chooseOption(2)

    if choice == 1:
        returnTicket()
    elif choice == 2:
        deny()
    else:
        print("Error")


def returnTicket():
    consoleMessages("end",
                    "The manager thanks for returning tickets but still asks you to leave, upon exiting the building you hear a voice booming from some hidden location. \"Simulation failed... Rebooting.\"")
    time.sleep(5)


def deny():
    print(
        "The manager is forced to call the police, they demand you return the tickets and come with them, what do you do?")
    time.sleep(1)
    print("1 Punch the officer and run away")
    print("2 Surrender the tickets and run away")
    print("3 Surrender the tickets and go with them")
    time.sleep(2.3)
    choice = chooseOption(3)

    if choice == 1:
        shot()
    elif choice == 2:
        surrender()
    elif choice == 3:
        comply()
    else:
        print("Error")


def shot():
    consoleMessages("end",
                    "You sucker punch the closest officer and run, you make it about 5 steps away before his partner tases you. You pass out from the pain, in your dreams your haunted by images of some fell creature following... no, hunting you.")
    time.sleep(3)
    monsterDescription()
    pause()


def surrender():
    consoleMessages("end",
                    "You give them the tickets and run, they pursue you into the street where you forget to look both ways. A passing bus turns you into a fine paste.")
    pause()


def comply():
    consoleMessages("end",
                    "You fully comply with the officers and they bring you down to the station. You are alone in a holding cell when the door slams open to reveal... nothing. Your skin begins to burn as your legs collapse beneath you, you look up as the lights go out. As your head leaves your body you have a vision of your killer.")
    time.sleep(5)
    monsterDescription()
    pause()


def begTicket():
    consoleMessages("secret", "What do you think this is Communism? No Tickets for you!")
    time.sleep(2)
    print("You are unable to get any tickets before the store closes ")


def bullyTicket():
    print(
        "You find small children and threaten them until they give you your tickets, you manage to collect enough to buy the Key. You go to the counter to purchase the Key.")
    time.sleep(2)
    buyKey()


def buyKey():
    print("You buy the key with your tickets, as you pick it up you feel nauseous and pass out. ")
    global key
    key = True


def stealKey():
    print(
        "You carefully distract the worker behind the counter by saying that someone diarreahead all over the PacMan machine. While she's gone you grab the Key and run, you feel accomplished but you know your journey isn't over yet.")
    time.sleep(3)
    global key
    key = True


########################## CLIFF PATH #######################
# rename function to reflect your actual location/scene/action
def cliffStart():
    print("The door opens to reveal an icy windshield, and a steering wheel in front of you.")
    time.sleep(1)
    print("The rumble of a motor and the keys in the ignition, you're moving. Fast. It's slippery")
    time.sleep(1)
    print("The road tilts down, you're on a hill, you're going 60km/h")
    time.sleep(1)
    pause()
    print(
        "You approach a sharp, icy, turn, the road continues left, the right is met with a cliff, where will you go? What will you do?")
    # list players options
    print("1 Brake and turn left")
    print("2 Brake and turn right")
    print("3 Turn right")
    print("4 Hard turn left, no braking")
    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(4)
    if 1 == choice:
        cliffCrash()
    elif 2 == choice:
        cliffDeath("turnRight")
    elif 3 == choice:
        cliffDeath("turnRight")
    elif 4 == choice:
        cliffDeer()
    else:
        print("Error")


def cliffCrash():
    print("You made the wrong decision, the ice gets to you..")
    time.sleep(1)
    print("You're in a ditch, your head hurts, there's a forest around you.")
    time.sleep(1)
    print("You're eyes open to smoke, your engine is on fire")
    time.sleep(1)
    pause()
    print("Escape is vital, but what is the best option?")
    time.sleep(0.5)
    print("There is a gas leak.")
    # list players options
    print("1 Climb out the window")
    print("2 Wait until help arrives")
    print("3 Assess the car")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(3)
    if 1 == choice:
        cliffDeath("window")
    elif 2 == choice:
        crashWait()
    elif 3 == choice:
        crashAssess()
    else:
        print("Error")


def cliffDeath(instance):
    if instance == "turnRight":
        print(
            "Your wheels lock up and catch the ice, not knowing why you want this, you continue pressing forward, slipping far off the cliff")
        time.sleep(1)
        pause()
        print("As the car leaves the cliff you start to ask youself")
        time.sleep(2)
        print("Why have I just driven off a cliff..")
        time.sleep(2)
        print("Why am I here...")
        time.sleep(2)
        print("What's the purpose?")
        time.sleep(2)
        pause()
        consoleMessages("end", "As you hit the ground you start to hear a familiar sound")
    elif instance == "brake":
        print("You come to a stop, the deer safely presses forward..")
        time.sleep(2)
        pause()
        print("But that's not the issue, the issue is what's in front of you now that you've stopped.")
        time.sleep(2)
        print("You..")
        time.sleep(0.5)
        print("What.....?")
        time.sleep(0.5)
        monsterDescription()
        pause()
        print("You can't move, nothing works, what is there to do?")
        time.sleep(1)
        print("You can't win, you know that")
        time.sleep(1)
        print("You'll never win")
        time.sleep(1)
        consoleMessages("end",
                        "Something swells within you as you are dismembered, an obnoxious noise reminds you of &#@$^@#^$@&#... you can't quite remember")
    elif instance == "window":
        print("You crawl out of the window")
        time.sleep(2)
        print("You start to hear... something around you")
        time.sleep(2)
        print("There's a facility in the distance, you remember wanting to be there.. it was")
        time.sleep(2)
        print("safe?")
        time.sleep(0.5)
        print("A horrifying chill runs down your spine")
        time.sleep(1)
        print("You hear what you know you shouldn't hear, the car explodes..")
        time.sleep(1)
        print("But that's not what's bothering you..")
        time.sleep(1)
        print("It's...")
        pause()
        time.sleep(1)
        print("Inevitable... You saw it coming")
        time.sleep(2)
        print("But you can see nothing")
        time.sleep(1)
        print("But you know....")
        time.sleep(1)
        monsterDescription()
        pause()
        print(
            "Paralyzed in fear, you collapse to see in the distance, just out of your grasp, your objective, the escape.")
        time.sleep(2)
        print("Just out of reach...")
        consoleMessages("end",
                        "The escape of death only brings you back to another beginning, time to reboot, @#$%^&* always wins.")


def cliffDeer():
    print("You safely make the turn to continue your journey")
    time.sleep(1)
    print("The icy road continues for a straight away..")
    time.sleep(1)
    print("You move to check on the mirror behind you")
    time.sleep(1)
    pause()
    print("A deer jumps out in front of you")
    print("What's the best course of action?")
    # list players options
    print("1 Swerve")
    print("2 Brake")
    print("3 Step on the gas")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(3)
    if 1 == choice:
        cliffCrash()
    elif 2 == choice:
        cliffDeath("brake")
    elif 3 == choice:
        cliffPark()
    else:
        print("Error")


def crashWait():
    print("You sit in the vehicle contemplating everything")
    time.sleep(1)
    print("You can't wait any longer you know it will end bad..")
    time.sleep(2)
    pause()
    print("What do you want to do? Help is not coming, it never has.")
    # list players options
    print("1 Climb out the window")
    print("2 Assess the car")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(2)
    if 1 == choice:
        cliffDeath("window")
    elif 2 == choice:
        crashAssess()
    else:
        print("Error")


def crashAssess():
    print("You take a second to really examine the car")
    time.sleep(1)
    print("There is a glovebox to your right, with something hanging out of it")
    time.sleep(1)
    print("You reach for it to hear.. chatter")
    time.sleep(1)
    pause()
    print(radioArt)
    print("You've aquired a radio, almost instantly a dark and foreboding prescene approaches")
    time.sleep(1)
    print(
        "You notice him, but now that you have the radio, you realise you've won, you're one step closer. He can do nothing about it, but you know he will still rip you to pieces")
    time.sleep(2)
    consoleMessages("win",
                    "#$%#$%#$ made quick work of you, but the familiar beeping at your side in your dreams tells you, you've kept the radio, another step forward, another piece of the puzzle.")
    global radio
    radio = True


def cliffPark():
    print("You step on the gas and plow through towards the facility, the deer isn't so lucky...")
    pause()
    print("You head down the icy road to a facility where you can safely park your vehicle, it grinds to a stop, this is it, you're here")
    time.sleep(1)
    print("There's little to decide now, what's happening?")
    print("1 Go inside")
    print("2 Wait for something to happen")
    print("3 Get ouside and look around")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(3)
    if 1 == choice:
        facilityEnter()
    elif 2 == choice:
        facilityWait()
    elif 3 == choice:
        facilityExplore()
    else:
        print("Error")


def facilityWait():
    print("You sit in the vehicle contemplating everything")
    time.sleep(1)
    print("You can't wait anylonger you know it will end bad..")
    time.sleep(2)
    pause()
    print("What do you really want to do? You have to make something happen.")
    # list players options
    print("1 Exit and explore")
    print("2 Assess the car")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(2)
    if 1 == choice:
        facilityExplore()
    elif 2 == choice:
        crashAssess()
    else:
        print("Error")


def facilityExplore():
    print("You try to look around")
    time.sleep(2)
    print("you start to weaken, before long you can't even feel your legs, it's so cold")
    time.sleep(2)
    print("You look up to hear..")
    time.sleep(2)
    print("The familiar jingle")
    time.sleep(1)
    print("And prancers bells..")
    time.sleep(1)
    print("But Santa is not there, there is meerly an empty sleigh, that's getting closer")
    pause()
    consoleMessages("end",
                    "You try and figure out what is happening, then it hits you. Literally. You'll never live that one down.")


def facilityEnter():
    print("You creak open the doors to get inside, this is it")
    time.sleep(1)
    print("You look inside to see nothing..")
    time.sleep(1)
    print("But there is some faint chatter coming from one distant room")
    time.sleep(0.5)
    print("You need to act fast, you hear footsteps all around you, you might get caught")
    print("What's the course of action? There's only two options, the rest of the facility is seemingly empty")
    # list players options
    print("1 Go to the room")
    print("2 Leave and explore")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(2)
    if 1 == choice:
        facilityEnd()
    elif 2 == choice:
        facilityExplore()
    else:
        print("Error")


def facilityEnd():
    print("This is it, you creep open the door to peak around")
    time.sleep(2)
    print("You can't understand what you see")
    time.sleep(2)
    print("It's a handheld radio..")
    print("You feel an overwhelming urge to pick it up, now that it's in your hands you feel relieved")
    time.sleep(3)
    print("That raises the question, where were those footsteps coming from")
    time.sleep(2)
    print("Then your realise what they were...")
    time.sleep(1.5)
    print("Or rather..")
    time.sleep(1.5)
    print("What they were")
    time.sleep(1.5)
    monsterDescription()
    pause()
    consoleMessages("win",
                    "You feel a sense of relief as you're being mauled as you have what you came for, even though your not sure, it feels like you made the right decision given the circumstances.")
    global radio
    radio = True


########################## LAB #######################
# rename function to reflect your actual location/scene/action
def radioChatter():
    playsound("Media/Door.mp3")
    print("You pull out your radio and really listen to what it has to say")
    consoleMessages("radio", "HELLO... Hello?? I know you can hear me I can see you on the cameras")
    pause()
    consoleMessages("radio",
                    "If you want to see what's really happening, pull the lever on your left, it'll turn on the lights")
    time.sleep(2)
    print(narratorDialogue(
        "Don't listen to him, he's just lying to you. Let me take control, I will fix everything, it will be nice again"))
    pause()
    print("The choice is yours, what will you do?")
    # list players options
    print("1 Pull the lever")
    print("2 Release control")

    # handle player"s selection to jump to other locations/scenes/actions
    choice = chooseOption(2)
    if 1 == choice:
        labLever()
    elif 2 == choice:
        controlLost()
    else:
        print("Error")


def controlLost():
    print("You release control of the simulation and submit it to him")
    time.sleep(2)
    print(narratorDialogue("Ah, I love this. It has been so long"))
    pause()
    print("Quickly realising you have made a mistake, you try to take back the simulation")
    time.sleep(2)
    print(narratorDialogue(
        "Nơt ҉so ҉fast, ́y̧o͢ù d̡o̵n'̛t͠ c̡ońt̶r̛o͜l̢ ̵any͜th͏in͠g ̧any҉m̧or̵e,̀ ́it's ͜aĺl m̛i͞ņe͟.́"))
    time.sleep(2)
    print("You are petrified in fear as you suddenly feel a rush of a hauntingly familiar presence")
    time.sleep(2)
    print("He is here, he is in control. Praise him.")
    pause()
    print(narratorDialogue("Thi̶s͜ is ́all̶ I̢ ̡nee̶de͞d͠,̵ i͞t's͞ ̀al̸l̕ ͜ovèr ͞f͜or̷ ҉you ̡no͘w҉.̢ ͢Goo͝db̕ye.̨"))
    time.sleep(2)
    consoleMessages("win", "You are made quick work of... but the simulation is no more, you are free, but the character you control wasn't so lucky...")
    time.sleep(2)

    # End the game...
    print("Quitting...")
    time.sleep(0.3)
    sys.exit(0)
    quit()


def labLever():
    print("You reach for the lever, it has all come to this")
    print(leverArt)
    playsound("Media/Lever.mp3")
    time.sleep(1)
    print("with a pull, the lever flicks and the lights turn on, everything is illuminated, you notice a strong presence through a tinted window across the lab.")

    consoleMessages("radio", "You did it! You actually did it! You can escape, you will escape.")
    time.sleep(1)
    consoleMessages("radio",
                    "The simulation is down, it will reboot in 5 minutes, be quick, this is your only chance. There is a console over there, go break the code. You can do it")
    print(narratorDialogue(
        "Stop listening to him.. You know me... This is all a setup, give me control, I will fix this blip and return things to the way we want them. Give me control."))
    pause()
    print(
        "As you see it you have 3 choices, you can try to leave this place, you can give control or you can break the code. What do you do?")

    print("1 Run")
    print("2 Give Control")
    print("3 Destroy the Code")

    choice = chooseOption(3)
    if 1 == choice:
        run()
    elif 2 == choice:
        controlLost()
    elif 3 == choice:
        destroyCode()
    else:
        print("Error")


def run():
    print(
        "You run as far as you can away from the &#&%$&#& but to no avail. In your haste you drop your radio, it cracks open to reveal a dwarf inside,but you don't have time to ponder the sillyness of the simulation. He screams in complete terror as the distortion in reality approaches him, he is devoured in the second it took you to blink.")
    time.sleep(2)
    consoleMessages("end",
                    "You make it to a door through which you can see the outside world, it is locked. You desperately pull on the handle but it won't open. You feel... you feel the beast come up behind you and lean close to your ear. It breathes heavily on the back of your neck and then impales you with a spike through your stomach, you die a horrible and painful death for what seems like an eternity of torment")
    print("Quitting...")
    time.sleep(0.3)
    sys.exit(0)
    quit()


def destroyCode():
    print("You follow the instructions of the radio and you move towards the console.")
    print(narratorDialogue("I'm starting to get impatient, you better give up control"))
    time.sleep(2.5)
    print("Seeing as you have already made your decision thus far, you push forward to break the code.")
    print(consoleArt)
    pause()
    hackSuccess = hackChallenge(10, 20)
    if hackSuccess == True:
        brokenCode()
    elif hackSuccess == False:
        failedCode()


def brokenCode():
    print("You've broken the simulation, you hear a door open on the other side of the room")
    consoleMessages("radio", "You've done it, you can escape, there is nothing left for you here. GET OUT NOW")
    pause()
    print(narratorDialogue("Don't think you're getting out that easy, this is what you need, you need me."))
    time.sleep(2)
    print("You make a dash for the door, you need to get out..")
    pause()
    print("The glass shatters behind you")
    print(narratorDialogue("N̛ow̶ th̴a͝t͢ ͡I͏'m out̷ t̶he͟r̴e įs̀ ̡no҉ ͠hope f͏o͘r you.̀"))
    pause()
    consoleMessages("radio", "You can make it, just RUNNNNN")
    time.sleep(2)
    print("You make a final stride through the door")
    time.sleep(2)
    print("It shuts behind you")
    pause()
    consoleMessages("win",
                    "You've escaped, you don't know what this new world is, but it's an adventure, there is a future for you now. A future of freedom.")
    pause()
    consoleMessages("secret", "Goodbye, for now.")
    # End the game...
    print("Quitting...")
    time.sleep(0.3)
    sys.exit(0)
    quit()


def failedCode():
    print("You realise now that you have failed everything, and it's all over.")
    consoleMessages("radio", "How could you have failed this, we were so close... Whyyyyyyy")
    pause()
    print("The distress you feel is nothing compared to what is about to come.")
    time.sleep(2)
    print(narratorDialogue("Thi̶s͜ is ́all̶ I̢ ̡nee̶de͞d͠,̵ i͞t's͞ ̀al̸l̕ ͜ovèr ͞f͜or̷ ҉you ̡no͘w҉.̢ ͢Goo͝db̕ye.̨"))
    print("Terror fills your body as you realise who was running the simulation, but at least it's over.")
    pause()
    consoleMessages("win",
                    "You are made quick work of... but the simulation is no more, you are free, but you feel like the man you control wasn't so lucky...")
    time.sleep(2)

    # End the game...
    print("Quitting...")
    time.sleep(0.3)
    sys.exit(0)
    quit()


###################### ASCII ART ############################

# http://patorjk.com/software/taag/#p=testall&h=2&f=TRaC&t=Ambiguous%20Shadow
titleArt = r"""
 ▄▄▄· • ▌ ▄ ·. ▄▄▄▄· ▪   ▄▄ • ▄• ▄▌      ▄• ▄▌.▄▄ ·     .▄▄ ·  ▄ .▄ ▄▄▄· ·▄▄▄▄       ▄▄▌ ▐ ▄▌
▐█ ▀█ ·██ ▐███▪▐█ ▀█▪██ ▐█ ▀ ▪█▪██▌▪     █▪██▌▐█ ▀.     ▐█ ▀. ██▪▐█▐█ ▀█ ██▪ ██▪     ██· █▌▐█
▄█▀▀█ ▐█ ▌▐▌▐█·▐█▀▀█▄▐█·▄█ ▀█▄█▌▐█▌ ▄█▀▄ █▌▐█▌▄▀▀▀█▄    ▄▀▀▀█▄██▀▐█▄█▀▀█ ▐█· ▐█▌▄█▀▄ ██▪▐█▐▐▌
▐█ ▪▐▌██ ██▌▐█▌██▄▪▐█▐█▌▐█▄▪▐█▐█▄█▌▐█▌.▐▌▐█▄█▌▐█▄▪▐█    ▐█▄▪▐███▌▐▀▐█ ▪▐▌██. ██▐█▌.▐▌▐█▌██▐█▌
 ▀  ▀ ▀▀  █▪▀▀▀·▀▀▀▀ ▀▀▀·▀▀▀▀  ▀▀▀  ▀█▄▀▪ ▀▀▀  ▀▀▀▀      ▀▀▀▀ ▀▀▀ · ▀  ▀ ▀▀▀▀▀• ▀█▄▀▪ ▀▀▀▀ ▀▪
"""

# https://ascii.co.uk/art/key
keyArt = r"""

    _____________
   /      .      \
   [] :: (_) :: []
   [] ::::::::: []
   [] :F:O:R:D: []
   [] ::::::::: []
   [_____________]
       I     I
       I_   _I
        /   \
        \   /
        (   )
        /   \
        \___/

"""
# https://ascii.co.uk/art/radio
radioArt = r"""

                       |
                       |  
                       |  
         .============.|  
       .-;____________;|.    
       | [_________I__] |     
       |  ''''' (_) (_) |
       | .=====..=====. |
       | |:::::||:::::| |
       | '=====''=====' |
       '----------------'

"""
# https://ascii.co.uk/art/lever
leverArt = r"""

      ___ (@)
     |.-.|/
     || |/
     || /|
     ||/||
     || ||
     ||_||
     '---'

"""
# https://www.asciiart.eu/computers/game-consoles
consoleArt = r"""

 _____________________________   
/        _____________        \  
| == .  |             |     o |  
|   _   |             |    B  |  
|  / \  |             | A   O |  
| | O | |             |  O    |  
|  \_/  |             |       |  
|       |             | . . . |  
|  :::  |             | . . . |  
|  :::  |_____________| . . . |  
|                             |  
\_____________________________/

"""
# https://ascii.co.uk/art/doors
closedDoorArt = r"""

 ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |

| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_|

"""
# https://ascii.co.uk/art/doors
openDoorArt = r"""

 ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |   | |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|

"""
###################### THE MAIN GAME LOOP ############################
# ------------------Game Loop ------------------------
respawn = 0
titleShown = False
while True:

    # Start the game
    # Tutorial user intro
    if titleShown == False:
        titleScreen()
        titleShown = True
    spawnRoom()

    # "Play again" user option
    print("\nSimulation finished, return to testing room?")
    playAgain = input("Y/N> ")
    if playAgain == "Y" or playAgain == "y":
        print("\n")
        continue
    elif playAgain == "N" or playAgain == "n":
        break  # leave while loop
    break

# End the game...
print("Quitting...")
sys.exit(0)
quit()
