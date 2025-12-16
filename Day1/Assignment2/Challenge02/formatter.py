def format_joke(joke_data):
    if not joke_data:
        return "Could not fetch a joke right now."

    setup = joke_data.get("setup")
    punchline = joke_data.get("punchline")

    return f"\n😂 Joke of the Day 😂\n\n{setup}\n👉 {punchline}\n"
