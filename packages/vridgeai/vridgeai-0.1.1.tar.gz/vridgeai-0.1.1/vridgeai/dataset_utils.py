import requests
import json


class DatasetUploader:
    def __init__(self, project_id, org_id, api_key):
        self.projectId = project_id
        self.orgId = org_id
        self.api_key = api_key
        self.url = "https://ai.vazil.me/api/ai/dataset"
        self.body = None

    def set_dataset_upload_body(self):
        self.body = {
            "projectId": self.projectId,  # p-rkxbu51xz4fs
            "orgId": self.orgId,  # 2f0e2dc9433c46b1b21f81fdc3258fe6
            "train": [
                {
                    "id": "6694da754f5ac118d66912e3",
                    "key": "2f0e2dc9433c46b1b21f81fdc3258fe6/image/p-rkxbu51xz4fs/img_32908.jpg",
                    "filename": "img_32908.jpg",
                    "fileSize": 534,
                    "folder": "2",
                    "orgId": "2f0e2dc9433c46b1b21f81fdc3258fe6",
                    "projectId": "p-rkxbu51xz4fs",
                    "tags": [],
                    "approval": False,
                    "annotationObjectList": None,
                    "size": None,
                    "splitType": "TRAIN",
                    "createDate": "2024-07-15T17:14:45.698",
                    "updateDate": None,
                    "deleteDate": None,
                    "editor": None,
                    "creator": {
                        "id": 2,
                        "name": "peter",
                        "email": "ghp@vazilcompany.com",
                        "avatar": ""
                    },
                    "type": "IMAGE"
                }
            ],
            "valid": [
                {
                    "id": "6694da754f5ac118d66912e1",
                    "key": "2f0e2dc9433c46b1b21f81fdc3258fe6/image/p-rkxbu51xz4fs/img_32914.jpg",
                    "filename": "img_32914.jpg",
                    "fileSize": 560,
                    "folder": "2",
                    "orgId": "2f0e2dc9433c46b1b21f81fdc3258fe6",
                    "projectId": "p-rkxbu51xz4fs",
                    "tags": [],
                    "approval": False,
                    "annotationObjectList": None,
                    "size": None,
                    "splitType": "VALID",
                    "createDate": "2024-07-15T17:14:45.697",
                    "updateDate": None,
                    "deleteDate": None,
                    "editor": None,
                    "creator": {
                        "id": 2,
                        "name": "peter",
                        "email": "ghp@vazilcompany.com",
                        "avatar": ""
                    },
                    "type": "IMAGE"
                }
            ],
            "test": [
                {
                    "id": "6694da754f5ac118d66912f1",
                    "key": "2f0e2dc9433c46b1b21f81fdc3258fe6/image/p-rkxbu51xz4fs/img_32939.jpg",
                    "filename": "img_32939.jpg",
                    "fileSize": 652,
                    "folder": "2",
                    "orgId": "2f0e2dc9433c46b1b21f81fdc3258fe6",
                    "projectId": "p-rkxbu51xz4fs",
                    "tags": [],
                    "approval": False,
                    "annotationObjectList": None,
                    "size": None,
                    "splitType": "TEST",
                    "createDate": "2024-07-15T17:14:45.82",
                    "updateDate": None,
                    "deleteDate": None,
                    "editor": None,
                    "creator": {
                        "id": 2,
                        "name": "peter",
                        "email": "ghp@vazilcompany.com",
                        "avatar": ""
                    },
                    "type": "IMAGE"
                }
            ],
            "preprocessing": {
                "resize": "Stretch to",
                "width": 380,
                "height": 380,
                "grayscale": False
            },
            "augmentations": {
                "brightness": {
                    "enable": False,
                    "scaleFactor": 1,
                    "offset": 0
                },
                "rotation": {
                    "enable": False,
                    "angle": 0
                },
                "crop": {
                    "enable": False,
                    "cropRate": 0
                },
                "flip": {
                    "enable": False,
                    "flipType": "HORIZONTAL"
                }
            },
            "details": {
                "versionId": 0,
                "name": "111_dataset_2024. 7. 29.",
                "createdAt": "2022-11-16T10:38:00",
                "trainingType": "IMAGE_CLASSIFICATION"
            },
            "labelMap": {
                "1": {
                    "color": "#47c9ad",
                    "count": 30,
                    "num": 1
                },
                "2": {
                    "color": "#008a6c",
                    "count": 42,
                    "num": 0
                }
            },
            "createUser": {
                "id": 1,
                "name": "관리자",
                "email": "admin@vazilcompany.com",
                "avatar": None
            },
            "datasetType": "IMAGE"
        }

    def dataset_upload(self):
        try:
            self.set_dataset_upload_body()
            params = {"api_key": self.api_key}
            headers = {"Content-Type": "application/json"}

            response = requests.post(self.url, params=params, headers=headers, data=json.dumps(self.body)).json()
            if response["status"] != None:
                response = False
            return response
        except requests.exceptions.RequestException as e:
            print("Error occurred: ", e)
            return False
        except ValueError as e:
            print(f"ValueError: {e}")
            return False


if __name__ == "__main__":
    projectId = "p-rkxbu51xz4fs"
    orgId = "2f0e2dc9433c46b1b21f81fdc3258fe6"
    api_key = "bf47a560-d8d2-411b-957b-1e8b3036369f"

    uploader = DatasetUploader(projectId, orgId, api_key)
    response = uploader.dataset_upload()
    print(response)
