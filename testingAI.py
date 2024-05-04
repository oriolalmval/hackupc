import csv
import requests
import os
import re

# Directory where images will be saved
save_dir = 'downloaded_images'

# Ensure the save directory exists
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to sanitize the filename
def sanitize_filename(filename):
    # Remove characters that are not allowed in filenames on Windows
    return re.sub(r'[\\/:"*?<>|]', '_', filename)

# Open the CSV file containing image URLs
with open('indie2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if present
    for row in reader:
        # Assuming the URLs are in the first, second, and third columns
        urls = [row[0], row[1], row[2]]
        
        for url in urls:
            try:
                # Sanitize the filename
                sanitized_url = sanitize_filename(url)
                filename = os.path.join(save_dir, os.path.basename(sanitized_url))
                
                # Download the image
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    with open(filename, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                    print(f"Downloaded {url} as {filename}")
                else:
                    print(f"Failed to download {url}")
            except Exception as e:
                print(f"An error occurred while processing {url}: {e}")

print("All images downloaded.")