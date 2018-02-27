import re
pattern = r'\d+'
text = "12 ай, 12 жыл 12 үй 12 киши"
res = re.findall(pattern, text)
string = str(res)
print(string)

