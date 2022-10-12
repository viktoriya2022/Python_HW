# --------------------------------------------------
# 6 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# ---------------------------------------------------


def to_rle(st):  
    code_to_file = []
    count = 1
    for i in range(len(st)-1):
        if i <= len(st):
            if st[i] == st[i + 1]:
                count += 1
            else:
                a = st[i]
                code_to_file.append(str(count))
                code_to_file.append(st[i])
                count = 1
    code_to_file.append(str(count))
    code_to_file.append(st[i])
    return ''.join(code_to_file)


def from_rle(st1): 
    decode = ''
    count = '' 
    for i in st1: 
        if i.isdigit(): 
            count += i 
        else: 
            decode += i * int(count) 
            count = '' 
    return decode


with open('hw5_6.txt') as read_line:
    st = read_line.readline()
with open('hw5_6_1.txt', 'a') as data:
    data.write(to_rle(st))
print(to_rle(st))

with open('hw5_6_1.txt') as read_line1:
    st1 = read_line1.readline()
with open('hw5_6_2.txt', 'a') as data:
    data.write(from_rle(st1))
print(from_rle(st1))
