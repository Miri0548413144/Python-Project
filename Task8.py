import os
import re
from AdvancedArray import  AdvancedArray

class Task8:
    def check_file_exists(self, file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            print(f"Directory created: {file_path}")

    def read_usernames_to_generator(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()

    def read_usernames_to_list(self, file_path, percentage):
        with open(file_path, 'r') as file:
            usernames = [line.strip() for line in file.readlines() if len(line.strip()) > 0]

        total_users = len(usernames)
        selected_users_count = int(total_users * percentage / 100)
        selected_users = usernames[:selected_users_count]
        return selected_users

    def create_advanced_array(self, data):
        advanced_array = AdvancedArray(data)
        return advanced_array.get_advanced_data()
    def create_advanced_array2(self, data):
        advanced_array = AdvancedArray(data)
        return advanced_array.get_advanced_data2()

    def check_emails_validity(self, email_file):
        with open(email_file, 'r') as file:
            email_addresses = [line.strip() for line in file.readlines()]

        valid_emails = [email for email in email_addresses if re.match(r"[^@]+@[^@]+\.[^@]+", email)]
        print("Valid Emails:", valid_emails)

    def filter_gmail_addresses(self, email_file):
        with open(email_file, 'r') as file:
            email_addresses = [line.strip() for line in file.readlines()]
        gmail_addresses = [email for email in email_addresses if email.endswith('@gmail.com')]
        print("Gmail Addresses:", gmail_addresses)

    def process_user_names_and_emails(self, names_file, emails_file):
        with open(names_file, 'r') as names_file:
            names = [line.strip() for line in names_file.readlines()]

        with open(emails_file, 'r') as emails_file:
            email_addresses = [line.strip() for line in emails_file.readlines()]

        for name, email in zip(names, email_addresses):
            print(f"Name: {name}, Email: {email}")

    def validate_user(self,path):
        with open(path, 'r') as names_file:
            users_list = [line.strip() for line in names_file.readlines()]

        user_name = input("נא להזין את שמך: ")
        if user_name in users_list:
            print("המשתמש קיים ברשימה.")
        else:
            print("המשתמש לא קיים ברשימה.")

        user_name_as_number = [ord(char) for char in user_name]
        ''.join([chr(num) for num in user_name_as_number])
        count_of_letter_a = user_name.count('A')
        print(f"מספר האותיות 'A' בשם: {count_of_letter_a}")





    def count_letter_occurrences(self, names_file):
        with open(names_file, 'r') as file:
            names = [line.strip() for line in file.readlines()]

        valid_names = [name for name in names if name[0].isupper()]
        print(f"שמות המשתמשים עם אותיות רישיות גדולות: {valid_names}")

    def calculate_payment_for_groups(self, user_list):
        payments = []
        for i, user in enumerate(user_list):
            if (i + 1) % 8 == 0:
                payment = 200
                if (i + 1) % 88 != 0:
                    payment += 50
                payments.append(payment)

        total_payment = sum(payments)
        print("Total Payment for Groups:", total_payment)