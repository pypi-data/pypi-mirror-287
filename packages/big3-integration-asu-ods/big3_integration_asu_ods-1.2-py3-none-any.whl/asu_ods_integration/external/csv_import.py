
import csv


class CSVImport:

    def __init__(self, fn):
        self.fn = fn

    def __iter__(self):
        with open(self.fn, newline='') as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                yield row

