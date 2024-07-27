import requests
from time import sleep
    

class InternetStatus:

    def __init__(self, output_file_path, url="https://google.com", timeout=5, continous=False):
        self.__url = url
        self.__timeout = timeout
        self.__output_file_path = output_file_path
        self.__continous = continous
        self.__valid = True
        self.__work = True
        self.__validate()

    def __validate(self):
        if not self.__output_file_path:
            self.__valid = False
        if not isinstance(self.__timeout, int):
            self.__valid = False

    def __checker(self):
        try:
            response = requests.get(url=self.__url, timeout=self.__timeout)
            with open(self.__output_file_path, "w") as initiator_file:
                initiator_file.write("active" if response.status_code >= 200 and response.status_code <= 300 else "unactive")
        except:
            with open(self.__output_file_path, "w") as initiator_file:
                initiator_file.write("unactive")

    def quit(self):
        self.__work = False

    def checkStatus(self):
        if self.__valid:
            if self.__continous:
                while self.__work:
                    self.__checker()
                    sleep(0.333)
            else:
                self.__checker()
        else:
            raise ValueError("Check parameters carefully")