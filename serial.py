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
    def __init__(self,start = 0):
        self.start = start
        self.count = start

    def __repr__(self):
        return f'I am currently at {self.count}'

    def generate(self):
        self.count = self.count + 1
        return self.count - 1

    def reset(self):
        self.count = self.start