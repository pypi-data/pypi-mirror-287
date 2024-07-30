# 전체 데이터를 데이터베이스에서 다 조회했다고 가정한 후 나온 값이라고 가정.

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


