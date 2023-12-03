import re

text = input()
pattern = r"(?:[@#]+)(?P<color>[a-z]+)(?:[^A-Za-z0-9]*)(?:\/)(?P<amount>\d+)(?:/)"

matches = re.finditer(pattern, text)
for match in matches:
    print(f"You found {match.group('amount')} {match.group('color')} eggs!")
