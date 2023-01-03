import requests
import time

import requests
import time

def call_api(api, filename):
    print("requesting")
    try:
        response = requests.get(f"{api}/file_upload/{filename}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")
    except:
        print("Error")

while True:
    api = "http://192.168.68.113:5000"
    call_api(api, "something")
    time.sleep(100)

