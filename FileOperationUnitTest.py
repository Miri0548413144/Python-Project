import unittest
import pandas as pd
from FileOperation import FileOperation

class TestFileOperation(unittest.TestCase):

    def setUp(self):
        self.file_operation = FileOperation()

    def test_read_excel(self):
        file_path = 'your_file_path.xlsx'
        data = self.file_operation.read_excel(file_path)
        self.assertIsInstance(data, pd.DataFrame, "The output should be a pandas DataFrame")

    def test_save_to_excel(self):
        data = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
        file_name = 'test_output.xlsx'
        self.file_operation.save_to_excel(data, file_name)
        loaded_data = pd.read_excel(file_name)
        self.assertTrue(data.equals(loaded_data), "Saved and loaded DataFrames should be equal")

if __name__ == '__main__':
    unittest.main()
