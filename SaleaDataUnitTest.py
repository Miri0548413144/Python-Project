import unittest
import pandas as pd
from SalesData import SalesData

class TestSalesData(unittest.TestCase):

    def test_calculate_total_sales(self):
        # יצירת DataFrame לצורך הטסט
        data = {'Product': ['A', 'B', 'A', 'B'],
                'Quantity': [5, 10, 3, 8]}
        df = pd.DataFrame(data)

        # יצירת אובייקט מסוג SalesData עם DataFrame המייצג את הנתונים
        sales_data_object = SalesData(df)

        # קריאה לפונקציה שאנו רוצים לבדוק
        result = sales_data_object.calculate_total_sales()

        # בדיקה שהתוצאה תואמת לערך הצפוי
        self.assertEqual(result['A'], 8)
        self.assertEqual(result['B'], 18)


if __name__ == '__main__':
    unittest.main()