import pandas as pd
from SalesData import SalesData


def main():
    dataset_path = r'C:\Users\User\Desktop\python\YafeNof.csv'
    dataset = pd.read_csv(dataset_path)
    sales_data_object = SalesData(dataset)
    sales_data_object.eliminate_duplicates()
    sales_data_object.calculate_cumulative_sales()
    sales_data_object.add_90_percent_values_column()

    # הרצת פעולות ופונקציות ישירות מהאובייקט
    total_sales = sales_data_object.calculate_total_sales()
    print("Total Sales:")
    print(total_sales)

    # הרצת פעולת הצגת גרף
    sales_data_object.bar_chart_category_sum()



if __name__ == "__main__":
    main()
