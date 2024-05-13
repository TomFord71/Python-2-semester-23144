import time
import os
import logging
import argparse

# Настройка журналирования
logging.basicConfig(filename='clean_trash.log', level=logging.INFO)

# Функция для очистки мусора
def clean_trash(trash_folder_path, age_thr):
    while True:
        for root, dirs, files in os.walk(trash_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_age = time.time() - os.path.getmtime(file_path)
                if file_age > age_thr:
                    # Журналирование удаления файла
                    logging.info(f"Deleting file: {file_path}")
                    os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if not os.listdir(dir_path):
                    # Журналирование удаления пустой папки
                    logging.info(f"Deleting empty directory: {dir_path}")
                    os.rmdir(dir_path)
        time.sleep(1)

def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Clean trash files and directories.")
    parser.add_argument("--trash_folder_path", required=True, help="Path to the trash folder")
    parser.add_argument("--age_thr", type=int, required=True, help="Threshold age in seconds")
    args = parser.parse_args()

    # Вызов функции очистки мусора
    clean_trash(args.trash_folder_path, args.age_thr)

if __name__ == "__main__":
    main()
