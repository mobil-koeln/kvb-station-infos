import csv


class TestCSVParsing:

    def test_csv_parsing(self):

        with open('stations.csv', newline='') as csvfile:
            stations = csv.DictReader(csvfile)
            for station in stations:
                assert station["name"] != None, f"Name is None in {station}"
                assert station["infolink"] != None, f"Info link is None in {station}"
