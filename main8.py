from Task8 import  Task8

def Main8():
    task8 = Task8()
    task8.check_file_exists('additional_directory')
    task8.read_usernames_to_generator(r'C:\Users\User\Desktop\python\UsersName.txt')
    task8.read_usernames_to_list(r'C:\Users\User\Desktop\python\UsersName.txt', 10)
    task8.create_advanced_array(task8.read_usernames_to_list(r'C:\Users\User\Desktop\python\UsersName.txt',100))
    task8.create_advanced_array2(task8.read_usernames_to_list(r'C:\Users\User\Desktop\python\UsersName.txt',100))
    task8.check_emails_validity(r'C:\Users\User\Desktop\python\UsersEmail.txt')
    task8.filter_gmail_addresses(r'C:\Users\User\Desktop\python\UsersEmail.txt')
    task8.process_user_names_and_emails(r'C:\Users\User\Desktop\python\UsersName.txt', r'C:\Users\User\Desktop\python\UsersEmail.txt')
    task8.validate_user(r'C:\Users\User\Desktop\python\UsersName.txt')
    task8.count_letter_occurrences(r'C:\Users\User\Desktop\python\UsersName.txt')
    task8.calculate_payment_for_groups([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

if __name__ == "__main__":
     Main8()