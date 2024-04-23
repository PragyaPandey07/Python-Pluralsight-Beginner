#Parent class
class Robot:
    def __init__(self, name) :
        self.name = name
        self.position = [0,0]
        print("My name is", self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("My new position is", self.position)

    def eat(self) :
        print("I am hungry !!")

#Child class
class Robot_Dog(Robot) :
    #child class can also have __init__ method, if not then the __init__ method of the parent class is considered

    def make_noise(self):
        print("Woof Woof!!")

    def eat(self) :
        super().eat() #use super() keyword to call overloaded method in the parent class
        print("Feed me !!")

my_robot_dog = Robot_Dog('Buddy')
my_robot_dog.walk(10)
my_robot_dog.make_noise()

#method eat() is overloaded in parent class
my_robot_dog.eat() 