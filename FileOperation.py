
import pandas as pd

class FileOperation:
    def read_excel(self, file_path: str):
        data = pd.read_csv(file_path)
        return data

    def save_to_excel(self, data, file_name: str):
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)

