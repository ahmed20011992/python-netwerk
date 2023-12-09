import re


def find_substring(pattern, text):
    result = re.findall(pattern, text)
    print(result)


txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."

# Find all occurrences of "or"
find_substring("or", txt)

# Find all characters
find_substring(".", txt)

# Find "or" followed by any character
find_substring("or.", txt)

# Find any two characters followed by a dot
find_substring("..\\.", txt)

# Print "Hello\nWorld"
print("Hello\nWorld")

# Print raw string "Hello\nWorld"
print(r"Hello\nWorld")

# Find all word characters
find_substring(r"\w", txt)

# Find all non-word characters
find_substring(r"\W", txt)

# Find all digits
find_substring(r"\d", txt)

# Find all non-digits
find_substring(r"\D", txt)

# Find all whitespace characters
find_substring(r"\s", txt)

# Find all non-whitespace characters
find_substring(r"\S", txt)

# Find all consonants
find_substring(r"[bcdfghjklmnpqrstvxz]", txt)

# Find all non-vowels
find_substring(r"[^aeiouy]", txt)

# Find all digits and lowercase letters a-f
find_substring(r"[0-9a-f]", txt)

# Find all integers
find_substring(r"\d+", txt)

# Find all word-like sequences
find_substring(r"\w+", txt)

# Find all words containing "or"
find_substring(r"\w*or\w*", txt)

# Find greedy matching
find_substring(r"\w*\d", "abc123def456ghi")

# Find lazy matching
find_substring(r"\w*?\d", "abc123def456ghi")

# Example with emails
mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."
pattern = r'\s(\w+(?:\.\w*)?@\w+(?:\.\w+)+)'
valid_emails = re.findall(pattern, mtxt)
print(valid_emails)

# Example with HTML
with open("tabla.html", encoding="utf-8") as file:
    txt = file.read()

time = re.findall(
    r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>', txt)
print(time)

season = re.findall(
    r'<h4.*?>\s*Simpsons\s*</h4>.*?Säsong (\d+).*?</p>', txt, re.DOTALL)
episode = re.findall(
    r'<h4.*?>\s*Simpsons\s*</h4>.*?Del (\d+) av (\d+).*?</p>', txt, re.DOTALL)
description = re.findall(
    r'<h4.*?>\s*Simpsons\s*</h4>.*?Del.*?\.([^\.]*).*?</p>', txt, re.DOTALL)

min_length = min(len(time), len(season), len(episode), len(description))
time = time[:min_length]
season = season[:min_length]
episode = episode[:min_length]
description = description[:min_length]

result_text = ""
for a, b, c, d in zip(time, season, episode, description):
    result_text += f"{'-' * 28}\nTid:      {a}\nSäsong:   {b}\nAvsnitt:  {c}\nHandling: {d}.\n"

print(result_text)
