# 作者: Michael(phb)
# 2022年06月13日20时28分05秒
# MAXKEY = 10
#
#
# def elf_bash(hash_str):
#     h = 0
#     g = 0
#     for i in hash_str:
#         h = (h << 4) + ord(i)
#         g = h & 0xf0000000
#         if g:
#             h ^= g >> 24
#         h &= ~g
#     return h % MAXKEY
#
#
# if __name__ == '__main__':
#     str_list = ["yf", "lele", "hanmeimei", "michael", "fenghua"]
#     hash_table = [None] * MAXKEY
#     for i in str_list:
#        hash_table[elf_bash(i)] = i
#     print(hash_table)

# python自带的hash
import hashlib

print(hash('longge'))  # hash里边加了盐值，每次进程结束后，下次启动盐值不一样
print(hash('longge'))
