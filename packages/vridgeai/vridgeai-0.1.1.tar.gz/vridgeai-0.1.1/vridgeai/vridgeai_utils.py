import requests 
import json


class ModelCheck:
    """
    If you want to look up the organizational project model, use for_organization.
    Conversely, if you are a project model, look up the for_project model
    """
    def __init__(self, api_key, id):
        self.api_key = api_key
        self.id = id

    @staticmethod
    def request(url, params):
        try:
            response = requests.get(url, params=params).json()
            if response["status"] != 200:
                return False
            return response
        except requests.exceptions.RequestException as e:
            print("Error occurred: ", e)
            return False

    def for_organization(self):
        url = "https://ai.vazil.me/api/ai/model/org"
        params = {"api_key": self.api_key, "orgId": self.id}
        return self.request(url, params)

    def for_project(self):
        url = "https://ai.vazil.me/api/ai/model/project"
        params = {"api_key": self.api_key, "projectId": self.id}
        return self.request(url, params)
    

if __name__ == "__main__":
    api_key = "bf47a560-d8d2-411b-957b-1e8b3036369f"
    orgId = "2f0e2dc9433c46b1b21f81fdc3258fe6"
    projectId = "p-rkxbu51xz4fs"