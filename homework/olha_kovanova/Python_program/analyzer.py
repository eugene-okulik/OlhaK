import os
import argparse


def find_text_in_logs(log_dir, search_text):
    # Check if the specified directory exists
    if not os.path.isdir(log_dir):
        print(f"The specified {log_dir} directory not found!")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)

        # Process only text files with .log extension
        if os.path.isfile(file_path) and filename.endswith('.log'):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if search_text in line:
                        # Break line into words
                        words = line.split()
                        # Find indices of the search text
                        indexes = [i for i, word in enumerate(words) if search_text in word]

                        for index in indexes:
                            # Get context around the found text
                            start_index = max(index - 5, 0)
                            end_index = min(index + 6, len(words))
                            context = " ".join(words[start_index:end_index])

                            # Print the result
                            print(f"File: {filename}, Line: {line_number}, Context: {context}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Text search in the logs')

    # Adding argument for directory path where log files are located
    parser.add_argument("log_directory", help="Path to the directory with log files")

    parser.add_argument("-d", "--date", help="Search date")
    parser.add_argument("--full", help="Full date match", action="store_true")
    parser.add_argument("--text", help="Text to search for", required=True)

    # Parse arguments
    args = parser.parse_args()

    # Get the log directory from the argument
    log_directory = args.log_directory
    search_word = args.text

    # Call the function to search for the text in logs
    find_text_in_logs(log_directory, search_word)


if __name__ == "__main__":
    main()

# Commands to run:
# By text: python C:\Users\olha.kovanova\OlhaK\homework\olha_kovanova\Python_program\analyzer.py C:\Users\olha.kovanova
# \OlhaK\homework\eugene_okulik\data\logs --text WARN
# By date: python C:\Users\olha.kovanova\OlhaK\homework\olha_kovanova\Python_program\analyzer.py C:\Users\olha.kovanova
# \OlhaK\homework\eugene_okulik\data\logs --text WARN --date 2024-11-01
