
import re
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."

result = re.findall("or", txt)
print(result)


result_all = re.findall(".", txt)
print(result_all)


result_after_or = re.findall("or.", txt)
print(result_after_or)


result_two_chars_dot = re.findall("..\.", txt)
print(result_two_chars_dot)


print("Hello\nWorld")
print(r"Hello\nWorld")


result_word = re.findall(r"\w", txt)
print(result_word)


result_non_word = re.findall(r"\W", txt)
print(result_non_word)


result_digit = re.findall(r"\d", txt)
print(result_digit)


result_non_digit = re.findall(r"\D", txt)
print(result_non_digit)


result_space = re.findall(r"\s", txt)
print(result_space)


result_non_space = re.findall(r"\S", txt)
print(result_non_space)


result_consonants = re.findall(r"[bcdfghjklmnpqrstvxz]", txt)
print(result_consonants)


result_non_vowels = re.findall(r"[^aeiouy]", txt)
print(result_non_vowels)


result_digits_and_af = re.findall(r"[0-9a-f]", txt)
print(result_digits_and_af)


result_integers = re.findall(r"\d+", txt)
print(result_integers)

result_word_like = re.findall(r"\w+", txt)
print(result_word_like)


result_words_with_or = re.findall(r"\w*or\w*", txt)
print(result_words_with_or)


result_greedy = re.findall(r"\w*\d", "abc123def456ghi")
print(result_greedy)


result_lazy = re.findall(r"\w*?\d", "abc123def456ghi")
print(result_lazy)


mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

pattern = r'\s(\w+(?:\.\w*)?@\w+(?:\.\w+)+)'

valid_emails = re.findall(pattern, mtxt)

print(valid_emails)

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
