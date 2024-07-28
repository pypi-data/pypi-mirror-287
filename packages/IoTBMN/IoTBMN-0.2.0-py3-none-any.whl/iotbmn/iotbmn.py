import requests
import time

class IoTBMN:
    def __init__(self, server_url):
        self.server_url = server_url
        self.session = requests.Session()
        # Initialize connection by calling the serverlet
        try:
            response = self.session.get(self.server_url)
            response.raise_for_status()
            print(f"Connection established with {self.server_url}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to establish connection: {e}")
            raise

    def pinpoll(self, interval=5):
        def pinpoll(self, interval=5):
            while True:
                try:
                    response = self.session.get(f'{self.server_url}/NewIDSInterface/getStatus')
                    response.raise_for_status()
                    try:
                        data = response.json()
                        return data
                    except ValueError:
                        print(f"Error parsing JSON response: {response.text}")
                except requests.exceptions.RequestException as e:
                    print(f"Error polling the serverlet: {e}")
                time.sleep(interval)
