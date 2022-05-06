import openpyxl

import unittest
  
wb = openpyxl.load_workbook(filename="books.xlsx")
sheet = wb.active
rows = sheet.max_row

# test if any cells are empty
class TestMethods(unittest.TestCase):
    # test function 
    def testcells1(self):
        for i in range(2,rows+1):
            author = sheet['A'+str(i)].value
        # error message in case if test case got failed
            message = "Author not specified"
        # assertIsNotNone() to check that if input value is not none
            self.assertIsNotNone(author, message)
    def testcells2(self):
        for i in range(2,rows+1):
            title = sheet['B'+str(i)].value
        # error message in case if test case got failed
            message = "Title not specified"
        # assertIsNotNone() to check that if input value is not none
            self.assertIsNotNone(title, message)
  
if __name__ == '__main__':
    unittest.main()