import requests
from prettytable import PrettyTable
import json


class MakeRequest(object):

    def __init__(self, mb_url, mb_c_class_url, lexus_url):
        self.mb_api = mb_url
        self.mb_c_api = mb_c_class_url
        self.lexus_api = lexus_url
        self.table = PrettyTable()

        # Original data strings if pleased
        self.mb_string_data = ""
        self.lexus_string_data = ""

    def get_mb_data(self):
        """
        Reaches out to the Mercedes Benz API for desired search query
        :return: data
        """
        response = requests.get(self.mb_api)
        data = response.text
        self.mb_string_data += data
        return data

    def get_mb_c_class_data(self):
        """
        Reaches out to the Mercedes Benz API for desired search query
        :return: data
        """
        response = requests.get(self.mb_c_api)
        data = response.text
        self.mb_string_data += data
        return data

    def get_lexus_data(self):
        """
        Reaches out to the Lexus API for desired search query
        :return: data
        """
        response = requests.get(self.lexus_api)
        data = response.text
        self.lexus_string_data += data
        return data

    def __create_table(self):
        self.table.field_names = [
            "Brand",
            "Model",
            "Year",
            "Mileage",
            "price",
            "Vin Number",
            "Exterior Color",
            "Interior Color",
            "Dealer City",
            "Dealer State",
            "Dealer Zip Code",
            "Dealer Phone Number",
            "Inventory URL"
        ]

        mb_parsed_data = json.loads(self.get_mb_data())['models']
        mb_c_parsed_data = json.loads(self.get_mb_c_class_data())['models']
        lexus_parsed_data = json.loads(self.get_lexus_data())['data']['docs']

        for car in mb_parsed_data:
            self.table.add_row([
                "Mercedes Benz",
                car['vehicles']['records'][0]['modelName'],
                car['vehicles']['records'][0]['year'],
                car['vehicles']['records'][0]['mileage'],
                car['vehicles']['records'][0]['dsrp'],
                car['vehicles']['records'][0]['vin'],
                car['vehicles']['records'][0]['exteriorColorDesc'],
                car['vehicles']['records'][0]['interiorColorDesc'],
                car['vehicles']['records'][0]['dealer']['city'],
                car['vehicles']['records'][0]['dealer']['state'],
                car['vehicles']['records'][0]['dealer']['zip'],
                car['vehicles']['records'][0]['dealer']['phone'],
                car['vehicles']['records'][0]['dealer']['url'],
            ])

        for car in mb_c_parsed_data:
            self.table.add_row([
                "Mercedes Benz",
                car['vehicles']['records'][0]['modelName'],
                car['vehicles']['records'][0]['year'],
                car['vehicles']['records'][0]['mileage'],
                car['vehicles']['records'][0]['dsrp'],
                car['vehicles']['records'][0]['vin'],
                car['vehicles']['records'][0]['exteriorColorDesc'],
                car['vehicles']['records'][0]['interiorColorDesc'],
                car['vehicles']['records'][0]['dealer']['city'],
                car['vehicles']['records'][0]['dealer']['state'],
                car['vehicles']['records'][0]['dealer']['zip'],
                car['vehicles']['records'][0]['dealer']['phone'],
                car['vehicles']['records'][0]['dealer']['url'],
            ])

        for car in lexus_parsed_data:
            self.table.add_row([
                "Lexus",
                car['overview']['modelname'],
                car['overview']['year'],
                car['overview']['miles'],
                car['overview']['lotPrice'],
                car['overview']['vin'],
                car['color']['exteriorcolorname'],
                car['color']['interiorcolorname'],
                car['dealerInfo']['address']['city'],
                car['dealerInfo']['address']['state'],
                car['dealerInfo']['address']['zipCode'],
                car['dealerInfo']['phone'],
                car['inventoryData']['inventoryUrl']['vehicle'][0],
            ])

        print(self.table)

        return self.table

    def output_table(self):
        with open('auto_info.txt', 'w') as file:
            file.write(str(self.__create_table()))
            file.close()
