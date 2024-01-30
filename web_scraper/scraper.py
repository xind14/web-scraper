from bs4 import BeautifulSoup

import requests


def get_citations_needed_count(url):
    url="https://en.wikipedia.org/wiki/Fatigue"
    response=requests.get(url)
    results = parse(response.text)
    soup = BeautifulSoup(results, "html.parser")
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')
    return len(citations_needed)

    with open("courses.txt","w") as f:
      f.write(results)



def get_citations_needed_report():
    url="https://en.wikipedia.org/wiki/Fatigue"
    response=requests.get(url)
    results = parse(response.text)
    soup = BeautifulSoup(results, "html.parser")
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')
    report = "These texts need citations: \n\n"

    for citation in citations_needed:
        parent = citation.find_parent()
        citation_report += f"{parent.text.strip()}\n\n"

    return citation_report



