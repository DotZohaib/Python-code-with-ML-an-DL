import requests
from bs4 import BeautifulSoup

url = "https://awamiawaz.pk/"
url = "https://awamiawaz.pk/category/latest-news"
url = "https://awamiawaz.pk/category/sindh-news"
url = "https://awamiawaz.pk/category/awami-awaz-tv"
url = "https://awamiawaz.pk/category/national"
url = "https://awamiawaz.pk/category/todays-newspaper"
url = "https://awamiawaz.pk/category/articles"
url = "https://awamiawaz.pk/category/international"
url = "https://awamiawaz.pk/category/sports"
url = "https://awamiawaz.pk/category/entertainment"
url = "https://awamiawaz.pk/category/health"
url = "https://awamiawaz.pk/category/special-reports"


r = requests.get(url)

if r.status_code != 200:
    print("Failed to retrieve the page.")
    exit()

htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title
print("Title:", title.text)

paras = soup.find_all('p')
for idx, para in enumerate(paras, start=1):
    print(f"Paragraph {idx}: {para.text}")

first_paragraph = soup.find('p')
print("First Paragraph:", first_paragraph.text)

print("Page Text:", soup.get_text())

with open("file.csv", "w") as f:
    f.write("Every,word,will,go,in,separate,column\n")
    f.write("This,will,go,in,next,row")

ul = soup.find(id="li")
if ul:
    elem = ul.next_sibling.next_sibling
    print("Next Sibling of ul:")
    for i in elem.stripped_strings:
        print(i)

    print("Children of ul:")
    for i in ul.children:
        print(i)
else:
    print("Element with id 'li' not found.")
