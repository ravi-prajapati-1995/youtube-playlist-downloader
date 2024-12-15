import requests
from bs4 import BeautifulSoup

from get_song_names import get_song_names


def download_file(url, file_name):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Save the file locally
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded successfully as {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")

def fetch_and_parse_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract the title of the page
        title = soup.title.string if soup.title else "No title found"
        print(f"Page Title: {soup.prettify()}")

        # Example: Extract all links from the page
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print(f"Found {len(links)} links on the page:")
        for link in links[:10]:  # Print first 10 links
            print(link)

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL: {e}")

from bs4 import BeautifulSoup

def read_html_from_file(file_path):
    song_names = []
    try:
        # Open the HTML file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Example: Print the formatted HTML
        print("Formatted HTML from file:")
        # print(soup.prettify())
        music_elements = soup.find_all('music-image-row')
        for element in music_elements:
            attrs = element.attrs
            song_name = f"{attrs['secondary-text-2']} by {attrs['secondary-text-1']}".replace("[Explicit]", "")
            song_names.append(song_name)
            print(song_name)

        # Example: Extract and print the title
        title = soup.title.string if soup.title else "No title found"
        print(f"\nPage Title: {title}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return song_names


# Example usage
# file_path = "amz_music.html"  # Replace with the path to your HTML file
# read_html_from_file(file_path)
print(get_song_names())

# fetch_and_parse_url("https://music.amazon.in/albums/B0CLDFTG7K?trackAsin=B0CLDFY5W1")
# Example usage
# url = "https://example.com/song.mp3"  # Replace with your file URL
# file_name = "song.mp3"               # Desired file name
# download_file(url, file_name)
