# Lab: Class 17 - Web Scraper

## Author: Xin Deng

### Links and Resources

- chatGPT
- [Wiki Page Used](https://en.wikipedia.org/wiki/Fatigue)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#searching-the-tree)
- [Class Demo](https://github.com/codefellows/seattle-code-python-401d24/blob/main/class-17/demo/cf-courses/page_parser.py)

### Set up

Type into your terminal:

```bash
mkdir web-scraper
cd web-scraper
touch README.md
python3 -m venv .venv
source .venv/bin/activate
git init
touch .gitignore
mkdir web_scraper
touch web_scraper/scraper.py


```

Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```

Create remote repo and follow instructions

```bash
pip install requests
pip install beautifulsoup4

pip freeze > requirements.txt

```

### Overview - Web Scraper

Scrape a Wikipedia page of your choosing and record which passages need citations. It should report the number of citations needed and identify those cases AND include the relevant passage.

#### Version 1.0

Build 1.0 Feature Tasks

1. Get request that handles a url string and turn integer for citation count
2. Get request that handles a url string and returns a string report

### To run web-scraper:

    ```bash
    python web_scraper/scraper.py
    ```
