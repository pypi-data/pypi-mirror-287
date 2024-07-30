import requests
import os
import json


class ModelDownloader:
    def __init__(self, key, file_name):
        self.key = key
        self.file_name = file_name
        self.model_download()

    @staticmethod
    def is_download_folder_exist():
        if not os.path.exists('./download_folder'):
            os.mkdir("./download_folder")
            print("download_folder has been created")
            print("The model was successfully downloaded.")
        else:
            print("donwload_folder already exist")
            print("The model was successfully downloaded.")

    @staticmethod
    def base64_convert_to_zipfile(file_name, base64_data):
        # download zip file
        with open(f"download_folder/{file_name}.zip", "wb") as file:
            file.write(base64_data)

    def model_download(self):
        url = "https://ai.vazil.me/api/storage/file/download"
        params = {"key": key}

        """
        If you do not have a download path, create a download folder.
        download path: download_file/
        """
        self.is_download_folder_exist()

        try:
            response = requests.get(url, params=params)
            if response:
                base64_data = response.content
                self.base64_convert_to_zipfile(self.file_name, base64_data)
        except Exception as e:
            print(f"Error downloading the model: {e}")


class StatInfoSaver:
    """
    Save statistics information
    """
    def __init__(self, api_key):
        self.url = "https://ai.vazil.me/api/ai/point-statistics"
        self.api_key = api_key
        self.body = None

    def set_stat_info_body(self):
        self.body = {
            "edgeId": "test-edge-id",
            "modelId": "test-model-id",
            "orgId": "test-orgId",
            "projectId": "test-projectId",
            "result": "ok",
            "inferenceRate": 0.8343494534492493,
            "inferenceTime": 47
        }

    def save_stat_info(self):
        params = {"api_key": self.api_key}
        headers = {"Content-Type": "application/json"}

        try:
            self.set_stat_info_body()
            response = requests.post(self.url, params=params, headers=headers, data=json.dumps(self.body)).json()
            if response["status"] != 201:
                return False
            return response
        except requests.exceptions.RequestException as e:
            print("Error occurred: ", e)
            return False
        except ValueError as e:
            print(f"ValueError: {e}")
            return False


if __name__ == "__main__":
    key = "MmYwZTJkYzk0MzNjNDZiMWIyMWY4MWZkYzMyNThmZTYvbW9kZWxzL3RyYWluLTFqeHpna3R5a2g1Ym8uemlw"
    api_key = "bf47a560-d8d2-411b-957b-1e8b3036369f"
    ModelDownloader(key, file_name='ddd')
    saver = StatInfoSaver(api_key)
    response = saver.save_stat_info()
    print(response)
