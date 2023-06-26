#How does this solution ensure data immutability?
#Is this solution a pure function? why or why not?
#Is this solution a higher order function? Why or why not?
#Would it have been easier to solve this problem using a different programming style?
#Why in particular is functional programming a helpful paradigm when solving this problem?

#Parent class +++++++
class Podracer:
    def __init__(self, speed, state , cost) -> None:
        self.max_speed =  speed
        self.condition = state
        #states are perfect, trashed, and repaired
        self.price = cost

    def repair(self):
        self.condition = "repaired"

#

#Childrens class ++++++
class AnakinsPod(Podracer):
    def __init__(self, speed, state, cost) -> None:
        super().__init__(speed, state, cost)

    def boost(self):
        self.max_speed *= 2

class SebulbasPos(Podracer):
    def __init__(self, speed, state, cost) -> None:
        super().__init__(speed, state, cost)

    def flame_jet(self, obj_a ):
        obj_a.condition= "Trashed"


Anikin = AnakinsPod(50,"Perfect", 20)
Sebulba = SebulbasPos(48, "Perfect", 22)

Sebulba.flame_jet(Anikin)

print(Anikin.condition)

Anikin.repair()

print(Anikin.condition)

#===== Final Questions ====
# How does this solution demonstrate the four pillars of OOP?
#   In terms of the four pillars of OOP Encapsulation, Abstraction, Inheritance, Polymorphism.
#   The first ecapsulation is simple having a class that contains the key info into what makes a podracer.
#   The second Abstraction is simple that the classes contain function that could easly be accessed to change the conditions of the object
#   The third Inheritance is shown by the children class that contains the original info of the parent as well as adition attributes.
#   Lastly Polymorphism the children with different attributes changes the object while still containing key elements to make them unique.

# Would it have been easier to implement a solution to this problem using a different coding style? why or why not?
#   It would have been easier to have a Dictionarie to be able to change such few attribues. 
#   The issue would have harder if more podracer would have been added.

# How in particular did Object Oriented Programming assist in the solving of this problem?
#   Having a base class that one build from made things much easier. Having function that could easily change attributes of self makes it much
#   easier for the programer to keep track of each class atribute.