import os
import requests

class Prenzl:
    def __init__(self, api_key=os.environ.get("PRENZL_API_KEY"), base_url=os.environ.get("PRENZL_BASE_URL", "https://agentlens.onrender.com/")):
        if api_key is None:
            raise ValueError("API key is not set. Please set the PRENZL_API_KEY environment variable or pass the API key as an argument using 'api_key=YOUR_API_KEY'")
        self.api_key = api_key
        self.base_url = base_url

    def prenzl_observe(self, data):
        headers = {"Content-Type": "application/json"}
        payload = {"apiKey": self.api_key, "data": data}
        response = requests.post(f"{self.base_url}/log", json=payload, headers=headers)
        
        if response.ok:
            try:
                return response.json()
            except requests.JSONDecodeError:
                return {"error": "Response is not valid JSON", "content": response.text}
        else:
            return {"error": f"Request failed with status code {response.status_code}", "content": response.text}