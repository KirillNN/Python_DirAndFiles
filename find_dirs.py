import os
import shutil
from sys import argv

# print(argv)

# main_dir = r'f:/'
main_dir = r'\\mrs\buffer'
try:
    main_dir = argv[1]
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    # x, y = inst.args
    # print('x =', x)
    # print('y =', y)

find_name = 'History'
# устанавливаем в True если надо удалять каталоги, если False - то просто список выводится
deleted = False

os.chdir(main_dir)
ar_name = []
count = 0
for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        if name == find_name:
            dir_name = os.path.join(root, name)
            print(main_dir + dir_name[1:])
            # ar_name.append(dir_name)
            count += 1
            if deleted:
                try:
                    # os.remove(main_dir + dir_name[1:]) # remove - удаляет только файлы!
                    # os.rmdir(main_dir + dir_name[1:])  # rmdir - для удаления только пустых каталогов!!!!!!!!
                    shutil.rmtree(main_dir + dir_name[1:], ignore_errors=True)
                except Exception as inst:
                    # print('Отказано в доступе. Каталог не удален: ' + main_dir + dir_name[1:])
                    print(type(inst))
                    print(inst.args)
                    print(inst)
                    x, y = inst.args
                    print('x =', x)
                    print('y =', y)

print('Найдено каталогов:', count)
# print(ar_name)
# os.chdir(dist_dir)  # Переходим в директорию для копирования

# dist_dir = r'f:\tmp2'
# for item in ar_name:  # item = '.\Library\il2cpp_cache\linkresult_B5B242D3FD8025D63DCF2ECCC55A7FF5\build.bc'
# print(item.rfind('\\'))
# print(item[2:item.rfind('\\')])  # item` = 'Library\il2cpp_cache\linkresult_B5B242D3FD8025D63DCF2ECCC55A7FF5'
# try:
#     os.makedirs(dist_dir + '\\' + item[2:item.rfind('\\')])  # создаем директорию "приемник"
# except FileExistsError:
#     print('Не удалось создать директорию: ' + dist_dir + '\\' + item[2:item.rfind('\\')])
# try:
#     shutil.copy2(main_dir + item[1:], dist_dir + '\\' + item[2:item.rfind('\\')])  # копируем файл в "приемник"
# except PermissionError:
#     print('Файл не скопирован: ' + main_dir + item[1:])
# try:
#     os.remove(main_dir + item[1:])  # удаляем исходный файл - получем функцию перемещения
# except PermissionError:
#     print('Отказано в доступе. Файл не удален: ' + main_dir + item[1:])
