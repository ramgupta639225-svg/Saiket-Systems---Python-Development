
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
            return content

    except FileNotFoundError:
        print("Error: File not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except OSError as error:
        print(f"Error reading file: {error}")

    return None


def find_word(content):
    word = input("Enter word to find: ").strip()

    if not word:
        print("Search word cannot be empty!")
    elif word.lower() in content.lower():
        print("Word found in the file!")
    else:
        print("Word not found!")


def replace_word(filename, content):
    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")

    if not old_word:
        print("Word to replace cannot be empty!")
        return

    if old_word.lower() not in content.lower():
        print("Word not found! File was not changed.")
        return

    updated_content = content.replace(old_word, new_word)

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print("File updated successfully!")

    except PermissionError:
        print("Error: Permission denied!")
    except OSError as error:
        print(f"Error saving file: {error}")


filename = "sample.txt"

while True:
    print("\n========== FILE HANDLING TOOL ==========")
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
