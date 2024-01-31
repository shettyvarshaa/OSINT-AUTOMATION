import requests
from bs4 import BeautifulSoup

def get_website_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            return title
        else:
            return f"Error: Unable to fetch title. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    target_url = input("Enter the target URL: ")
    title = get_website_title(target_url)
    print(f"Title of the website '{target_url}': {title}")


if __name__ == "__main__":
    main()