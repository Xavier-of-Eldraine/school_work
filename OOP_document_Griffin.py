"""
Griffin Stover
11/17/24
CRN:
Class: CIS 216
Estimated Time: 2 Hours
"""


#Welcome to my super professional and awesome introduction to some basic OOP stuff!
# Here's the outline: 
"""
x Classes
x Instance
x Private vs Public Variables
x Inheritance
x Multiple Inheritance  
x Polymorphism 
*Interfaces/Duck Typing
"""


#Let's begin with classes! 
    #A class is a user-defined blueprint for objects! A class can store variables, as well as methods(functions for a class). 
    #In order to use a class, you have to create an instance of it in the same way you'd think of calling on a function. 
    #Let's demonstrate these ideas with a bit of code!

def class_instance_ex():
    #Alright, we've got a baseline sword here! It can swing, and as it does so it swooshes. Nice!

    class Sword:
        #Your class can also store variables!
        times_swung = 0
        sword_type = 'Bronze'

        def __init__(self):
            self.times_swung = 0
            self.sound = "swoosh"
    
        def swing(self):
            print("The sword swings, {}".format(self.sound))
            #This one is a count up-ticker for all swords, like a master sword swing variable. It covers the entire sword class.
            Sword.times_swung += 1
            #This one is a counter for just the sword object. It's an individual tracker that goes on a per-sword basis. 
            self.times_swung += 1

    #Time to create an instance!
    #Instances are objects created from the class blueprint. You can think of them as realizations of the schematic laid out by the 
    #class. These allow for us to make a bunch of similar objects that all behave similarly, while saving us tons of time. Super neat!
    shortsword = Sword()
    longsword = Sword()

    #Now let's see it in action! To do so, let's call upon its method.
    shortsword.swing()
    #This allows us to see how many times our shortsword has been swung
    print("Shortsword swung {} time(s)".format(shortsword.times_swung))
    longsword.swing()
    #this does the same for our longsword!
    print("Longsword swung {} time(s)".format(longsword.times_swung))

    #I'm wondering what type of sword those are now... let's check!
    print(Sword.sword_type)
    #How many times have the swords been swung? 
    print("Total swings: ",Sword.times_swung)
    
    print("---------")
    #Let's try something different. Classes are able to accept arguments!
    class Egg:
        #By setting the argument to default to none, we'll get an output even if the user doesn't input a value for doneness.
        def __init__(self, doneness = None):
            self.doneness = doneness or 'Over Easy'

        def cook(self):
            print("Sizzle Sizzle...")
            print("Your {} egg is ready!".format(self.doneness))

    #Let's try this with no variables added and see the outcome:        
    breakfast = Egg("Over medium")
    breakfast.cook()
    return
    #With this demonstration we've gone over some of the utilities of classes! By counting sword swings across instances we can see
    #the total number of swings. We've also demonstrated how variables like sword type can be shared too! And with our egg class we
    #learned about arguments!

    #We've also learned a bit about instances! We learned how to call on it's methods with the swords by using
    # longsword/shortsword.swing(). With our eggs we learned about creating instances with arguments too, alongside default values that
    #we can use in case our user forgets to provide a value.

#Now onto Public and Private variables. 

def pub_priv():
    #As said in the example given for the assignment, there are public and private variables. Private variables are those which shouldn't be manipulated from outside of a class. Although
    #Python doesn't formally have these types of variables, they can be denoted by putting an '_" in front of the name. The sort of variables you'd want to make private are things like 
    #internal counters.

    class MusicPlayer:
        def __init__(self, song):
            #self.song would be public as it's not prefixed with an "_"! 
            self.song = song
            #self._counter would be private as it has that _! Don't tamper with this one!
            self._counter = 0
        
        def song_counter(self):
            print("Now playing: {}".format(self.song))
            self._counter += 1

    player = MusicPlayer("Bohemian Rhapsody")
    player.song_counter()
    print("Songs played:{}".format(player._counter))
    #We can see that the print statement involving the private variable does in fact work, even from outside of the class. This demonstrates that the "private" variable is still accessible, but
    #the _ indicates that it shouldn't be treated as such. self._song is open for use though!
    return

def inheritance():
    #Classes can inherit methods and properties from other classes! This is referred to as inheritance. The baseline class is referred to as the parent, and any classes which borrow from their code
    #are known as children. You can also ensure a child class has access to a parent's specific version of a function as well through the super() function!

    #Back to swords, because they're cool! Here's a basic one:
    class Sword:
        def __init__(self,material = None):
            self.material = material or 'Bronze'
        
        def swing(self):
            print("The {} sword is swung... Swoosh!".format(self.material))
        
    class HeroSword(Sword):
        def hero_swing(self):
            print("The Hero's {} Blade swings forth!".format(self.material))
        def normal_swing(self):
            super().swing()

    sword = Sword()

    hero_sword = HeroSword()

    sword.swing()
    hero_sword.hero_swing()
    print("And here's a totally normal swing:")
    hero_sword.normal_swing()
    #Here we demonstrated the power of inheritance! Our hero sword got it's material value from the Sword class, and even stole a function from its parent using super(). By passing in the parent class
    #like we could an argument in a function, we can cut down on the code we need to rewrite, increasing our efficiency!
    return

def multiple_inheritance():
    #If you must reuse code from two different code bases, you can use multiple inheritance! Be careful to not overlap methods while using this. If you do, the first class entered will take priority.

    class Wizard():
        def cast(self):
            print("I cast Fireball!")
        
        def walk(self):
            print("The wizard shuffles about")
    
    class Knight():
        def slash(self):
            print("The Knight's sword swings!")

        def walk(self):
            print("The Knight's armor clangs")
    #Note that Knight is first here.
    class EldritchKnight(Knight,Wizard):
        pass

    class BladeSinger(Wizard,Knight):
        pass

    player_1 = EldritchKnight()
    player_2 = BladeSinger()
    print("player 1's turn!")
    player_1.cast()
    player_1.slash()
    player_1.walk()
    print("------")
    print("player2's turn!")
    player_2.slash()
    player_2.cast()
    player_2.walk()

#As demonstrated by the elegant code above, despite being of two different classes, the BladeSinger and EldritchKnight both possess very similar capabilities. This is because they share parents,
#however there is a difference on what the 'primary' parent is! This determines their walk message, which shows as the walk function is called for both, with different outcomes. Be wary, as this is
#ambiguous code!
    return


def polymorphism():
    #If we know that an object or set of objects shares a common parent then you can operate on them as instances of that parent. This allows you to get the use of the parent class and the child class
    #interchangably. You can only call methods that are common to all children though, if you intend to iterate through a group of child classes. 

    class Adventurer:
        DEFAULT_HEALTH = None
        NAME = None
        
        def __init__(self,health = None):
            self._health = health or self.DEFAULT_HEALTH
            self._name = self.NAME
        
        def display_health(self):
            print("The {}'s health is: {}".format(self._name,self._health))
        
    class Wizard(Adventurer):
        DEFAULT_HEALTH = '15'
        NAME = 'Wizard'

        def cast(self):
            print("The Wizard casts!")
        
    class Fighter(Adventurer):
        DEFAULT_HEALTH = '30'
        NAME = 'Fighter'
        
        def slash(self):
            print("The Fighter slashes!")
    fighter = Fighter()
    wizard = Wizard()

    fighter.slash()
    wizard.cast()
    party = [fighter,wizard]
    for member in party:
        member.display_health()
    #Since both party members have a display health function due to their shared lineage(Adventurer), we can use a for loop to iterate through the party and display their healths easily! Of course,
    #asking a fighter to slash or a wizard to cast wouldn't work, so we keep the method generic. At the end of the day, all adventurers have health!   
    return

def interfaces_and_ducktyping():
    #As demonstrated above, polymorphism is powerful when classes share a parent, but it's useless otherwise. Interfaces are the solution! Though python doesn't have them technically, they can be
    #simulated with Abstract Base Classes. It'll define a set of methods but not actually do much of anything alone.
    class Weather:
        def weather_on(self):
            #ONLY CHILDREN TO BE MADE FROM THIS CLASS
            raise NotImplementedError
    
    class Sunny(Weather):
        def weather_on(self):
            print("The sun beams down, how lovely!")

    class Windy(Weather):
        def weather_on(self):
            print("Blustering winds blow by, hold your hat!")
    
    class Stormy(Weather):
        def weather_on(self):
            print("Crackling lightning crashes overhead, get inside!")
    
    day1 = Sunny()
    day2 = Windy()
    day3 = Stormy()

    days = [day1,day2,day3]
    for day in days:
        day.weather_on()
    #This is one way to access polymorphism. By creating a core class that can connect a variety of unrelated classes, we can ensure that certain properties are available regardless.
    # A powerful alternative to this is ducktyping, where regardless of whether a common ancestor is there or not, so long as objects share the methods called upon, we don't need a common ancestor. 

    #Duck Typing
    class Reuben:
        def eat(self):
            print("You eat the Reuben Sandwich")

    class BlackForestHam:
        def eat(self):
            print("You eat the Black Forest Ham Sandwich")
    sandwich1 = Reuben()
    sandwich2 = BlackForestHam()

    sandwiches = [sandwich1,sandwich2]
    for sandwich in sandwiches:
        sandwich.eat()
     
    return
if __name__ == "__main__":
    #Class/Instance example
    #class_instance_ex()

    #Private vs Public variable example!
    #pub_priv()
    
    #Inheritance Example!
    #inheritance()
    
    #Multiple Inheritance Example:
    #multiple_inheritance()

    #Polymorphism!
    #polymorphism()

    #interface/duck type!
    interfaces_and_ducktyping()