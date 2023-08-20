# imports modules to be used in program
import random
import turtle


# outputs a message
def output(message):
    print(message + "\n\n")

# draws a line with a turtle
def draw_line(turtle,xcor,ycor,length,heading):
    turtle.penup()
    turtle.setposition(xcor,ycor)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.forward(length)
    
# procedure that moves the player turtle in a direction
def move_player(direction,player):
    headings = [90,360,270,180]
    player.setheading(headings[direction])
    player.forward(100)
        
# creates an instance of the Player class
def initialise_Player():
    global player
    player = Player(25,True,15,False)
    return player


# -------------------------------------------------------------------------------------------------------------------------


# class used to store data for the player
class Player:

    floor = 0
    room = 0
    alive = True
    difficulty = 1.0

    @staticmethod
    def increase_difficulty():
        Player.difficulty += 0.4

    def __init__(self,health,item,mana,key):
        self.health = health
        self.item = item
        self.mana = mana
        self.key = key

    def use_item(self):
        self.health += 15
        if self.health > 25:
            self.health = 25
        self.item = False

    def use_magic(self):
        damage = 0 
        if self.mana >= 5:
            damage = random.randint(10,13)
            self.mana -= 5
        return damage

    def take_hit(self):
        damage = random.randint(3,8)
        self.health -= damage
        output("you took " + str(damage) + " damage from the enemie")
        return self.health



# ----------------------------------------------------------------------------------------------------------------------------------------



# procedure to draw a blue square over the screen
def reset_floor():
    floor = turtle.Turtle()
    floor.penup()
    floor.pensize(7)
    floor.pencolor("black")
    floor.setposition(-260,260)
    floor.pendown()
    floor.speed(0)
    floor.setheading(90)
    floor.fillcolor("darkgrey")
    floor.begin_fill()
    for i in range(0,4):
        floor.right(90)
        floor.forward(520)
    floor.end_fill()
    floor.hideturtle()


# function that draws floor1 and returns a turtle to act as the player
def create_floor0():
    background = turtle.Screen()
    background.bgcolor("darkgreen")
    
    walls = turtle.Turtle()
    walls.penup()
    walls.pensize(10)
    walls.setposition(-150,150)
    walls.setheading(360)
    walls.pendown()
    walls.speed(0)
    walls.pencolor("grey")
    walls.forward(100)
    walls.pencolor("brown")
    walls.forward(100)
    walls.pencolor("grey")
    walls.forward(100)
    for i in range(0,3):
        walls.right(90)
        walls.forward(300)
    walls.hideturtle()
    
    playerTurtle = turtle.Turtle()
    playerTurtle.setheading(90)
    playerTurtle.penup()
    playerTurtle.color("yellow")
    playerTurtle.turtlesize(3)
    playerTurtle.setposition(0,0)

    return playerTurtle


def create_floor1():
    reset_floor()
    
    walls = turtle.Turtle()
    walls.penup()
    walls.pensize(4)
    walls.setposition(-200,200)
    walls.setheading(90)
    walls.pendown()
    walls.speed(0)
    walls.fillcolor("grey")
    walls.begin_fill()
    for i in range(0,4):
        walls.right(90)
        walls.forward(400)
    walls.end_fill()

    # draws interior walls for floor 1
    draw_line(walls,-200,100,200,360)
    draw_line(walls,0,100,100,270)
    draw_line(walls,0,0,100,180)
    draw_line(walls,100,200,300,270)
    draw_line(walls,100,-100,200,180)
    walls.hideturtle()

    door = turtle.Turtle()
    door.penup()
    door.setposition(100,-100)
    door.pendown()
    door.pensize(2.5)
    door.pencolor("brown")
    door.forward(100)
    door.penup()
    door.setposition(100,200)
    door.forward(100)
    door.hideturtle()

    playerTurtle = turtle.Turtle()
    playerTurtle.penup()
    playerTurtle.color("yellow")
    playerTurtle.turtlesize(3)
    playerTurtle.setposition(-50,-150)
    playerTurtle.setheading(180)

    return playerTurtle


def create_floor2():
    reset_floor()

    walls = turtle.Turtle()
    walls.penup()
    walls.pensize(4)
    walls.setposition(-200,250)
    walls.setheading(360)
    walls.pendown()
    walls.speed(0)
    walls.fillcolor("grey")
    walls.begin_fill()
    for i in range(0,2):
        walls.forward(400)
        walls.right(90)
        walls.forward(500)
        walls.right(90)
    walls.end_fill()

    draw_line(walls,100,-250,300,90)
    draw_line(walls,0,-50,300,90)
    draw_line(walls,200,150,100,180)
    draw_line(walls,0,50,100,180)
    draw_line(walls,-100,-50,200,270)
    draw_line(walls,-100,-150,100,360)
    draw_line(walls,-100,250,100,270)
    walls.hideturtle()

    door = turtle.Turtle()
    door.pensize(4)
    door.speed(0)
    door.pencolor("brown")
    draw_line(door,-200,250,100,360)
    draw_line(door,100,-250,100,360)
    draw_line(door,-100,150,100,180)
    door.hideturtle()

    playerTurtle = turtle.Turtle()
    playerTurtle.penup()
    playerTurtle.color("yellow")
    playerTurtle.turtlesize(3)
    playerTurtle.setposition(150,-200)
    playerTurtle.setheading(90)

    return playerTurtle


def create_floor3():
    reset_floor()

    walls = turtle.Turtle()
    walls.penup()
    walls.pensize(4)
    walls.setposition(-200,150)
    walls.setheading(360)
    walls.pendown()
    walls.speed(0)
    walls.fillcolor("grey")
    walls.begin_fill()
    for i in range(0,2):
        walls.forward(400)
        walls.right(90)
        walls.forward(300)
        walls.right(90)
    walls.end_fill()

    draw_line(walls,100,-150,200,90)
    walls.hideturtle()

    playerTurtle = turtle.Turtle()
    playerTurtle.penup()
    playerTurtle.color("yellow")
    playerTurtle.turtlesize(3)
    playerTurtle.setposition(-150,-100)
    playerTurtle.setheading(90)

    return playerTurtle


# -------------------------------------------------------------------------------------------------------------------------------


# function to simulate combat with an enemie
def enter_combat(player):

    # initialises local variables
    combat = True
    enemie = {"health":8*Player.difficulty,"alive":True}
    
    # informs player they are in combat
    output("you have entered combat\nhealth: " + str(player.health))

    # starts combat loop
    while combat:
        # asks player for input
        action = input("what do you do?\n (attack, heal, magic)").lower()
        # will attack enemie if the player inputs "attack"
        if action == "attack":
            damage = random.randint(7,10)# damage delt will be randomized
            enemie["health"] -= damage
            output("you did " + str(damage) + " damage")

        # will use magic if pplayer inputs "magic"
        if action == "magic":
            damage = player.use_magic()
            if damage > 0:# will only cast spell if it does damage
                enemie["health"] -= damage
                output("you cast a fireball\nyou did " + str(damage) + " damage")
                output("mana remaning: " + str(player.mana))
            else:
                # informs player they do not have the requirements to cast a spell
                output("you dont have enouth mana to cast a spell")

        # will heal player if they input "heal"
        if action == "heal":
            if player.item == True:
                player.use_item()
                output("you healed 15 health")
            else:
                output("you dont have any healing items")
        
        # ends combat when enemie is killed
        if enemie["health"] <= 0:
            # marks the enemie as dead
            enemie["alive"] = False
            combat = False
            output("enemie has been killed")

        # enemie will hit player if they are alive
        if enemie["alive"] == True:
            player.take_hit()
            output("health: " + str(player.health))

        # will end combat and game if player dies
        if player.health <= 0:
            combat = False
            Player.alive = False
            output("you have died")

    return player


# ------------------------------------------------------------------------------------------------------------------------------------


def floor0():
    # room:  0  1  2  3  4  5  6  7  8 | direction:
    map = [[-1,-1,-1, 0, 1, 2, 3, 4, 5], #N
           [ 1, 2,-1, 4, 5,-1, 7, 8,-1], #E
           [ 3, 4, 5, 6, 7, 8,-1,-1,-1], #S
           [-1, 0, 1,-1, 3, 4,-1, 6, 7]] #W
    
    playerTurtle = create_floor0()
    player = initialise_Player()
    Player.room = 4
    enemies = {"room":[],"alive":[]} # keeps track of enemie status' and location for room 1
    # keeps track of props status' and location for room 1
    room_props = {"key":{"room":-1,"used":False}, "door":{"room":-1}, "item":{"room":-1,"used":False}, "exit":{"room":1}, "fountian":{"room":-1}}
    
    gameloop(map,player,playerTurtle,enemies,room_props)

def floor1():
    # room:   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 | direction:
    map =  [[-1,-1,-1, 2, 3,-1, 7,-1,-1, 6,-1,-1,13,14,15,-1], #N
            [ 1, 2,-1,-1,-1, 4, 5, 8,-1,10,11,12,-1,-1,-1,-1], #E
            [-1,-1, 3, 4,-1,-1, 9, 6,-1,-1,-1,-1,-1,12,13,14], #S
            [-1, 0, 1,-1, 5, 6,-1,-1, 7,-1, 9,10,11,-1,-1,-1]] #W
    
    playerTurtle = create_floor1()
    Player.room = 10
    enemies = {"room":[3,7,9,13],"alive":[True,True,True,True]} # keeps track of enemie status' and location for floor 1
    # keeps track of props status' and location for floor 1
    room_props = {"key":{"room":0,"used":False}, "door":{"room":12}, "item":{"room":8,"used":False}, "exit":{"room":15}, "fountian":{"room":-1}}
    
    gameloop(map,player,playerTurtle,enemies,room_props)


def floor2():
    # room:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 | direction:
    map = [[ 1, 2, 3,-1, 5,-1,-1, 4, 7, 8,-1,12,-1,16,13,14,19,18,-1,-1], #N
           [-1,-1,-1,-1, 3, 6,-1,-1,-1,-1, 9, 8,-1,12,-1,-1,17,-1,-1,-1], #E
           [-1, 0, 1, 2, 7, 4,-1, 8, 9,-1,-1,-1,11,14,15,-1,13,-1,17,16], #S
           [-1,-1,-1, 4,-1,-1, 5,-1,11,10,-1,-1,13,-1,-1,-1,-1,16,-1,-1]] #W

    playerTurtle = create_floor2()
    Player.room = 0
    player.key = False
    enemies = {"room":[5,7,14,17],"alive":[True,True,True,True]} # keeps track of enemie status' and location for floor 2
    # keeps track of props status' and location for floor 2
    room_props = {"key":{"room":15,"used":False}, "door":{"room":16}, "item":{"room":6,"used":False}, "exit":{"room":19}, "fountian":{"room":10}}
    
    gameloop(map,player,playerTurtle,enemies,room_props)


def floor3():
    # room:   0  1  2  3  4  5  6  7  8  9 10 11  | direction:
    map =  [[ 5, 4, 3, 8, 7, 6,-1,-1,-1,-1, 9,10], #N
            [ 1, 2,-1,-1, 3, 4, 7, 8, 9,-1,-1,-1], #E
            [-1,-1,-1, 2, 2, 0, 5, 4, 3,10,11,-1], #S
            [-1, 0, 1, 4, 5,-1,-1, 6, 7, 8,-1,-1]] #W

    Player.difficulty = 3
    playerTurtle = create_floor3()
    Player.room = 0
    enemies = {"room":[10],"alive":[True]} # keeps track of enemie status' and location for floor 3
    # keeps track of props status' and location for floor 2
    room_props = {"key":{"room":-1,"used":True}, "door":{"room":-1}, "item":{"room":4,"used":False}, "exit":{"room":11}, "fountian":{"room":-1}}
    
    gameloop(map,player,playerTurtle,enemies,room_props)




# ------------------------------------------------------------------------------------------------------------------------



def gameloop(map,player,playerTurtle,enemies,room_props):
    
    while Player.alive and Player.room != room_props["exit"]["room"]:
        try:
            direction = int(input("pick a direction\n(0:North, 1:East, 2:South, 3:West)  \n"))
        except:
            direction = -1

        if direction != 0 and direction != 1 and direction != 2 and direction != 3:
            pass
        else:
            if map[direction][Player.room] != -1 and Player.room == room_props["door"]["room"] and direction == 0:
                if player.key == False:
                    output("you need key to go throught door")
                else:
                    output("you unlock the door with the key")
                    Player.room = map[direction][Player.room]
                    move_player(direction,playerTurtle)
                    output("you have moved to room " + str(Player.room))

            elif map[direction][Player.room] != -1:
                Player.room = map[direction][Player.room]
                move_player(direction,playerTurtle)
                output("you have moved to room " + str(Player.room))
            else:
                output("you have hit a wall")

            for i in range(0,len(enemies["room"])):
                if Player.room == enemies["room"][i] and enemies["alive"][i] == True:
                    player = enter_combat(player)
                    enemies["alive"][i] = False
                    Player.increase_difficulty()        

            if Player.room == room_props["key"]["room"] and room_props["key"]["used"] == False:
                player.key = True
                room_props["key"]["used"] = True
                output("you picked up a key")
    
            if Player.room == room_props["exit"]["room"]:
                Player.floor += 1
                output("you are now on floor " + str(Player.floor))

            if Player.room == room_props["fountian"]["room"]:
                Player.mana = 15
                output("your mana is restored")

            if Player.room == room_props["item"]["room"] and room_props["item"]["used"] == False:
                output("you find an item")
                if input("pick it up? (yes,no) ").lower() == "yes":
                    player.item = True
                    room_props["item"]["used"] = True
                    output("you pick up a health potion")


# ------------------------------------------------------------------------------------------------------------------------


def progress_floor():
    if Player.alive:
        floor0()
    if Player.alive:
        floor1()
    if Player.alive:
        floor2()
    if Player.alive:
        floor3()
    if Player.alive:
        output("you have beat the game")
        input("")

progress_floor()