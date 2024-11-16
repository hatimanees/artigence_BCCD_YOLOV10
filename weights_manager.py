import os
import urllib.request

def download_weights(weights_dir, urls):
    """Downloads the weights from the specified URLs."""
    os.makedirs(weights_dir, exist_ok=True)
    for url in urls:
        file_name = os.path.join(weights_dir, os.path.basename(url))
        print(f"Downloading {url}...")
        urllib.request.urlretrieve(url, file_name)
        print(f"Downloaded {file_name}")
