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
        """
        Constantly poll the serverlet to check its status.
        Args:
        - interval (int): Time interval in seconds between polls.
        
        Returns:
        - The value from the online serverlet.
        """
        while True:
            try:
                response = self.session.get(self.server_url)
                response.raise_for_status()
                data = response.json()  # Assuming the serverlet returns JSON data
                print(f"Received data: {data}")
                return data  # You can change this to suit your needs
            except requests.exceptions.RequestException as e:
                print(f"Error polling the serverlet: {e}")
            time.sleep(interval)
