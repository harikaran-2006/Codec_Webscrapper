import requests
from bs4 import BeautifulSoup
import schedule
import time
import csv


def scrape_website():
    url = "https://quotes.toscrape.com/" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    with open("quotes.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Quote", "Author"])

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            writer.writerow([text, author])

    print("Scraped data successfully and saved to quotes.csv!")


schedule.every(1).minutes.do(scrape_website)

print("Scheduler is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
