import unittest
from student import Student

class MyTestClass(unittest.TestCase):
    """"
    Class of test cases running on unittest.TestCase
    """
    def test_student_moved(self):
        """
        This test unit tests if the 
        student_moved method properly 
        returns the country passed as new_country
         """
        my_instance = Student()
        new_country = 'USA'
        result = my_instance.student_moved(new_country)
        
        self.assertEqual(result, new_country)

if __name__ == '__main__':
    unittest.main()