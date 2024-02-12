import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from SalesData import SalesData
from Task7 import Task7

def main():
    dataset_path = r'C:\Users\User\Desktop\python\YafeNof.csv'
    dataset = pd.read_csv(dataset_path)
    sales_data_object = SalesData(dataset)
    sales_data_object.eliminate_duplicates()
    sales_data_object.calculate_cumulative_sales()
    sales_data_object.add_90_percent_values_column()
    total_sales = sales_data_object.calculate_total_sales()
    matplotlib_sales = SalesData(dataset)

    # דיאגרמת קווים עם קווים מקווקווים
    plt.plot(dataset['Product'], dataset['Total'], marker='o', linestyle='--', color='green')
    plt.title('Line Plot of Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')  # לסובל משמאל
    plt.tight_layout()
    plt.show()

    # שרטוט 2: שרטוט מקומות (Bar Plot)
    plt.figure(figsize=(12, 6))
    sales_data_object.bar_chart_category_sum()
    plt.title('Bar Chart - Category Sum')
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.show()
#
    # שרטוט 3: שרטוט פיזור (Scatter Plot)
    plt.figure(figsize=(10, 6))
    plt.scatter(dataset.index, dataset['cumulative_sales'])
    plt.title('Scatter Plot - Cumulative Sales over Time')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sales')
    plt.show()
#
    # שרטוט 4: שרטוט פאי (Pie Chart)
    plt.figure(figsize=(8, 8))
    total_sales = matplotlib_sales.calculate_total_sales()
    plt.pie(total_sales.values, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart - Total Sales Distribution')
    plt.show()
#
    # שרטוט 5: שרטוט קוביה (3D Plot)
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(dataset.index, dataset['Total'], dataset['cumulative_sales'])
    ax.set_xlabel('Index')
    ax.set_ylabel('Total')
    ax.set_zlabel('Cumulative Sales')
    ax.set_title('3D Scatter Plot - Total and Cumulative Sales')
    plt.show()
#
    # שרטוט 6: שרטוט בהשקפה לוגריתמית (Logarithmic Scale)
    plt.figure(figsize=(12, 6))
    for column in dataset.columns:
        plt.plot(dataset.index, np.maximum.accumulate(dataset[column]), label=column)
    plt.yscale('log')
    plt.title('Logarithmic Scale - Cumulative Max Values')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Max Values')
    plt.legend()
    plt.show()
#
    # שרטוט 7: שרטוט כמויות מתוך חישובים סטטיסטיים (Box Plot)
    plt.figure(figsize=(12, 6))
    box_data = [dataset['Total'], dataset['cumulative_sales']]
    plt.boxplot(box_data, labels=['Total', 'Cumulative Sales'])
    plt.title('Box Plot - Total and Cumulative Sales')
    plt.ylabel('Values')
    plt.show()

    seaborn_sales = SalesData(dataset)

    data = {'Product': ['Sidur', 'Teilim', 'Sidur', 'Chumash', 'Tanach'],
            'Price': [60, 400, 50, 300, 80],
            'Quantity': [3, 5, 10, 2, 20]}
    df = pd.DataFrame(data)
#
    # שרטוט פיז'בוקס
    sns.boxplot(x='Product', y='Price', data=df)
    plt.title('Boxplot of Price per Product')
    plt.show()
#
    # שרטוט דיסטריביות כמויות
    sns.histplot(df['Quantity'], kde=True)
    plt.title('Distribution of Quantity')
    plt.xlabel('Quantity')
    plt.show()
#
    # שרטוט קורולציה בין עמודות
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
#
#4#
    data = {'Category': ['A', 'A', 'B', 'B', 'A', 'C', 'C', 'C'],
            'Values': [20, 25, 30, 15, 18, 22, 28, 32]}
    df = pd.DataFrame(data)
    sns.boxplot(x='Category', y='Values', data=df, hue='Category')
    plt.title('Boxplot with Category Separation')
    plt.show()
#5
    data = {'Score': [75, 88, 92, 78, 84, 66, 90, 82, 79, 95]}
    df = pd.DataFrame(data)
    sns.histplot(df['Score'], bins=10, kde=True, color='skyblue')
    plt.title('Distribution of Scores')
    plt.xlabel('Score')
    plt.show()

    #תרגיל 7
    task7 = Task7()
    task7.handle_errors(ValueError)
    task7.read_additional_files()
    task7.generate_random_sales_data("ProductA")
    task7.print_python_version()
    task7.process_parameters(42, 'hello', name='John', age=25)
    task7.print_table_info(sales_data_object)
    task7.iterate_table_elements(sales_data_object)

if __name__ == "__main__":
    main()
