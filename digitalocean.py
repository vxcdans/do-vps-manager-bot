import requests
from config import DO_TOKEN

BASE_URL = "https://api.digitalocean.com/v2"

class DigitalOceanError(Exception):
    pass

class DigitalOcean:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {DO_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def request(self, method, path, payload=None):
        try:
            response = self.session.request(
                method, f"{BASE_URL}{path}", json=payload, timeout=30,
            )
        except requests.RequestException:
            raise DigitalOceanError("Tidak dapat terhubung ke DigitalOcean API.")
        if response.status_code == 204:
            return {}
        try:
            data = response.json()
        except ValueError:
            data = {}
        if not response.ok:
            message = data.get("message", f"HTTP {response.status_code}")
            raise DigitalOceanError(str(message)[:300])
        return data

    def get(self, path):
        return self.request("GET", path)

    def post(self, path, payload):
        return self.request("POST", path, payload)

    def delete(self, path):
        return self.request("DELETE", path)
