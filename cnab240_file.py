from cnab240.v10_7 import models

class CNAB240_File():
    def __init__(self, initial_data):
        self.header = models.HeaderLine(initial_data["header"])

    def generate_file(self):
        print(self.header.formatted_data())



if __name__ == "__main__":
    import data_handler
    spreadsheet_data = data_handler.get_spreadsheet_data()
    fields_initial_data = data_handler.get_initial_data(spreadsheet_data)

    cnab = CNAB240_File(fields_initial_data)
    cnab.generate_file()