import requests 
import os 


def is_download_folder_exist():
    if not os.path.exists('./download_folder'):
        os.mkdir("./download_folder")
        print("download_folder has been created")


def base64_convert_to_zipfile(file_name, base64):
    # download zip file
    with open(f"download_folder/{file_name}.zip", "wb") as file:
        file.write(base64)


def model_download(key):
    url = "https://ai.vazil.me/api/storage/file/download"
    params = {"key": key}

    """
    If you do not have a download path, create a download folder.
    download path: download_file/
    """
    is_download_folder_exist()

    try:
        response = requests.get(url, params=params)
    finally:
        if response:
            file_name = 'dog classifcation model'
            base64 = response.content
            base64_convert_to_zipfile(file_name, base64)
    

if __name__ == "__main__":
    key = "MmYwZTJkYzk0MzNjNDZiMWIyMWY4MWZkYzMyNThmZTYvbW9kZWxzL3RyYWluLTFqeHpna3R5a2g1Ym8uemlw"
    res = model_download(key)