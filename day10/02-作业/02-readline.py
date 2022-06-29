f = open('Readme', 'r+', encoding='utf8')
while True:
    txt = f.readline()
    if not txt:
        break
    print(txt, end='')
f.close()
