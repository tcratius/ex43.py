# ex43.py
Gothon game
## This is the orginal game from exercise 43 in "learn python the hardway" with an extra fight scene.

```
class LockerRoom(Scene):

    def enter(self):
        global weapon
        global item

        item = ["Rock", "Torch", "Gun",]
        weapon = None
```

```
class Battle(Scene):

    def enter(self):

        if weapon == "Gun":
            print "\n"
            print "You see the Gothon walk with his back to you.  Taking your"
            print "Gun, you fire!  The clown looking creature stumbles a few"
            print "meters and dies"
            return 'laser_weapon_armory'
```
