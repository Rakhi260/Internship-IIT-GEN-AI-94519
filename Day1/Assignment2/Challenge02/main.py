from joke_api import get_joke
from formatter import format_joke

def main():
    print("=== JOKE APP ===")

    while True:
        data = get_joke()
        print(format_joke(data))

        again = input("Want another joke? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
