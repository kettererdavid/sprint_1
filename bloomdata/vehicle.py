class Vehicle:
    """
    Class of Vehicles with certain attributes and methods
    """
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self): 
        """
        Honks
        """
        return ' Hooooonk'
    
    def drive(self, miles_driven):
        """
        Adds miles_driven to self.mileage and returns the sum 
        as new value of self.mileage
        """
        self.mileage+= miles_driven
        return self.mileage

    def __repr__(self):
        """
        Returns a f string containing make, model, color and year
        """
        return f'A {self.make} {self.model}in the color {self.color} built in {self.year} with a mileage of{self.mileage}.'

class Convertible:
    """
    Practice class that vould technically inherit from Vehicle class, 
    but doesnt, to show how much more work it is
    """
    def __init__(self, make, model, color, year, mileage, top_down=True):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        self.top_down = top_down

    def honk(self): 
        """
        Honks
        """
        return ' Hooooonk'
    
    def drive(self, miles_driven):
        """
        Adds miles_driven to self.mileage and returns the sum 
        as new value of self.mileage
        """
        self.mileage+= miles_driven
        return self.mileage

    def change_top_status(self):
        """
        Changes status of top. If top is up, gets put down.
        If top is down, gets put up. Also prints status of top after 
        done changing status
        """
        if self.top_down:
            self.top_down = False
            return 'Top is now up'
        else:
            self.top_down = True
            return 'Top is now down'

    def __repr__(self):
        return f'A {self.make} {self.model}in the color {self.color} built in {self.year} with a mileage of{self.mileage}.'
    