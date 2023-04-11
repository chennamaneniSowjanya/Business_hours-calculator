import unittest
from business_hours import business_hours

class TestBusinessHours(unittest.TestCase):

    #test whether exception is thrown when invalid parametrs are passed to the function
    def test_inavalid_input(self):
        self.assertEqual(business_hours('2034-21-34', 2), 'invalid inputs for date parameter')

    #test to check number of business hours returned by the function on weekend with same start datetime and end datetime
    def test_weekend_sameday(self):
        self.assertEqual(business_hours('2023-02-18 09:00:00','2023-02-18 09:00:00' ), 0)
    
    #test to check number of business hours returned by the function on weekend with same start date and end date but with different start time and end time
    def test_weekend_sameday(self):
        self.assertEqual(business_hours('2023-02-18 09:00:00','2023-02-18 13:00:00' ), 0)
    
    #test to check number of business hours returned by the function on consecutive weekends with same time
    def test_weekend_sameday(self):
        self.assertEqual(business_hours('2023-02-18 09:00:00','2023-02-19 09:00:00' ), 0)
    
    #test to check number of business hours returned by the function on consecutive weekends with different time
    def test_weekend_sameday(self):
        self.assertEqual(business_hours('2023-02-18 09:00:00','2023-02-19 13:00:00' ), 0)

    #test to check the functionality of code if start datetime is after end datetime
    def test_date_order(self):
        self.assertEqual(business_hours('2024-02-19 09:00:00','2023-02-19 09:00:00'), 'start datetime should be before than end datetime')

        

    #test to check the number of business hours on a workingday with same start date and end date
    def test_one_working_day(self):
        self.assertEqual(business_hours('2023-02-18 09:00:00','2023-02-20 18:00:00') , 8)
        self.assertEqual(business_hours('2023-02-18 15:00:00','2023-02-20 15:00:00') , 6)
        self.assertEqual(business_hours('2023-02-18 15:00:00','2023-02-20 09:00:00') , 0)

        self.assertEqual(business_hours('2023-02-20 09:00:00','2023-02-20 09:00:00') , 0)
        self.assertEqual(business_hours('2023-02-20 09:00:00','2023-02-20 18:00:00'), 8)
        self.assertEqual(business_hours('2023-02-20 19:00:00','2023-02-20 20:00:00'), 0)
        self.assertEqual(business_hours('2023-02-20 08:00:00','2023-02-20 15:00:00'), 6)
        self.assertEqual(business_hours('2023-02-20 07:00:00','2023-02-20 18:00:00'), 8)
        self.assertEqual(business_hours('2023-02-20 09:00:00','2023-02-20 09:30:00'), 0)
        self.assertEqual(business_hours('2023-02-20 08:00:00','2023-02-20 09:30:00'), 0)
        
        self.assertEqual(business_hours('2023-02-17 08:00:00','2023-02-19 09:30:00'), 8)
        self.assertEqual(business_hours('2023-02-17 14:00:00','2023-02-19 19:30:00'), 3)
        self.assertEqual(business_hours('2023-02-17 18:00:00','2023-02-19 09:30:00'), 0)
        self.assertEqual(business_hours('2023-02-17 09:00:00','2023-02-19 09:30:00'), 8)

        self.assertEqual(business_hours('2023-02-20 18:00:00','2023-02-20 09:00:00'), 'start datetime should be before than end datetime')


    #tests to chek the business hours between any two dates with more than one working day in between them
    def test_nonweekend(self):
        self.assertEqual(business_hours('2023-02-05 09:00:00','2023-02-12 18:00:00') , 40)
        self.assertEqual(business_hours('2023-02-05 08:00:00','2023-02-12 16:00:00') , 40)
        self.assertEqual(business_hours('2023-02-05 19:00:00','2023-02-12 18:00:00') , 40)
        self.assertEqual(business_hours('2023-02-05 19:00:00','2023-02-12 09:00:00') , 40)
        self.assertEqual(business_hours('2023-02-05 19:00:00','2023-02-12 08:00:00') , 40)
        self.assertEqual(business_hours('2023-02-05 19:00:00','2023-02-12 12:00:00') , 40)
        self.assertEqual(business_hours('2023-02-20 18:00:00','2023-02-20 09:00:00'), 'start datetime should be before than end datetime')

        self.assertEqual(business_hours('2023-02-09 09:00:00','2023-02-16 18:00:00') , 48)
        self.assertEqual(business_hours('2023-02-09 08:00:00','2023-02-16 16:00:00') , 47)
        self.assertEqual(business_hours('2023-02-09 19:00:00','2023-02-16 18:00:00') , 40)
        self.assertEqual(business_hours('2023-02-09 19:00:00','2023-02-16 09:00:00') , 32)
        self.assertEqual(business_hours('2023-02-09 19:00:00','2023-02-16 08:00:00') , 32)
        self.assertEqual(business_hours('2023-02-09 19:00:00','2023-02-16 12:00:00') , 35)
        self.assertEqual(business_hours('2024-02-09 18:00:00','2023-02-16 09:00:00'), 'start datetime should be before than end datetime')
    
    #test to check the results on base testcases as given in the task
    def test_basecases(self):
        self.assertEqual(business_hours('2019-12-02 08:00:00','2019-12-04 12:15:00') , 19)
        self.assertEqual(business_hours('2019-12-01 09:30:00','2019-12-07 12:15:00') , 40)




if __name__ == '__main__':
    unittest.main()
