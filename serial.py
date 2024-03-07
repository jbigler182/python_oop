"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
        
    """


    def __init__(self, start = 0):
        """This function sets the start equal to the next number to be generated"""
        self.start = self.next = start

    def generate(self):
        """This function adds one to start number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """This function resets start number"""
        self.next = self.start

    def __repr__(self):
        return f"<SerialGenerator start=100 next=101>"
        















    # def __repr__(self):
    #     """Show representation."""
    #     return f"{self.start} will add one to itself each time it is generated"

    # def __init__(self, start=0):
    #     self.start = self.next = start

    # def generate(self):
    #     self.next = self.next + 1
    #     return self.next - 1

    # def reset(self):
    #     self.next = self.start
