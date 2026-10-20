
from collections import Counter
import re

def analyze_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        words = re.findall(r"\b\w+\b", content.lower())
        lines = content.splitlines()
        characters = len(content)
        frequency = Counter(words)

        print("\n========== WORD COUNT REPORT ==========")
        print(f"Total words: {len(words)}")
        print(f"Total lines: {len(lines)}")
        print(f"Total characters: {characters}")

        print("\nWord Frequency:")

        if frequency:
            for word, count in frequency.most_common():
                print(f"{word}: {count}")
        else:
            print("No words found in the file.")

        if frequency:
            word, count = frequency.most_common(1)[0]
            print(f"\nMost common word: {word} ({count} times)")

    except FileNotFoundError:
        print("Error: File not found!")

    except PermissionError:
        print("Error: Permission denied!")

    except OSError as error:
        print(f"File error: {error}")


while True:
    print("\n========== WORD COUNT TOOL ==========")
    print("1. Analyze File")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        filename = input("Enter text file name: ").strip()

        if not filename:
            print("File name cannot be empty!")
        else:
            analyze_file(filename)

    elif choice == "2":
        print("Thank you for using Word Count Tool!")
        break

    else:
        print("Invalid choice!")
