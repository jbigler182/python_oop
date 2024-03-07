#V2
#Python Object Oriented Programming 
#dir(obj)

    #OO review 
        #Class - blueprint for new objects, defines attribues and methods. Used to make new instances of objects(dict)
        #Method - a function defined on class, can see change attributes on instanace
        #Class method - function defined on class, called on class, not individual instance
        #Basic EX str() is an example of a class. What we get back '' is an instance of the class

        # In [15]: str()
        # Out[15]: ''

# PRETTY MUCH EVERYTHING WE WORK WITH IN PYTHON IS AN INSTANCE OF SOME CLASS. 

#EX1
#Built in class (Counter is first example, has to be imported as seen below)

        # In [1]: from collections import Counter

        # In [2]: help(Counter)


        # In [3]: c = Counter('abcdeabcdabcada')

        # In [4]: c
        # Out[4]: Counter({'a': 5, 'b': 3, 'c': 3, 'd': 3, 'e': 1})

#How can I tell if something is a class?

        # In [7]: type(c)
        # Out[7]: collections.Counter
        # In [9]: isinstance(c, Counter)     #(isinstance is aboolean method)
        # Out[9]: True

    # We can see that c is in fact a instance of the Counter class
    # Counter is the blue print, when we encounter it we get back an instantiated class.

#THESE BUILT IN (IMPORTABLE) CLASSES HAVE METHODS THAT COME WITH THEM

    # In [10]: c.most_common()
    # Out[10]: [('a', 5), ('b', 3), ('c', 3), ('d', 3), ('e', 1)]
        #to call an attribute or method(as seen here) in python its simple. somevariable.the_method

#V3
#Defining classes in python

# instance methods directly below: Operate on a specific instance of Triangle

# from math import sqrt
# from random import randint

# class Triangle:                #self is a lot like this. It needs to be the first parameter in init.
#     def __init__(self, a, b):  #we have to manually place dunder init method in our new class. It's called for us in built in methods. This takes the place of the constructor seen in js
#         self.a = a
#         self.b = b

#     def get_hypotenuse(self):
#         return sqrt(self.a ** 2 + self.b ** 2)
    
#     def get_area(self):
#         return self.a * self.b / 2
    
    #How to run above class
        # In [59]: %run notes.py

        # In [60]: t.get_hypotenuse()
        # Out[60]: 5.0

        # In [61]: t.get_area()
        # Out[61]: 6.0


# Above class accepts two arguments (a, b) when we instanciate a new instance of Triangle. 

# class Triangle {
#     function constructor(a,b){
#         this.a = a;
#         this.b = b;
#     }
# }
    
#V4
#Class Methods - by far less common then instance methods. They are different then instance methods.
    # They are method of the class. The @classmethod references the class Triangle2

from math import sqrt
from random import randint


class Triangle:         
    """
    A class used to represent a right triangle

    Attributes
    ------------
    a: int
        length of side a
    b: int 
        length of side b
    """                       #This is the "constructor" of python
    def __init__(self, a, b): #Call a dunder method! Manually place dunder in out class. 
        self.a = a
        self.b = b


            #DUNDER METHODS
    
    #Using a dunder method to represent Triangle
        
    def __repr__(self):
        return f"Trianlge (a={self.a}, b={self.b})"      #for developers
    
    def __str__(self):
        return self.describe()   #for print
    
    #Test equality using a dunder method

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    


    
            #WE ARE CREATING A FUNCTION FACTORY FOR THIS CLASS. THIS FACTORY MAKES RANDOM TRIANGLES


    @classmethod #this will alter the behavior of the text that comes directly after it. 
    def random(cls): 
        """Class method which returns Triangle with random sides"""                                  #cls is just industry standard
        # print(cls)
        return cls(randint(1, 100), randint(1, 100))   #NOTICE NO self needed because it is referencing the class
                    #How to access/how this class works
                        # In [194]: t = Triangle.random()
                        # In [195]: t.a
                        # Out[195]: 91
                        # In [196]: t.b
                        # Out[196]: 22

    def get_hypotenuse(self):
        """Calculates hypotenuse (3rd side of right triangle)"""
        return sqrt(self.a ** 2 + self.b ** 2)
        
    def get_area(self):
        """Calculates area of right triangle"""
        return self.a * self.b / 2
    
    def describe(self):
        """Returns string representing triangle"""
        return f"I am a triangle with sides: {self.a} and {self.b}."
    
        #When I ran the above code

            # In [83]: %run notes.py

            # In [84]: TT = Triangle2.random()

            # In [85]: TT
            # Out[85]: <__main__.Triangle2 at 0x7eff042d8d90>

            # In [86]: TT.a
            # Out[86]: 64

            # In [87]: TT.b
            # Out[87]: 21

            # In [88]: TT.get_hypotenuse()
            # Out[88]: 67.35725647619564

            # In [89]: TT.get_area()
            # Out[89]: 672.0

#V5 Inheritance - can have more then one parent but not super common
        #SEE colored_triangle.py tab (Need to come back and figure out why 'super' object has no attribute' I KNWO IM TRYIN TO CALL A METHOD!)
    
#V6 Class_docstrings - See above method for examples
    #It is a standard to add attribute to docstring
    #Need to properly document method

#V7 Special Methods or (DUNDER METHODS) aka double underscore
        #Can add a method called __repr__ (a dunder) SEE ABOVE

