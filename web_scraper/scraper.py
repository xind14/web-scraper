from bs4 import BeautifulSoup
import requests

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

    with open("wiki.txt", "w") as f:
        f.write(response.text)

    return len(citations_needed)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Fatigue"
    count = get_citations_needed_count(url)
    print(f"Number of citations needed: {count}")

