import numpy as np
import pandas as pd
import seaborn as sns

class SalesData:
    def __init__(self, dataset):
        self.dataset = dataset

    def eliminate_duplicates(self):
        self.dataset.drop_duplicates(inplace=True)
        self.dataset.dropna(inplace=True)

    def calculate_total_sales(self):
        total_sales = self.dataset.groupby('product')['sales'].sum()
        return total_sales

    def _calculate_total_sales_per_month(self):
        self.dataset['month'] = self.dataset['date'].dt.month
        total_sales_per_month = self.dataset.groupby('month')['sales'].sum()
        return total_sales_per_month

    def _identify_best_selling_product(self):
        best_selling_product = self.dataset.groupby('product')['sales'].sum().idxmax()
        return best_selling_product

    def _identify_month_with_highest_sales(self):
        month_with_highest_sales = self.dataset.groupby('month')['sales'].sum().idxmax()
        return month_with_highest_sales

    def analyze_sales_data(self):
        best_selling_product = self._identify_best_selling_product()
        month_with_highest_sales = self._identify_month_with_highest_sales()
        analysis_result = {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales
        }
        return analysis_result

    def add_additional_values(self, analysis_result):
        min_sales_product = self.dataset.groupby('product')['sales'].sum().idxmin()
        average_sales = self.dataset['sales'].mean()
        analysis_result['min_sales_product'] = min_sales_product
        analysis_result['average_sales'] = average_sales
        return analysis_result


    def calculate_cumulative_sales(self):
        self.dataset['cumulative_sales'] = self.dataset.groupby('product')['sales'].cumsum()

    def add_90_percent_values_column(self):
        self.dataset['90_percent_values'] = self.dataset['discount'].apply(lambda x: x * 0.9)

    def bar_chart_category_sum(self):
        sns.barplot(x='product', y='quantity', data=self.dataset.groupby('product')['quantity'].sum().reset_index())

    def calculate_mean_quantity(self):
        mean = np.mean(self.dataset['Total'])
        median = np.median(self.dataset['Total'])
        second_max = np.partition(self.dataset['Total'], -2)[-2]

        return mean, median, second_max

    def filter_by_sellings_or_and(self):
        filtered_data = self.dataset[(self.dataset['selling'] > 5) | (self.dataset['selling'] == 0)]
        filtered_data = filtered_data[(filtered_data['price'] > 300) & (filtered_data['selling'] < 2)]

        return filtered_data

    def divide_by_2(self):
        self.dataset['BlackFridayPrice'] = self.dataset['BlackFridayPrice'] / 2

    def calculate_stats(self, columns=None):
        if columns is None:
            columns = self.dataset.columns

        stats = {}
        for column in columns:
            stats[column] = {
                'max': np.max(self.dataset[column]),
                'sum': np.sum(self.dataset[column]),
                'absolute_values': np.abs(self.dataset[column]),
                'cumulative_max': np.maximum.accumulate(self.dataset[column])
            }

        return stats