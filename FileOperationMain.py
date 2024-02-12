from FileOperation import FileOperation

def main():
    # יצירת אובייקט מסוג FileOperation
    file_operation = FileOperation()

    # קריאת נתונים מקובץ אקסל
    file_path = r'C:\Users\User\Desktop\python\YafeNof.csv'
    data = file_operation.read_excel(file_path)

    # שמירת הנתונים לקובץ אקסל חדש
    new_file_path = r'C:\Users\User\Desktop\python'
    file_operation.save_to_excel(data, new_file_path)

if __name__ == "__main__":
    main()
