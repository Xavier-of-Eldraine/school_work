"""
Griffin Stover
11/17/24
CRN:
Class: CIS 216
Estimated Time:
"""


#Welcome to my super professional and awesome introduction to some basic OOP stuff!
# Here's the outline: 
"""
*Classes
*Private vs Public Variables
*Instance
*Inheritance
*Polymorphism   
*Multiple Inheritance
*Interfaces/Duck Typing
"""


#Let's begin with classes! 
    #A class is a user-defined blueprint for objects! A class can store variables, as well as methods(functions for a class). 
    #In order to use a class, you have to create an instance of it in the same way you'd think of calling on a function. 
    #Let's demonstrate these ideas with a bit of code!

def class_instant_ex():
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

    #With this demonstration we've gone over some of the utilities of classes! By counting sword swings across instances we can see
    #the total number of swings. We've also demonstrated how variables like sword type can be shared too! And with our egg class we
    #learned about arguments!

    #We've also learned a bit about instances! We learned how to call on it's methods with the swords by using
    # longsword/shortsword.swing(). With our eggs we learned about creating instances with arguments too, alongside default values that
    #we can use in case our user forgets to provide a value.

#Now onto Public and Private variables. 




if __name__ == "__main__":
    #Class example
    class_instant_ex()
