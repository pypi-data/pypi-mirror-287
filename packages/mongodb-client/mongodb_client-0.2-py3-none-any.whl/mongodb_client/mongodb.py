import os
import requests

class MongoDB:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        self.token = None

    def signin(self, email, password):
        url = f'{self.base_url}/signin'
        data = {
            "email": email,
            "password": password
        }
        res = requests.post(url, json=data)
        
        if res.status_code != 200:
            print(F'LOGIN FAILED: {res.text}')
            return False
            
        data = res.json()
        self.token = data['token']        
        return True
        
    def _handle_response(self, response):
        if response.ok:
            return response.json()
        else:
            return {"error": f"Request failed | status-code: {response.status_code} | message: {response.reason} | response: {response.text}"}
    
    def _get_auth_headers(self, token):
        if token:
            return {'Authorization': f'Bearer {token}'}
        elif self.token:
            return {'Authorization': f'Bearer {self.token}'}
        else:
            raise ValueError("No token provided and self.token is None")

    def get_records(self, database, collection, query_params=None, token=None):
        try:
            url = f"{self.base_url}/{database}/{collection}"
            headers = self._get_auth_headers(token)
            response = requests.get(url, headers=headers, params=query_params)
            return self._handle_response(response)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}
    
    def get_record_by_id(self, database, collection, record_id, token=None):
        try:
            url = f"{self.base_url}/{database}/{collection}/{record_id}"
            headers = self._get_auth_headers(token)
            response = requests.get(url, headers=headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}
    
    def create_records(self, database, collection, record_data, token=None):
        try:
            url = f"{self.base_url}/{database}/{collection}"
            headers = self._get_auth_headers(token)
            response = requests.post(url, headers=headers, json=record_data)
            return self._handle_response(response)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}
    
    def update_record(self, database, collection, record_id, updated_data, token=None):
        try:
            url = f"{self.base_url}/{database}/{collection}/{record_id}"
            headers = self._get_auth_headers(token)
            response = requests.put(url, headers=headers, json=updated_data)
            return self._handle_response(response)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}
    
    def delete_record(self, database, collection, record_id, token=None):
        try:
            url = f"{self.base_url}/{database}/{collection}/{record_id}"
            headers = self._get_auth_headers(token)
            response = requests.delete(url, headers=headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}

    def delete_records(self, database, collection, token=None):
        try:
            url = f"{self.base_url}/{database}/{collection}"
            headers = self._get_auth_headers(token)
            response = requests.delete(url, headers=headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            return {"error": f"Request failed: {e}"}
