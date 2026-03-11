import unittest, requests, json, os
from dotenv import load_dotenv

class test(unittest.TestCase):

    def testServerConnection(self):
        server = "http://127.0.0.1:5000"
        res = requests.get(server)
        status = res.status_code

        print("Server connection test")

        self.assertEqual(status, 200)

    
    def testIncorrectServerRoute(self):
        server = "http://127.0.0.1:5000"
        incorrectRoute = "/abcdef"
        status = requests.get(server+incorrectRoute).status_code

        print("Incorrect Server Route Test")

        self.assertEqual(status, 404)


    def testRateLimitOfServer(self):
        server = "http://127.0.0.1:5000/ratetest"
        
        for i in range(10):
            requests.get(server)

        status = requests.get(server).status_code

        print("RateLimitServerTest")
        self.assertEqual(status, 429)


    def testAPIConnection(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q=Almaty&appid={api_key}&units=metric&lang=ru"
        weatherAPI = requests.get(url)
        status = weatherAPI.status_code

        print("Weather API Connection test")

        self.assertEqual(status, 200)
        

    def testJsonData(self):
        with open("json/weather.json", "r") as file:
            data = json.load(file)
        
        print("Data Save Test")

        self.assertEqual(type(data), type(dict()))

unittest.main()