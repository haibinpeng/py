# 作者: Michael(phb)
# 2022年06月10日10时40分28秒
import os

os.system('wc -m The_Holy_Bible1.txt')  # 统计字符数
os.system('wc -l The_Holy_Bible1.txt')  # 统计行数
os.system('wc -w The_Holy_Bible1.txt')  # 统计字数


def count_word():
    word_frequency = {}
    file1 = open('The_Holy_Bible1.txt', 'r', encoding="utf8")
    str1 = file1.read()
    str1 = str1.replace('\n', '')
    list1 = str1.split(' ')
    for i in list1:
        if i != '':
            if word_frequency.keys().__contains__(i):
                word_frequency[i] += 1
            else:
                word_frequency[i] = 1

    num = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    print('词频最高的前10个单词及其词频依次是：')
    for i in range(10):
        print('%s: %s' % (num[i][0], num[i][1]))
    file1.close()


if __name__ == '__main__':
    count_word()
