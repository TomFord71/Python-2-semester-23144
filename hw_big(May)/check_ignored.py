import os
import argparse


class IgnoredFile:
    def __init__(self, path, rule):
        self.path = path
        self.rule = rule


def check_ignored(project_dir):
    # Проверяем, что указана директория проекта
    if not project_dir:
        print("Please provide the project directory path.")
        return

    # Проверяем существование указанной директории проекта
    if not os.path.exists(project_dir):
        print(f"The project directory '{project_dir}' does not exist.")
        return

    # Считываем правила из файла .gitignore
    gitignore_path = os.path.join(project_dir, '.gitignore')
    if not os.path.exists(gitignore_path):
        print('No .gitignore file found in the project directory')
        return

    with open(gitignore_path, 'r') as f:
        gitignore_rules = f.readlines()

    # Обрабатываем правила из файла .gitignore
    gitignore_rules = [rule.strip() for rule in gitignore_rules]
    gitignore_rules = [rule.replace("/", "\\") for rule in gitignore_rules if rule and not rule.startswith('#')]

    # Получаем список всех файлов в проекте
    all_files = []
    for root, _, files in os.walk(project_dir):
        for file in files:
            all_files.append(os.path.join(root, file))

    # Проверяем файлы на соответствие правилам из .gitignore
    ignored_files = []
    for rule in gitignore_rules:
        for file in all_files:
            if rule.startswith('*'):
                if file.endswith(rule[1:]):
                    ignored_files.append(IgnoredFile(file, rule))
            elif rule in file:
                ignored_files.append(IgnoredFile(file, rule))

    # Выводим игнорируемые файлы
    if ignored_files:
        print('Ignored files:')
        for file in ignored_files:
            print(file.path.replace(project_dir + os.sep, '').replace("\\", "/"), 'ignored by expression',
                  file.rule.replace("\\", "/"))
    else:
        print('No ignored files found')


def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="Check ignored files in a project directory using .gitignore rules.")
    parser.add_argument('--project_dir', type=str, help='Path to the project directory')

    # Парсим аргументы
    args = parser.parse_args()

    # Вызываем функцию проверки игнорируемых файлов
    check_ignored(args.project_dir)


if __name__ == '__main__':
    main()
