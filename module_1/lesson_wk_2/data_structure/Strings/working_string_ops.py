text0 = "From the river to the sea, Palestine will be free insha Allah"
print(text0.upper())
print(text0.lower())
sentence = "Palestine will be free"
print(sentence.title())
print(sentence.replace("Palestine", "Congo"))
txt = "i LOVE gAZA  "
print(txt.swapcase())
text1 = "   Gaza is beautiful"
print(text1.strip())
text1 = "  Gaza is beautiful"
print(text1.lstrip())
text2 = "Gaza is beautiful    "
print(text2.rstrip())
oppressed = "Palestine Congo Sudan"
print(oppressed.split())
text3 = "1,2,3,4,56,789"
print(text3.rsplit(",",3))
lines = "line 1\nline 3\nline 6"
print(lines.splitlines())
text4 = ["I", "love", "Gaza"]
print(".".join(text4))
text5 = "Palestine"
text6 = "is"
text7 = "beautiful"
print(text5.center(20, "_"), text6.center(20, "_"), text7.center(20, "_"))
print(text7.rjust(20, "+"))
num = "92"
print(num.zfill(10))
print("Gaza".isalpha())
print("Gaza1948".isalpha())
print("Gaza123".isalnum())
print("Gaza 123".isalpha())
print("Gaza123".isdigit())
print("123".isdigit())