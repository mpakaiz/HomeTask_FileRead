from operator import itemgetter
with open('file1.txt', 'rt', encoding='utf-8') as file:
    res1 = (file.readlines())
    list1 = []
    for line in res1:
        list1.append(line.strip())

with open('file2.txt', 'rt', encoding='utf-8') as file:
    res2 = (file.readlines())
    list2 = []
    for line in res2:
        list2.append(line.strip())

with open('file3.txt', 'rt', encoding='utf-8') as file:
    res3 = (file.readlines())
    list3 = []
    for line in res3:
        list3.append(line.strip())

gen_dict = {'file1.txt': len(res1), 'file2.txt': len(res2), 'file3.txt': len(res3)}

dict_sorted = dict(sorted(gen_dict.items(), key=itemgetter(1)))

for i in dict_sorted:
    if i == 'file1.txt':
        with open('result.txt', 'a+', encoding='utf-8') as file:
            file.seek(0)
            file.writelines('file1.txt'+'\n')
            file.writelines(str(len(res1))+'\n')
            for i in list1:
                file.writelines(i+'\n')
    if i == 'file2.txt':
        with open('result.txt', 'a+', encoding='utf-8') as file:
            file.seek(0)
            file.writelines('file2.txt'+'\n')
            file.writelines(str(len(res2))+'\n')
            for i in list2:
                file.writelines(i+'\n')
    if i == 'file3.txt':
        with open('result.txt', 'a+', encoding='utf-8') as file:
            file.seek(0)
            file.writelines('file3.txt'+'\n')
            file.writelines(str(len(res3))+'\n')
            for i in list3:
                file.writelines(i+'\n')
