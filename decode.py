import pandas as pd

key = "CodeDeCode2.txt"
key2 = "CodeDeCode.txt"

df = pd.read_table(key, header = None, sep = "\t") 
df2 = pd.read_table(key2, header = None, sep = "\t")

filepath = "nom.txt"
with open(filepath, "r") as file2r:
    text = file2r.read()

b_values = text.split()

ascii_s = ""

for value in b_values:

    an_integer = int(value, 2)
    ascii_character = chr(an_integer)
    ascii_s += ascii_character

letters = ascii_s.split()
#print(letters)

out_mes = []
for letter in letters:
    out = df[df[1].str.contains(letter, case = True, regex = False)]
    out_mes.append(out[0].to_string(header = False ,index = False).replace(' ',''))

out_mes = "".join(out_mes)
print(out_mes)
numbers = out_mes.split('.')

result = []

for letter in numbers: 
    result.append(df2[0][int(letter) - 1])

result = "".join(result)
print(result)
