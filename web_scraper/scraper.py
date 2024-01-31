from bs4 import BeautifulSoup
import requests

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

# unsure why this is needed but used the class demo
    with open("wiki.txt", "w") as f:
        f.write(response.text)

    return len(citations_needed)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

    citation_report = "Citation needed for: \n\n"

    for citation in citations_needed:
      citation_text = citation.parent.get_text()
      citation_report += f"{citation_text}\n\n"
      
    return citation_report

# wasn't sure if this was needed but gpt said to add for the prints
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Fatigue"
    count = get_citations_needed_count(url)
    print(f"Number of citations needed: {count}")

    report = get_citations_needed_report(url)
    print(report)
