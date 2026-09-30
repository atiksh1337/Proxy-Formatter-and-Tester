from pathlib import Path
from config import INPUT_FILE, FORMATTED_FILE
from proxy_parser import normalize_proxy, parse_labeled_lines, parse_four_lines


def clean_label(line):
    labels = {"ip":"host", "host":"host", "hostname":"host", "port":"port",
              "username":"username", "user":"username", "password":"password", "pass":"password"}
    if ":" not in line:
        return None
    label, value = line.split(":", 1)
    key = labels.get(label.strip().lower())
    return (key, value.strip()) if key else None


def format_proxy(proxy):
    return normalize_proxy(proxy)


def format_file(input_file=INPUT_FILE, output_file=FORMATTED_FILE):
    input_path = Path(input_file)
    output_path = Path(output_file)
    if not input_path.is_file():
        raise FileNotFoundError(f"{input_file} was not found.")

    with input_path.open("r", encoding="utf-8-sig") as file:
        lines = [line.strip() for line in file if line.strip()]

    formatted, invalid, i = [], 0, 0
    while i < len(lines):
        result = format_proxy(lines[i])
        if result:
            formatted.append(result); i += 1; continue

        first_label = clean_label(lines[i])
        if first_label:
            group = []
            j = i
            while j < len(lines) and clean_label(lines[j]) and len(group) < 4:
                group.append(lines[j]); j += 1
            result_tuple = parse_labeled_lines(group) if len(group) == 4 else None
            if result_tuple:
                u, p, h, port = result_tuple
                formatted.append(f"{u}:{p}@{h}:{port}")
                i = j; continue

        if i + 3 < len(lines) and not any(clean_label(x) for x in lines[i:i+4]):
            result_tuple = parse_four_lines(lines[i:i+4])
            if result_tuple:
                u, p, h, port = result_tuple
                formatted.append(f"{u}:{p}@{h}:{port}")
                i += 4; continue

        invalid += 1
        i += 1

    formatted = list(dict.fromkeys(formatted))
    with output_path.open("w", encoding="utf-8") as file:
        for proxy in formatted:
            file.write(proxy + "\n")
    return len(formatted), invalid, output_path.resolve()


def main():
    try:
        count, invalid, path = format_file()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        return
    print("\nFormatting completed!")
    print(f"Successfully formatted: {count}")
    print(f"Skipped entries: {invalid}")
    print(f"Output saved to: {path}")


if __name__ == "__main__":
    main()
