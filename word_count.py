import argparse

def main():
    parser = argparse.ArgumentParser(description= "This program is a unix version of the command wc (word counter)" )
    parser.add_argument("-c", "--count", help="Count the bytes in a document.")
    parser.add_argument("-l", "--lines", help="Count the number of lines in a document.")
    parser.add_argument("-w", "--words", help="Count the number of words in a document.")

    args = parser.parse_args()
    
    if args.count:
        try:
            with open(args.count, 'rb') as file:
                byte_count = len(file.read())
            print(f"Number of bytes in {args.count} = {byte_count}")
            
        except FileNotFoundError:
            print("Error : File not Found. Enter a valid file name.")
            
    elif args.lines:
        try:    
            with open(args.lines, 'r') as file:
                line_count = sum(1 for line in file)
            print(f"Number of files in {args.lines} = {line_count}")
            
        except FileNotFoundError:
            print("Error : File not Found. Enter a valid file name.")
            
    elif args.words:
        try:    
            with open(args.words, 'r') as file:
                words = file.read().split()
                word_count = len(words)
            print(f"Number of words in {args.words} = {word_count}")
            
        except FileNotFoundError:
            print("Error : File not Found. Enter a valid file name.")
        
if __name__ == "__main__":
    main()

    
            
    