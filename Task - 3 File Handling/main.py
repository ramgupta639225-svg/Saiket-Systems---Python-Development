def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        print("\nFile Content:")
        print(content)

        return content

    except FileNotFoundError:
        print("File not found!")

    except PermissionError:
        print("Permission denied!")

    except OSError as error:
        print("Error:", error)

    return None


def find_word(content):
    word = input("Enter word to find: ").strip()

    if word == "":
        print("Please enter a word.")
    elif word.lower() in content.lower():
        print("Word found!")
    else:
        print("Word not found!")


def replace_word(filename, content):
    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")

    if old_word == "":
        print("Please enter a word to replace.")
        return

    if old_word not in content:
        print("Word not found. File was not changed.")
        return

    content = content.replace(old_word, new_word)

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        print("File updated successfully!")

    except PermissionError:
        print("Permission denied!")

    except OSError as error:
        print("Error saving file:", error)


filename = "sample.txt"

while True:
    print("\n===== FILE HANDLING TOOL =====")
    print("1. Read File")
    print("2. Find Word")
    print("3. Replace Word")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_file(filename)

    elif choice == "2":
        content = read_file(filename)

        if content is not None:
            find_word(content)

    elif choice == "3":
        content = read_file(filename)

        if content is not None:
            replace_word(filename, content)

    elif choice == "4":
        print("Thank you for using File Handling Tool!")
        break

    else:
        print("Invalid choice! Please select 1 to 4.")

