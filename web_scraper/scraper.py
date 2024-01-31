from bs4 import BeautifulSoup
import requests
import re

def get_citations_needed_count(url):
    """
    Get the count of citations needed for a Wiki page.

    Parameters:
    - url (str): The URL of the Wiki page.

    Returns:
    - int: The number of citations needed.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

# unsure why this is needed but used the class demo
    with open("wiki.txt", "w") as f:
        f.write(response.text)

    return len(citations_needed)

def get_citations_needed_report(url):
    """
    Get a report of citations needed for a Wiki page.

    Parameters:
    - url (str): The URL of the Wiki page.

    Returns:
    - str: A formatted report of citations needed.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

    citation_report = "Citation needed for: \n\n"

    for citation in citations_needed:
      # used gpt for regex bc previous method was including the citation brackets 
      citation_text = re.sub(r'\[.*?\]', '', citation.parent.text) 
      citation_report += f"{citation_text}\n\n"
    return citation_report

# wasn't sure if this was needed but gpt said to add for the prints
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Fatigue"
    count = get_citations_needed_count(url)
    print(f"\nCitations needed: {count}\n")
    report = get_citations_needed_report(url)
    print(report)
