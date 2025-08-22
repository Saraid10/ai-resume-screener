import nltk
import os

# Get NLTK's default download directory
path = nltk.downloader.Downloader().default_download_dir()
print(f"NLTK's data directory is: {path}")

# Create the directory if it doesn't exist
os.makedirs(path, exist_ok=True)