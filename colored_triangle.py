from notes import Triangle

class ColoredTriangle(Triangle):   #have to pass parent as argument in child/ can have multiple parents in here (can't do that shit in js)

    def __init__(self, a, b, color):
        super().__init__(a, b)         #super().__init__ is how we call the parent elements attributes 
        self.color = color

    def describe(self):
        # return f"I am a triangle with sides: {self.a} and {self.b}. I am {self.color}" #Can have own function
        msg = super().describe()  #IDK WHY BUT THIS WON'T WORK RETURNS THAT 'super' object has no attribute describe(), but it does?                                                    #Or can reference parent function and add on to it
        return msg + f" I am {self.color}."