import os
import shutil

main_dir = r'c:\Users\Kirill\HowToMakeAVideoGame'

os.chdir(main_dir)
ar_name = []
count = 0
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        # pass
        f_name = os.path.join(root, name)
        size = os.path.getsize(f_name)
        if size > 1024 * 1024 * 100:  # если больше 100 МБ
            print(f_name, end=' ')
            print(size, 'bytes')
            ar_name.append(f_name)
        count += 1
    # for name in dirs:
    #     print(os.path.join(root, name))

print(count)
# print(ar_name)
# os.chdir(dist_dir)  # Переходим в директорию для копирования

dist_dir = r'f:\tmp2'
for item in ar_name:  # item = '.\Library\il2cpp_cache\linkresult_B5B242D3FD8025D63DCF2ECCC55A7FF5\build.bc'
    # print(item.rfind('\\'))
    # print(item[2:item.rfind('\\')])  # item` = 'Library\il2cpp_cache\linkresult_B5B242D3FD8025D63DCF2ECCC55A7FF5'
    try:
        os.makedirs(dist_dir + '\\' + item[2:item.rfind('\\')])  # создаем директорию "приемник"
    except FileExistsError:
        print('Не удалось создать директорию: ' + dist_dir + '\\' + item[2:item.rfind('\\')])
    try:
        shutil.copy2(main_dir + item[1:], dist_dir + '\\' + item[2:item.rfind('\\')])  # копируем файл в "приемник"
    except PermissionError:
        print('Файл не скопирован: ' + main_dir + item[1:])
    try:
        os.remove(main_dir + item[1:])  # удаляем исходный файл - получем функцию перемещения
    except PermissionError:
        print('Отказано в доступе. Файл не удален: ' + main_dir + item[1:])
