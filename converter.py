import re


def convert_text(text):
    words = re.findall(r"[A-Za-z0-9]+", text)

    return {
        "UPPERCASE": text.upper(),
        "lowercase": text.lower(),
        "Title Case": text.title(),
        "snake_case": "_".join(words).lower(),
        "kebab-case": "-".join(words).lower()
    }
