import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"


def scrape_headlines():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.select(".titleline > a")

        if len(headlines) == 0:
            print("No headlines found.")
            return

        print("\n===== LATEST HEADLINES =====\n")

        count = 1

        for headline in headlines:
            title = headline.get_text()
            link = headline.get("href")

            print(f"{count}. {title}")
            print(f"Link: {link}\n")

            count += 1

        print("Total headlines:", len(headlines))

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Check your internet.")

    except requests.exceptions.RequestException as error:
        print("Unable to fetch headlines:", error)


while True:
    print("\n===== WEB SCRAPER =====")
    print("1. Get Headlines")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        scrape_headlines()

    elif choice == "2":
        print("Thank you for using Web Scraper!")
        break

    else:
        print("Invalid choice. Please select 1 or 2.")
