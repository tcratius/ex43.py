from sys import exit
from random import randint

""" Class Scene takes has-a function named enter that takes
    parameters self"""

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

""" class Engine has-a function(s) named __init__ that takes parameters
    self, and scene_map & function play that has self parameters"""
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

"""class Death has-a function named enter that
    takes parameters self."""
class Death(Scene):

    quips = [
    "You died. You kinda suck at this.",
    "Your mom would be proud...if she were smarter.",
    "Such a luser.",
    "I have a small puppy thats better at this.",
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips) -1)]
        exit(1)

""" class CentralCorridor is-a Scene that has-a function named enter that
    takes self parameters"""
class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You are running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He is blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metall wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            print 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and cannot move."
            print "While he is laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'locker_room'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'



class LockerRoom(Scene):



    def enter(self):
        global weapon
        global item

        item = ["Rock", "Torch", "Gun",]
        weapon = None

        print "\n"
        print "You step into the crews locker room to escape one of the clowns"
        print "walking down the corridor.  You wait sometime before you move"
        print "just in case the hiddeous monster hears you. Looking around the room"
        print "you decide you must either leave or stay here and die"
        action = raw_input("[Decission]> ")


        if action == "open locker":
            weapon = item[randint(0, len(item)-1)]
            print "\n"
            print "You found a %s and decide it's about time you found" % weapon
            print "bomb and got off this ships"
            return 'battle'
        elif action == "leave room":
            print "\n"
            print "You leave the room too early and Gothonian grabs you by the throat"
            print "Instancely killing you."
            return 'death'
        else:
            print "DOES NOT COMPUTE"
            return 'locker_room'


class Battle(Scene):



    def enter(self):

        if weapon == "Gun":
            print "\n"
            print "You see the Gothon walk with his back to you.  Taking your"
            print "Gun, you fire!  The clown looking creature stumbles a few"
            print "meters and dies"
            return 'laser_weapon_armory'

        elif weapon == "Torch":
            print "\n"
            print "Hold the torch in your right hand you sneak up behind the Gothon"
            print "and hit him on the head.  The Gothon looks stunned as he turnes"
            print "to face you and rips off your face"
            return 'death'
        elif weapon == "Rock":
            print "\n"
            print "You look at the rock in your hand and hope for the best as"
            print "you quietly walk up the clown like creature from behind. You"
            print "the rock at his head and are rewarded with a loud crack."
            print "Checking the Gothon won't get up again, you move on."
            return 'laser_weapon_armory'
        else:
            print "\n"
            print "Thinking back to days in combat training, you look at your"
            print "and hope it's enough. With the stealth of a ninja, you creep"
            print "up behind the clown and give him an almight blow with you"
            print "fist, that barely affects the Gothon.  Quick as a flash he"
            print "turns and you feel his hands on your throat.  You are dead"
            return 'death'

        exit(1)




""" class LazerWeaponArmory is-a Scene that has-a function named enter
    that takes self parameters"""
class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It is dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There is a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you cannot"
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        if int(guess) == 000 or int(guess) == code:
            return 'the_bridge'
        else:
            while guess != code and guesses < 10:
                print "BZZZZEDDD!"
                guesses += 1
                guess = raw_input("[keypad]> ")

                if int(guess) == 000 or int(guess) == code:
                     print "The container clicks open and the seal breaks, letting gas out"
                     print "You grab the neutron bomb and run as fast as you can to the"
                     print "bridge where you must place it in the right spot"
                     return 'the_bridge'
                else:
                     print "The lock buzzes one last time and then you hear a sickening"
                     print "melting sound as the mechanism is fused together."
                     print "You decide to sit there, and finally the Gothons blow up the"
                     print "ship for their ship and you die"
                     return 'death'


""" class TheBridge is-a Scene that has-a function named enter
    that takes self parameters"""
class TheBridge(Scene):

    def enter(self):
        print "You burst on the Bridge with the netron destruct bomb"
        print "under you arm and surprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. The haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out"
            print "Now that the bomb is placed you run to the escape pod to"
            return  'escape_pod'
        else:
            print "DOES NOT COMPUTE"
            return 'the_bridge'



""" class EscapePod is-a Scene that has-a function name enter
    that takes self parameters"""
class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so you run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick on to take.  Some of them could be damaged"
        print "but you don't have the time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, takeing out the Gothon ship at the same"
            print "time. You won!"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'


""" class Map has-a 3 functions 1) __init__ takes self, start_scene.
    2) next_scene take self, and scene_name. 3) opening_scene takes
    self parameters"""
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'locker_room': LockerRoom(),
        'battle': Battle(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

""" set a_map to an instance of class map and call it with 'central_corridor'
    parameters"""
a_map = Map('central_corridor')

""" set a_game to an instance of class Engine and call it with
    a_map parameters"""
a_game = Engine(a_map)

""" from a_game get the function play and call it with parameters
    self"""
a_game.play()
