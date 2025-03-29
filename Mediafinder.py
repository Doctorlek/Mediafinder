import requests
from bs4 import BeautifulSoup

def scrape_media(url):
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # ייצור שגיאה אם הסטטוס אינו 2xx
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    media_links = []
    for item in soup.find_all('a', href=True):  # חיפוש קישורים
        media_link = item['href']
        if media_link.endswith(('.mp4', '.avi', '.mkv', '.m3u8')):  # הוספת .m3u8
            media_links.append(media_link)

    return media_links

if __name__ == "__main__":
    while True:
        url = input("Enter the URL of your media page (or type 'exit' to quit): ")  # קלט מהמשתמש
        if url.lower() == 'exit':
            break  # יציאה מהלולאה אם המשתמש הקליד 'exit'
        
        media_links = scrape_media(url)

        if media_links:
            print("Found media links:")
            for link in media_links:
                print(link)  
        else:
            print("No media links found.")
