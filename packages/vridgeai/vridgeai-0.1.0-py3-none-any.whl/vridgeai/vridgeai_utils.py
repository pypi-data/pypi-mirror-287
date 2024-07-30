import requests 
import json

def dataset_upload_body_for_test():
    return {
    "projectId": "p-rkxbu51xz4fs",
    "orgId": "2f0e2dc9433c46b1b21f81fdc3258fe6",
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


def organization_model_check(api_key, orgId):
    url = "https://ai.vazil.me/api/ai/model/org" 
    params = {"api_key": api_key, "orgId": orgId,}

    try:
        response = requests.get(url, params=params).json()
        if response["status"] != 200:
            print("vridgae 서버에 접속이 되지 않습니다.")
            response = False
    finally:
        return response


def project_model_check(api_key, projectId):
    url = "https://ai.vazil.me/api/ai/model/project"
    params = {"api_key": api_key, "projectId": projectId,}

    try:
        response = requests.get(url, params=params).json()
        if response["status"] != 200:
            print("vridgae 서버에 접속이 되지 않습니다.")
            response = False
    finally:
        return response


def upload_dataset(api_key):
    url = "https://ai.vazil.me/api/ai/dataset"
    params = {"api_key": api_key}
    headers = {"Content-Type": "application/json"}

    try:
        # 테스트를 위해서 모든 데이터들이 들어있는 dataset_upload_body_for_test() 변수 사용 
        body = dataset_upload_body_for_test()
        response = response = requests.post(url, params=params, headers=headers, data=json.dumps(body)).json()
        if response["status"] != None:
            print("vridgae 서버에 접속이 되지 않습니다.")
            response = False
    finally:
        return response


def main():
    api_key = "bf47a560-d8d2-411b-957b-1e8b3036369f"
    orgId = "2f0e2dc9433c46b1b21f81fdc3258fe6"
    projectId = "p-rkxbu51xz4fs"

    response = upload_dataset(api_key)
    print(response)
    

if __name__ == "__main__":
    main()