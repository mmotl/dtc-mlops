import requests
import sys

arg = sys.argv[1]

url=f'http://127.0.0.1:9696/{arg}' #geht
# # url='http://localhost:9696/{arg}' #geht auch
# url='http://0.0.0.0:9696/{arg}' #geht auch

payload = {
    'name': 'Matthias',
    'message': 'Hello from the client!'
}

response = requests.post(url=url, json=payload)
print(response.text)
