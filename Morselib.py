import pandas as pd

key = "CodeDeCode.txt"

df = pd.read_table(key, header = None, sep = "\t") 

out_p = df.iloc[26][1]

input_mes = "desolequejenutiliseraispaslesespacesetjesuisdesolepourmonfrancaisaplus"
out_mes = []

for letter in input_mes: 
    out = df[df[0].str.contains(letter)]
    out_mes.append(out[3].to_string(header = False ,index = False).replace(' ','',1))
    out_mes.append(out_p)
out_mes = out_mes[:-1]
out_mes = " ".join(out_mes)


binar = [[" ",".","-"],["00100000 ","00101110 ","00101101 "]]
result = []

for string in out_mes:
    for char_n in range(3):
        string = string.replace(binar[0][char_n],binar[1][char_n])
    result.append(string)

result = "".join(result)

with open("Message.txt", "w") as file2w:
    file2w.write(result)