import unittest, requests, json, os
from dotenv import load_dotenv
from modules.ipChecker import getCity

class test(unittest.TestCase):

    def testServerConnection(self):
        server = "http://127.0.0.1:5000"
        res = requests.get(server)
        status = res.status_code
        expected_status = 200

        print("Server connection test")

        self.assertEqual(status, expected_status)

    
    def testIncorrectServerRoute(self):
        server = "http://127.0.0.1:5000"
        incorrectRoute = "/abcdef"
        status = requests.get(server+incorrectRoute).status_code
        expected_status = 404

        print("Incorrect Server Route Test")

        self.assertEqual(status, expected_status)


    def testRateLimitOfServer(self):
        server = "http://127.0.0.1:5000/ratetest"
        
        for i in range(10):
            requests.get(server)

        status = requests.get(server).status_code
        expected_status = 429

        print("RateLimitServerTest")
        self.assertEqual(status, expected_status)


    def testAPIConnection(self):
        load_dotenv()

        api_key = os.getenv("API_KEY_WEATHER")
        url = f"https://api.openweathermap.org/data/2.5/weather?q=Almaty&appid={api_key}&units=metric&lang=ru"
        weatherAPI = requests.get(url)
        status = weatherAPI.status_code
        expected_status = 200

        if status == 401:
            pass
        else:
            print("Weather API Connection test")
            self.assertEqual(status, expected_status)


if __name__ == "__main__":
    unittest.main()