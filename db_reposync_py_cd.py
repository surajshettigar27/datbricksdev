import requests
import os


bearer_token = os.environ["bearer_token"]


def getRepos():
    url = "https://burnsmcd-procurement-test.cloud.databricks.com/api/2.0/repos?path_prefix=/Repos/burnsmcd/cor-uip-procurement"

    payload = {}
    headers = {"Authorization": "Bearer dapic174d1ff42ad5f5bb8b1927dccbdf8a3"}

    response = requests.request("GET", url, headers=headers, data=payload)
    respJson = response.json()

    repoId = respJson["repos"][0]["id"]
    return repoId


def refreshRepo(repoId, bearer_token):
    url = (
        "https://burnsmcd-procurement-test.cloud.databricks.com/api/2.0/repos/{repoId}"
    )

    payload = '{\n    "branch": "develop"\n}'
    headers = {"Content-Type": "text/plain", "Authorization": f"Bearer {bearer_token}"}
    response = requests.request("PATCH", url, headers=headers, data=payload)
    print(response.text)


def main():
    repo_id = getRepos()
    refreshRepo(repo_id, bearer_token)
