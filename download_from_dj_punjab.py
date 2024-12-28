from multiprocessing.sharedctypes import class_cache

from get_song_names import read_url
from bs4 import BeautifulSoup
import requests

base_url = "https://djpunjab.is"

urls = read_url("djpunjab.html")


def go_to_song_page(song_page):
    song_url = base_url + song_page
    response = requests.get(song_url)
    response.raise_for_status()  # Check for HTTP request errors

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find('div', class_='touch-new')
    attrs = element.find('a').attrs
    song_page = attrs.get('href')



def go_to_url():

    for url_ in urls:
        url = base_url + url_

        try:
            # Send a GET request to fetch the webpage
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP request errors

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract specific content (e.g., title and lyrics)
            element = soup.find('div', class_='touch-new')
            attrs = element.find('a').attrs
            song_page = attrs.get('href')
            print(f"I am here: {}")
            go_to_song_page(song_page)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")



go_to_url()