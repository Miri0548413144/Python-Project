import sys
import random
import datetime
class Task7:
    def handle_errors(self, exception_type):
        try:
            raise exception_type("This is a custom error")
        except Exception as e:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"<Tami&Miri, {current_time}>{e}<Tami&Miri>"
            print(error_message)

    def read_additional_files(self):
        try:
            with open('additional_file.csv', 'r') as file:
                csv_content = file.read()
                print("Read CSV content:", csv_content)
            with open('additional_file.docx', 'r') as file:
                word_content = file.read()
                print("Read Word content:", word_content)

        except FileNotFoundError:
            print("File not found!")

    def generate_random_sales_data(self, product):
        random_sales = random.randint(1, 100)
        random_amount = random.uniform(10.0, 1000.0)
        print(f"Product: {product}, Random Sales: {random_sales}, Random Amount: {random_amount}")

    def print_python_version(self):
        print(f"Python Version: {sys.version}")

    def process_parameters(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, int):
                print(f"Value: {arg}")
            elif isinstance(arg, str):
                print(f"Value: {arg}")
            else:
                print("Unknown type")

        for key, value in kwargs.items():
            print(f"{key}: {value}")

    def print_table_info(self,sales_data):
        sales_data.print_table_head()
        sales_data.print_table_tail(2)
        sales_data.print_random_row()

    def iterate_table_elements(self,sales_data):
        numeric_values = sales_data.get_numeric_values()
        for value in numeric_values:
            print(value)
