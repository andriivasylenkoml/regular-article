import re

def fix_links_in_file(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Match [https://....} and replace } with ]
    fixed_text = re.sub(r"\[(https?://[^\]\s{}]+)}", r"[\1]", text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(fixed_text)

    print(f"Fixed links saved to: {output_file}")
if __name__ == "__main__":
    # Example usage
    fix_links_in_file("input.txt", "output.txt")
