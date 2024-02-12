class AdvancedArray:
    def __init__(self, data):
        self.data = data

    def get_advanced_data(self):
        total_users = len(self.data)
        first_10_percent = self.data[:int(0.1 * total_users)]
        return first_10_percent

    def get_advanced_data2(self):
        even_rows_users = self.data[1::2]
        return even_rows_users