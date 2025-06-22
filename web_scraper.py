import requests
from bs4 import BeautifulSoup
import schedule
import time
import csv

# Function to scrape data
def scrape_website():
    url = "https://quotes.toscrape.com/"  # Example website for scraping
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    # Prepare CSV to store the data
    with open("quotes.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Quote", "Author"])

        # Extract and save quotes and authors
        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            writer.writerow([text, author])

    print("Scraped data successfully and saved to quotes.csv!")

# Schedule the scraping task to run every minute
schedule.every(1).minutes.do(scrape_website)

# Keep the script running to execute scheduled tasks
print("Scheduler is running...")
while True:
    schedule.run_pending()
    time.sleep(1)