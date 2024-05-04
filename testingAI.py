import csv
import requests
import os
import time
import random

save_dir = 'downloaded_images'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def download_image_with_retry(url, filename, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f"Downloaded {url} as {filename}")
                break  # Success, exit the loop
            else:
                print(f"Failed to download {url}, status code: {response.status_code}")
                break  # Not a 200 OK, exit the loop
        except Exception as e:
            print(f"An error occurred while processing {url}: {e}")
            if attempt < max_retries - 1:  # Not the last attempt
                wait_time = 2 ** attempt + random.random()  # Exponential backoff
                print(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries reached, giving up.")

with open('filtered_urls.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if present
    for row in reader:
        urls = [row[0], row[1], row[2]]
        
        for url in urls:
            if url:  # Check if the URL is not empty
                # Ensure the URL starts with http:// or https://
                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url  # Prepend http:// if not present
                
                # Extract filename from URL
                filename = os.path.join(save_dir, os.path.basename(url))
                
                # Print the filename for debugging
                print("Downloading:", filename)
                
                # Download the image with retry logic
                download_image_with_retry(url, filename)
            else:
                print("Empty URL detected, skipping...")

print("All images downloaded.")
