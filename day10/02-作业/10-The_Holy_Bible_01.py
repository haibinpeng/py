f1 = open('The_Holy_Bible.txt', encoding='utf8')
f2 = open('The_Holy_Bible1.txt', 'w', encoding='utf8')
# list1 = [',', '.', ';', ':', '?', '!']  # 这种写法不全
while True:
    txt = f1.readline()
    w = ''
    if not txt:
        break
    # for i in list1:
    #     txt = txt.replace(i, ' ')
    # txt.lower()
    # f2.write(txt)
    for i in txt:
        if not i.isalnum():
            i = i.replace(i, ' ')
        w += i
    f2.write(w.lower() + '\n')
f1.close()
f2.close()
