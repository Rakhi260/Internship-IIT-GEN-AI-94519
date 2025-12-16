from news_api import fetch_top_headlines
from utils import print_headlines

def main():
    print("NEWS APP")

    country = input("Enter country code (default: in): ").strip() or "in"

    articles = fetch_top_headlines(country)

    if not articles:
        print("Could not fetch news. Try again.")
    else:
        print_headlines(articles)

if __name__ == "__main__":
    main()
