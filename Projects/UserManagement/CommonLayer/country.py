import pandas


class CountrySelection:
    def __init__(self):
        self.file_name = "country-list.csv"

    def get_all_country(self):
        country_list = []

        data = pandas.read_csv(self.file_name)

        for item in data["country"]:
            country_list.append(item)

        return country_list
