def print_headlines(articles, count=5):
    print("\nTop News Headlines:\n")

    for idx, article in enumerate(articles[:count], start=1):
        print(f"{idx}. {article.get('title')}")
        print(f"   Source: {article.get('source_id')}")
        print()
