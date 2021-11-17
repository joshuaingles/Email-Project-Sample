import csv

class csv_parser:
    def __init__(self, filePath):
        self.filePath = filePath
        self.fields = []
        self.bodies = []

    def get_bodies(self):
        fields = []
        rows = []

        with open(self.filePath, 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)

            self.fields = next(csvreader)

            for row in csvreader:
                self.bodies.append(row[4])

        return self.bodies
