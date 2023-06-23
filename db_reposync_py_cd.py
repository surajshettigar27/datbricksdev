import requests
import os

print("before ")
bearer_token = os.environ.get("bearer_token")

for i in bearer_token:
    print(i)
