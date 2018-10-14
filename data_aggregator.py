from Requests import MakeRequest
import threading

# Set API URl end points
mb_url = "https://www.mbusa.com/mercedes/json/cpo/inventory/vehicles/search?model=E350W4&count=4&start=0&sortBy=distance&zip=07675&distance=50&minYear=2016&maxYear=2018&minPrice=3000&maxPrice=38000&minMileage=0&maxMileage=10000&callSeq=1&_=1538969508535"
updated_mb_url = "https://www.mbusa.com/mercedes/json/cpo/inventory/vehicles/search?model=E350W4&count=4&start=0&sortBy=distance&zip=07675&distance=25&minYear=2016&maxYear=2018&minPrice=3000&maxPrice=38000&minMileage=0&maxMileage=11000&callSeq=1&_=1539534577948"
mb_c_class_url = "https://www.mbusa.com/mercedes/json/cpo/inventory/vehicles/search?model=C300W4&count=4&start=0&sortBy=distance&zip=07675&distance=25&minYear=2016&maxYear=2018&minPrice=3000&maxPrice=35000&minMileage=0&maxMileage=10000&callSeq=1&_=1539533873654"
lexus_url = "https://www.lexus.com/rest/inventorySearch?year=2016,2017&model=ES&minMileage=0&maxMileage=10000&minPrice=0&maxPrice=38000&zip=07675&sort=l&radius=25&limit=12&offset=0"


# Instances of Make Request Class
first_request = MakeRequest(updated_mb_url, mb_c_class_url, lexus_url)


def setInterval(func, time):
    """
    :param func: callback function
    :param time: set amount of seconds
    :return: Function Call
    """
    e = threading.Event()

    while not e.wait(time):
        func()


def make_library_request():
    """
    Creates Table and Outputs Table
    :return: None
    """
    first_request.output_table()
    return None


if __name__ == "__main__":
    make_library_request()
