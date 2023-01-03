import requests
import time

while True:
    print("requesting")
    api = "http://192.168.68.113:5000"
    try:
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")
    except:
        print("Error")

    time.sleep(100)
