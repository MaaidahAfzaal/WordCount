import argparse
import locale

def get_bytes(filename):
    with open(filename, 'rb') as file:
        byte_count = len(file.read())
    return byte_count

def get_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

def get_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        word_count = len(words)
    return word_count

def get_characters(filename):
    with open(filename, 'rb') as file:
        if locale.getpreferredencoding() == 'UTF-8':
            character_count = len(file.read().decode('utf-8'))
        else:
            character_count = len(file.read())
    return character_count

def main():
    parser = argparse.ArgumentParser(description="This program is a unix version of the command wc (word counter)")

    parser.add_argument("-o", "--options", choices=['-c', '-l', '-w', '-m'], help="Choose what to count (bytes, lines, words or characters)")
    parser.add_argument("file_path", help="Path to the file")

    args = parser.parse_args()
    filename = args.file_path

    if args.options == '-c':
        byte_count = get_bytes(filename)
        print(f"Number of bytes in {filename} = {byte_count} bytes")
    elif args.options == '-l':
        line_count = get_lines(filename)
        print(f"Number of lines in {filename} = {line_count} lines")
    elif args.options == '-w':
        word_count = get_words(filename)
        print(f"Number of words in {filename} = {word_count} words")
    elif args.options == '-m':
        character_count = get_characters(filename)
        print(f"Number of characters in {filename} = {character_count} characters")
    else:
        # If no specific operation is given, default to counting bytes, lines, and words
        byte_count = get_bytes(filename)
        line_count = get_lines(filename)
        word_count = get_words(filename)
        print(f"Number of bytes in {filename} = {byte_count} bytes")
        print(f"Number of lines in {filename} = {line_count} lines")
        print(f"Number of words in {filename} = {word_count} words")

if __name__ == "__main__":
    main()
