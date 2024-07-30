import csv
import os


class ReadCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        with open(self.csv_file, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            data = list(reader)
            return data


class WriteCSV:
    def __init__(self, csv_file, header, csvData):
        self.csv_file = csv_file
        self.header = header
        self.csvData = csvData

    def write_csv(self):
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
            print("The file has been deleted.")
        else:
            print("The file does not exist.")
        with open(self.csv_file, "w", encoding="UTF8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.header)
            writer.writerows(self.csvData)
            print(str(csvfile) + " created.")
            return
