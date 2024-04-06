import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://awamiawaz.pk/",
    "https://awamiawaz.pk/category/latest-news",
    "https://awamiawaz.pk/category/sindh-news",
    "https://awamiawaz.pk/category/awami-awaz-tv",
    "https://awamiawaz.pk/category/national",
    "https://awamiawaz.pk/category/todays-newspaper",
    "https://awamiawaz.pk/category/articles",
    "https://awamiawaz.pk/category/international",
    "https://awamiawaz.pk/category/sports",
    "https://awamiawaz.pk/category/entertainment",
    "https://awamiawaz.pk/category/health",
    "https://awamiawaz.pk/category/special-reports"
]

for url in urls:
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to retrieve the page for {url}")
        continue

    soup = BeautifulSoup(r.content, 'html.parser')

    # Print the title
    title = soup.title
    print("Title for", url, ":", title.text)

    # Extract and print text content of title, paragraphs, headings, and divs
    elements = soup.find_all(['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div'])
    for idx, element in enumerate(elements, start=1):
        if element.text.strip():
            print(f"Text content of Element {idx} for {url}:\n{element.text.strip()}\n")

    print("=" * 50)  # Separator between URLs
