import unittest
#COMPLETED BY MARGARITA BUSYGINA
import db_connector


class MyTestCase(unittest.TestCase):
#This unit test checks if read_data() function returns an empty string after deleting all the rows(using delete_all() )
    def test_delete(self):
        db_connector.delete_all()
        self.assertTrue( not db_connector.read_data())


if __name__ == '__main__':
    unittest.main()
