import requests 
import json

from test import dataset_upload_body_for_test

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