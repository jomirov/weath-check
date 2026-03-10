import unittest, requests, json, time

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
        self.assertEqual(status, 429)


    def testAPIConnection(self):
        weatherAPI = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Almaty&appid=68adc50359a9b655c39171f4ce0c136c&units=metric&lang=ru")
        status = weatherAPI.status_code

        print("Weather API Connection test")

        self.assertEqual(status, 200)
        

    def testJsonData(self):
        with open("json/weather.json", "r") as file:
            data = json.load(file)
        
        print("Data Save Test")

        self.assertEqual(type(data), type(dict()))

unittest.main()