
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://news.ycombinator.com/"

def scrape_headlines():
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "PythonWebScraper/1.0"},
            timeout=15
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.select(".titleline > a")

        if not headlines:
            print("No headlines found on the page.")
            return

        print("\n========== LATEST HEADLINES ==========\n")

        for number, headline in enumerate(headlines, start=1):
            title = headline.get_text(strip=True)
            link = urljoin(url, headline.get("href", ""))

            print(f"{number}. {title}")
            print(f"   Link: {link}\n")

        print(f"Total headlines found: {len(headlines)}")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print(f"Website returned an HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Unable to fetch website: {error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


while True:
    print("\n========== WEB SCRAPER ==========")
    print("1. Get Headlines")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        scrape_headlines()

    elif choice == "2":
        print("Thank you for using Web Scraper!")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")
