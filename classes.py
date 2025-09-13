import psutil
import platform
import os
import time

def get_computer_info():
    info = {}

    # Информация о процессоре
    info['cpu_count'] = psutil.cpu_count(logical=True) # логические ядра
    info['cpu_count_physical'] = psutil.cpu_count(logical=False) # физические ядра
    info['cpu_freq'] = psutil.cpu_freq()
    return info
def get_memory_info():
    info={}


    # Информация о памяти
    info['memory_total'] = psutil.virtual_memory().total
    info['memory_available'] = psutil.virtual_memory().available
    info['memory_percent'] = psutil.virtual_memory().percent
    return info
def get_system_info():
    info={}
    # Общая информация об ОС
    info['system'] = platform.system()
    info['node_name'] = platform.node()
    info['release'] = platform.release()
    info['version'] = platform.version()
    info['machine'] = platform.machine()
    info['processor'] = platform.processor()
    return info
def get_path_info():
    info={}
    # Имя пользователя и текущий каталог
    info['user'] = os.getlogin() # или os.getenv('USER') для Linux/macOS
    info['current_directory'] = os.getcwd()

    return info

def write_info_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f: # режим записи 'w', кодировка utf-8
        for key, value in data.items():
            f.write(f"{key}:\n")
            if isinstance(value, dict) or isinstance(value, list):
                import json
                f.write(json.dumps(value, indent=4)) # вывод словарей/списков в JSON-формате
            else:
                f.write(str(value) + "\n")
            f.write("\n") # разделитель
def activate():
    global text1
    global text2
    global text3
    os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    time.sleep(5)
    text1="Ключ применен"
    os.system("slmgr /skms kms.digiboy.ir")
    time.sleep(5)
    text2="Ключ активирован"
    os.system("slmgr /ato")
    time.sleep(5)
    text3="Windows активирован"

if __name__ == "__main__":
    computer_info = get_computer_info()
    write_info_to_file(computer_info, "computer_info.txt")

file=open("computer_info.txt", "r")
write_info_to_file(get_computer_info(), "computer_info.txt")
text1=file.read()
file.close()
file2=open("System.txt", "r")
write_info_to_file(get_system_info(), "System.txt")
text2=file2.read()
file2.close()
file3=open("Memory.txt", "r")
write_info_to_file(get_memory_info(), "Memory.txt")
text3=file3.read()
file3.close()
file4=open("Path.txt", "r")
write_info_to_file(get_path_info(), "Path.txt")
text4=file4.read()
file4.close()