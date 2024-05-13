import time
import os
import logging
import argparse

logging.basicConfig(filename='clean_trash.log', level=logging.INFO)

def clean_trash(trash_folder_path, age_thr):
    while (1):
        for root, dirs, files in os.walk(trash_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_age = time.time() - os.path.getmtime(file_path)
                if file_age > age_thr:
                    logging.info(f"Deleting file {file_path}")
                    os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if not os.listdir(dir_path):
                    logging.info(f"Deleting empty directory {dir_path}")
                    os.rmdir(dir_path)
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trash_folder_path", required=True)
    parser.add_argument("--age_thr", type=int, required=True)
    args = parser.parse_args()
    clean_trash(args.trash_folder_path, args.age_thr)
