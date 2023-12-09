import re


mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

regex = r"(?:\s)[\w.]+@[\w]+\.[\w]+"
match = re.findall(regex, mtxt)

print("Here is the asked emailes --->>")
for email in match:
    print("\t" + email)
print("\n")
