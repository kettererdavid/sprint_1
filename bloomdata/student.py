
import random

class Student:
    """"
    This class produces students with attributes name, age, 
    sex, country and IQ with the given defaults.]
    """
    def __init__(self, name='John', age='23', sex='M', country='GER', IQ='100'):
       self.name = name
       self.age = age
       self.sex= sex
       self.country = country
       self.IQ = IQ


    def student_moved(self, new_country):
        """
        Assigns the country passed as new_country
        as the new value of country"""
        self.country = new_country
        return self.country

    def passed_class(self, class_difficulty):
        """
        Increases a students IQ by the value class_difficulty, 
        once the student has passed the class"""
        self.IQ += class_difficulty

class BloomTechStudent(Student):
    """
    Child class of Student, with a new attribute performance
    """
    def __init__(self, name, age, sex, country, IQ, performance):
        super().__init__(name, age, sex, country, IQ)
        self.performance = performance

    def summary(self):
        """
        Prints f string that contains name, performance, IQ and age. 
        """
        print(f"Student {self.name} performs {self.performance}, with an IQ of {self.IQ} at an age of {self.age}.")
    
    def student_generator(self):
        """
        Generates 30 students with attributes chosen randomly''
        from the lists below.
        """
        
        names = ['Walter', 'Sieglinde', 'Edeltraud', 'Jambo']
        sexes = ['male', 'female', 'clownself']
        countries = ['Zimbabwe', 'Hungary', 'USA']
        performances = ['low', 'medium', 'high']
        students = []

        for _ in range (30):
            name = random.choice(names)
            sex = random.choice(sexes)
            country = random.choice(countries)
            performance = random.choice(performances)
            age = random.randint(17, 97)
            IQ = random.randint(83, 134)

            student = BloomTechStudent(name, age, sex, country, IQ, performance)
            students.append(student)
        print(students)

