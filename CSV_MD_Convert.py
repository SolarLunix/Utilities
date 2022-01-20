IN = "D:\\Documents\\Code\\testing.csv"
OUT = "D:\\Documents\\Code\\testing.md"

myfilein = ''

with open(IN, 'r') as reader:
    myfilein = reader.readlines()

count = 0
for e, line in enumerate(myfilein):
    line = line.replace(',', '|')
    if e == 0:
        count = line.count('|') + 1
        if line[0] == '|':
            line = '-' + line
    myfilein[e] = '|' + line.replace('\n', '|\n')

headder = '|' + ('---|')*count + '\n'
myfilein.insert(1, headder)

with open(OUT, 'w+') as writer:
    writer.writelines(myfilein)

print(" - - - - - - - ")
print("File: ", IN)
print("Writen to: ", OUT)
print("Job completed sucessfully.")
print(" - - - - - - - ")
