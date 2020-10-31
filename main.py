import json
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  response = requests.get('https://www.proxyscan.io/api/proxy?ping=100')
  jsons = json.loads(response.text)
  for i in jsons:
    ip = i["Ip"]
    port = i["Port"]
    t = i["Type"]
    tf = t[0].lower()
    final = f'{tf}://{ip}:{port}'
    print(final)
  return final

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

