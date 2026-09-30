from formatter import format_file
from proxy_tester import run_tests
from config import INPUT_FILE, FORMATTED_FILE


def main():
    print("=" * 55)
    print("          PROXY FORMATTER & TESTER")
    print("=" * 55)
    print("1. Format proxy list")
    print("2. Test formatted proxies")
    print("3. Format and test")
    print("4. Exit")
    choice = input("\nChoose an option: ").strip()

    if choice in {"1", "3"}:
        try:
            count, invalid, path = format_file(INPUT_FILE, FORMATTED_FILE)
            print(f"\nFormatted: {count} | Skipped: {invalid}")
            print(f"Output: {path}")
        except FileNotFoundError as exc:
            print(f"Error: {exc}")
            return
    if choice in {"2", "3"}:
        url = input("Enter test URL: ").strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        run_tests(url)
    elif choice == "4":
        print("Exiting.")
    elif choice not in {"1", "2", "3"}:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
