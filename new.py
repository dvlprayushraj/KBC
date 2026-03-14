# Solution 1: Basic Approach Using `requests` and `BeautifulSoup`

import os  # Provides functions for interacting with the operating system
import requests  # Allows sending HTTP requests
from bs4 import BeautifulSoup  # Used for parsing HTML content

def download_image(url, folder_path):
    """Download an image from a URL to the specified folder."""
    # Get the image name from the URL
    image_name = url.split("/")[-1]
    # Send a GET request to the image URL
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the image to the local directory
        with open(os.path.join(folder_path, image_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {image_name}")
    else:
        print(f"Failed to download: {url}")

def download_images_from_url(website_url, folder_path):
    """Download all images from a specified URL."""
    # Send a GET request to the website URL
    response = requests.get(website_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the website content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all image tags in the HTML content
        img_tags = soup.find_all('img')
        
        # Create the directory if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Download each image
        for img in img_tags:
            img_url = img.get('src')
            # If the image URL is valid, download the image
            if img_url and img_url.startswith(('http://', 'https://')):
                download_image(img_url, folder_path)
            else:
                print(f"Invalid URL found: {img_url}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Get the URL and folder path from the user
website_url = input("Enter the URL of the website with images: ")
folder_path = "downloaded_images"  # Folder to save the images

# Download images from the specified URL
download_images_from_url(website_url, folder_path)
