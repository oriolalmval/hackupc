import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import concurrent.futures
from time import sleep

def download_image(url, error_flag):
    try:
        headers = {
            'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
            'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
            'Accept-Language' : 'en-US,en;q=0.5',
            'DNT'             : '1', # Do Not Track Request Header 
            'Connection'      : 'close'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            print(f"Error downloading image from {url}: {response.status_code}")
            error_flag[0] = True  # Marcar error si ocurre
            return None
    except requests.RequestException as e:
        print(f"Request error downloading image from {url}: {e}")
        error_flag[0] = True  # Marcar error si ocurre
        return None
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")
        error_flag[0] = True  # Marcar error si ocurre
        return None

if __name__ == "__main__":
    # Read image URLs from CSV file using pandas
    df = pd.read_csv('indie2.csv')

    image_urls = []
    for index, col in df.iterrows():
        index += 1
        url1 = col.iloc[0]  
        url2 = col.iloc[1]  
        url3 = col.iloc[2]  
        combined_url = f"{url1}{url2}{url3}"  
        image_urls.append(combined_url)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("Downloading images from:")
        for url in image_urls:
            print(url)
        error_flag = [False]  # Bandera de error compartida
        future_to_url = {executor.submit(download_image, url, error_flag): url for url in image_urls}
        downloaded_images = []
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            if error_flag[0]:  # Verificar si se produjo un error
                print("Se produjo un error. Deteniendo la descarga de imágenes.")
                break
            try:
                image = future.result()
                if image:
                    downloaded_images.append(image)
            except Exception as e:
                print(f"Exception occurred while downloading image from {url}: {e}")
                error_flag[0] = True  # Marcar error si ocurre
            
            # Agregar un retraso de 0.5 segundos entre cada descarga de imagen
            sleep(0.5)

    print(downloaded_images)
