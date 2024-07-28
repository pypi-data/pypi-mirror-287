from backupfinder.backup_finder import generate_wordlist
from backupfinder.log_finder import generate_log_wordlist

def main():
    url = input("Enter the URL: ")
    if url:
        generate_wordlist(url)
        generate_log_wordlist(url)

if __name__ == "__main__":
    main()
