from bs4 import BeautifulSoup


def get_song_names(file_path = 'amz_music.html'):
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

def read_url(file_path='djpunjab.html'):
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
        music_elements = soup.find_all('a')
        for element in music_elements:
            attrs = element.attrs
            song_name = attrs['href']
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
