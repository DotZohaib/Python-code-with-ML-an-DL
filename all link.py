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

    links = soup.find_all('a', href=True)
    for idx, link in enumerate(links, start=1):
        print(f"Link {idx}: {link['href']}")

    print("=" * 50) 